# Codex spike: can we read which skill Codex chose?

Date: 2026-10-26. Agent: Codex CLI 0.144.5, model `gpt-5.6-terra`.

## Question

Can the chosen skill be read from `codex exec --json` output, so pass/fail per trial (and therefore pass@k and pass^k) can be scored automatically?

## Setup

- Toy project with three similar skills in `.agents/skills/`: `pr-description`, `commit-message`, `release-notes`. Each `SKILL.md` had a one-line description and told the agent to start its reply with a canary token (`SKILL_USED_<NAME>`).
- Command: `codex exec -m gpt-5.6-terra --json --ephemeral -s read-only -C . "<request>"`, run in a fresh git repo.
- The model was set on the command line. The `gpt-5.5` default in `~/.codex/config.toml` is rejected by a ChatGPT account (`model_not_found`). `gpt-5.6-luna` also worked in a probe.

## Detection method

A skill load shows up as a `command_execution` event whose command reads `.agents/skills/<name>/SKILL.md`. Matching `skills/([\w-]+)/SKILL\.md` in those commands gives the chosen skill. In every trial the file read and the canary token agreed.

## Results

| Request | Trials | Outcome |
|---|---|---|
| "I am about to open a pull request for my branch. Write the title and body for it." | 1 | `pr-description` |
| "Summarize my recent changes so my teammates can review them." (ambiguous) | 4 | `pr-description` x3, no skill x1 |
| "I have staged changes and want to commit them now. Write the commit message." (clear) | 3 | `commit-message` x3 |

## Conclusions

- Skill choice is observable from the event stream, so scoring can be deterministic. An LLM judge is only needed for borderline items.
- Scoring needs three outcomes: correct skill, wrong skill, and no skill (1 of 4 ambiguous trials loaded none).
- Clear requests were consistent. Ambiguous requests varied, which is the variance pass@k and pass^k measure.

## Limits

- Only 8 trials on 3 skills. This shows the method works, not how often Codex confuses skills.
- Not tested: 4-5 real, longer descriptions installed together, or description truncation.
- Real skills have no canary token, so detection must rely on the file read.
- Results depend on the model and settings (read-only sandbox, ephemeral session, default reasoning effort). Keep them fixed in real runs, and decide which model is the agent under test.
