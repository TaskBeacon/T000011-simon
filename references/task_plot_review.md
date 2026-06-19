# Task Plot Review

## Evidence Match

- Pass: title and construct match the Simon task README and logic audit.
- Pass: Congruent and Incongruent rows correctly collapse the four condition tokens.
- Pass: phase order matches `src/run_trial.py`: Fixation -> Simon target -> Feedback -> ITI.
- Pass: timing labels match config: 500 ms fixation, 1000 ms target, 500 ms feedback, 800-1200 ms ITI.
- Pass: response mapping is correct: F = red and J = blue.
- Pass: feedback outcomes show correct, incorrect, and no response.

## Visual Quality

- Pass: labels and timing text are readable.
- Pass: generated timeline content stays below the header band.
- Pass: fixed title and Construct subtitle are centered.
- Pass: top-right TaskBeacon logo lockup is borderless and non-overlapping.
- Pass: no generated title, subtitle, logo, watermark, people, devices, or decorative scene is present.

## README Embed

- Pass: `README.md` contains `## 2. Task Flow`.
- Pass: the section embeds `![Task Flow](task_flow.png)`.
- Pass: final image is saved as `task_flow.png`; raw timeline is saved as `references/task_plot_timeline_raw.png`.
