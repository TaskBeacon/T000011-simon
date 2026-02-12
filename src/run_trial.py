from psyflow import StimUnit
from functools import partial

def run_trial(
    win,
    kb,
    settings,
    condition: str,           # e.g., 'congruent_left'
    stim_bank: dict,
    trigger_runtime=None,
):
    """
    Runs a single trial of the Flanker task.

    Args:
        win: The PsychoPy window object.
        kb: The keyboard handler.
        settings: The task settings object.
        condition (str): A string defining the current trial's type,
                         e.g., "congruent_left".
        stim_bank: The stimulus bank containing all visual stimuli.
        trigger_runtime: The object responsible for sending EEG/fMRI triggers.

    Returns:
        dict: A dictionary containing all data recorded for this trial.
    """
    trial_data = {"condition": condition}
    make_unit = partial(StimUnit, win=win, kb=kb, runtime=trigger_runtime)

    # --- 1. Determine trial properties from condition string ---
    # For Simon task, condition will encode stimulus color and position
    # e.g., 'red_left', 'blue_right'
    stim_color, stim_position = condition.split('_')

    # Determine correct response based on stimulus color (e.g., red -> f, blue -> j)
    if stim_color == 'red':
        correct_response = settings.left_key  # Assuming 'f' is left key
    elif stim_color == 'blue':
        correct_response = settings.right_key # Assuming 'j' is right key
    else:
        raise ValueError(f"Unknown stimulus color: {stim_color}")

    trial_data.update({
        "stim_color": stim_color,
        "stim_position": stim_position,
        "correct_response": correct_response
    })

    # --- 2. Fixation ---
    make_unit(unit_label='fixation') \
        .add_stim(stim_bank.get("fixation")) \
        .show(duration=settings.fixation_duration, onset_trigger=settings.triggers.get("fixation_onset")) \
        .to_dict(trial_data)

    # --- 3. Simon Stimulus & Response ---
    stim_unit = make_unit(unit_label="stimulus")
    
    # Get the pre-defined stimulus from stim_bank based on the condition
    stim = stim_bank.get(condition)
    
    stim_unit.add_stim(stim)
    
    stim_unit.capture_response(
        keys=settings.key_list,
        correct_keys=correct_response, 
        duration=settings.stim_duration,
        response_trigger={settings.left_key: settings.triggers.get("left_key_press"),settings.right_key: settings.triggers.get("right_key_press")},
        onset_trigger=settings.triggers.get("stim_onset"),
        terminate_on_response=True 
    )
    stim_unit.to_dict(trial_data)

    # --- 4. Determine Accuracy and Feedback ---
    response = stim_unit.get_state("response", False)
    hit = stim_unit.get_state("hit", False) # Directly get hit state

    # Determine feedback based on response and hit status
    if response and hit:  # Correct response
        feedback_stim = stim_bank.get("correct_feedback")
        feedback_trigger = settings.triggers.get("feedback_correct_response")
    elif response and not hit:  # Incorrect response
        feedback_stim = stim_bank.get("incorrect_feedback")
        feedback_trigger = settings.triggers.get("feedback_incorrect_response")
    else:  # No response
        feedback_stim = stim_bank.get("no_response_feedback")
        feedback_trigger = settings.triggers.get("feedback_no_response")

    # --- 5. Feedback ---
    make_unit(unit_label="feedback") \
        .add_stim(feedback_stim) \
        .show(duration=settings.feedback_duration, onset_trigger=feedback_trigger) \
        .to_dict(trial_data)

    # --- 6. Inter-Trial Interval (ITI) ---
    make_unit(unit_label='iti').show(duration=settings.iti_duration).to_dict(trial_data)

    return trial_data

