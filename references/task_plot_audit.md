# Task Plot Audit

- generated_at: 2026-03-23T23:47:10.588495+08:00
- mode: existing
- task_path: E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000011-simon

## 1. Inputs

- `README.md`
- `config/config.yaml`
- `src/run_trial.py`
- `main.py` provides block-level screens (`instruction`, `block_break`, `good_bye`); `src/run_trial.py` provides the trial-level timeline.

## 2. README Alignment

- `Trial-Level Flow` maps to `pre_stim_fixation`, `simon_response`, `feedback`, and `iti`.
- Condition tokens are `red_left`, `red_right`, `blue_left`, and `blue_right`.
- The rendered plot is aligned to the README's task-flow description.

## 3. Config-Derived Parameters

- `fixation_duration = 0.5 s`
- `stim_duration = 1.0 s`
- `feedback_duration = 0.5 s`
- `iti_duration = [0.8, 1.2] s`
- `fixation` displays a centered `+`.
- `red_left` / `red_right` / `blue_left` / `blue_right` display a colored circle on the congruent or incongruent side.
- `feedback` uses `correct_feedback`, `incorrect_feedback`, or `no_response_feedback` depending on response outcome.
- `iti` is represented as a blank inter-trial interval.

## 4. Generated task_plot_spec

- `root_key`: `task_plot_spec`
- `spec_version`: `0.2`
- The spec contains four condition timelines matching the four Simon stimulus combinations.
- Each timeline contains four phases: `Fixation`, `Simon Response`, `Feedback`, and `ITI`.
- `Simon Response` depicts the condition-specific colored circle and response window.
- `Feedback` depicts the possible outcomes: correct, incorrect, or no response.
- `ITI` depicts the blank inter-trial interval.

## 5. Rendering Decisions

- Used a multi-condition timeline layout to show all four Simon conditions.
- Kept timing labels adjacent to each phase and separated condition labels from screen thumbnails.
- Rendered `Simon Response` with position-specific colored-circle examples.
- Used an image reference for the feedback-outcome panel so the three outcomes remain visually compact.

## 6. Rendering QA

- `output_file`: `task_flow.png`
- `dpi`: `300`
- `max_conditions`: `4`
- `screens_per_timeline`: `4`
- `screen_overlap_ratio`: `0.1`
- `screen_slope`: `0.08`
- `screen_slope_deg`: `25.0`
- `screen_aspect_ratio`: `1.4545454545454546`
- `qa_mode`: `local`
- `auto_layout_feedback`:
  - `layout pass 1: crop-only; left=0.064, right=0.076, blank=0.189`
- `auto_layout_feedback_records`:
  - `pass: 1`
    `metrics`: `{'left_ratio': 0.0644, 'right_ratio': 0.0756, 'blank_ratio': 0.1889}`
- `validator_warnings`: `none`

## 7. Source Hashes

- `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000011-simon\references\task_plot_spec.yaml`: `sha256=3518e8db89bce6b7b0b0d5fcb78b2e0e4e6e42423ec80ce362997d0ed28b68b2`
- `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000011-simon\references\task_plot_spec.json`: `sha256=21d99027696c11fe5472ba98a3a8b481b4ab06ef20096d307e22f4653eed07f5`
- `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000011-simon\task_flow.png`: `sha256=6b6294e2f258fd75931d7db636c49c7504f7a02ec8d5a16262b78c75a723ee01`
- `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000011-simon\references\task_plot_source_excerpt.md`: `sha256=defbf29616d7d6217bbcec24696bf2abc8a6a60ce68595df450eca160a926114`
- `E:\xhmhc\TaskBeacon\benchmark\reports\task_plot_redo_T000011_simon_summary.md`: `sha256=40733c5205190fb026bd31d0b5ca4e5045bb56bd7c262b5ab9e94063f3ac7cf8`
- `E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000011-simon\references\feedback_outcomes_text.png`: `sha256=67c50915b976b55075ddf342c7746d0421b682d404d7bdc2600ba9ec683ea473`


## 8. Conclusion

- The task-plot artifact is structurally aligned with the Simon trial timeline.
- The figure covers all four implemented stimulus conditions.
- `README.md` includes `task_flow.png` as the task-flow preview.
