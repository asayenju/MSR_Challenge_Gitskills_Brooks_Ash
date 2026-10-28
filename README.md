# MSR_Challenge_Gitskills_Brooks_Ash

MSR 2027 Mining Challenge project on the [GitSkills dataset](https://huggingface.co/datasets/mvaccargiu/gitskills) (3.8M `SKILL.md` files from 282K public GitHub repositories).

**Research question:** to what extent can similar agent skills confuse a coding agent into picking the wrong skill?

## Evaluation metrics: pass@k and pass^k

Agent skill choice is probabilistic, so a single run says little. Each request is run **n** times and scored with the two metrics used in Sierra's τ-bench:

- **pass@k**: the probability that at least one of k repeated trials passes. It measures whether the agent *can* pick the right skill.
- **pass^k** (pass-hat-k): the probability that all k repeated trials pass. It measures whether the agent picks the right skill *reliably*.

For a task with n trials of which c pass, the unbiased estimators are:

```
pass@k = 1 - C(n-c, k) / C(n, k)
pass^k = C(c, k) / C(n, k)
```

Both are averaged over tasks. pass@1 and pass^1 are equal; as k grows, pass@k rises and pass^k falls. A wide gap between them on a skill group means the agent sometimes finds the right skill but is not consistent, which is the signature of confusion between similar skills.

In this study:
- a **task** is one user request with a golden answer (the correct skill, plus any acceptable alternatives);
- a **trial** is one agent run on that request with the group's skills installed;
- a trial **passes** when the agent loads the correct (or an acceptable) skill.

Metrics are reported per skill group (below), so the effect of similarity can be compared against the isolated and fork-variant controls.

## Phase 1: grouping similar skills

Phase 1 finds skills that are textually similar and organizes a **200-skill** pilot set into groups by *type of confusion*. It is a feasibility pilot. The selection has not been hand-validated. The first agent runs are in Phase 2 below.

### Pipeline

1. **Filter.** Stream the `artifacts` config with DuckDB, keeping `dedup_primary=1`, valid front matter, and a description of at least 20 characters. This leaves **1,617,013 usable skills** from 221,961 repos.
2. **Sample.** Take 100K English skills, with at most 20 per repo and exact-duplicate descriptions removed (a few registry repos hold 10-27K skills each).
3. **Tokenize and compare.** TF-IDF over `name + description`: scikit-learn's default token pattern (2+ word characters, so hyphenated names are split), lowercase, English stopwords, word 1-2 grams, `min_df=3`, `max_df=0.05` (terms in more than 5% of skills are dropped), sublinear tf, L2-normalized. Top-10 cosine neighbours per skill. There is no stemming or CamelCase splitting.
4. **Group.** Pick skills into five groups with the rules below.

Median top-1 similarity is 0.28 and the 99th percentile is 0.91, where the highest-scoring pairs are near-copies.

### The 200-skill pilot set

| Group | Skills | What it tests |
|---|---|---|
| A. Cross-repo rivals | 48 (12 clusters of 4) | Different repos and names, same job (similarity 0.33-0.75) |
| B. Same-pack siblings | 48 (12 x 4) | Adjacent skills in one repo that would be installed together |
| C. Template families | 24 (6 x 4) | Shared boilerplate descriptions, only the topic differs |
| D. Fork variants | 24 (6 x 4) | Same skill copied across repos with small edits (control: any copy counts as correct) |
| E. Isolated controls | 56 (14 x 4) | Random, unrelated skills (baseline error rate) |

```mermaid
pie showData
    title Pilot set by group (200 skills)
    "A. Cross-repo rivals" : 48
    "B. Same-pack siblings" : 48
    "C. Template families" : 24
    "D. Fork variants" : 24
    "E. Isolated controls" : 56
```

The 200 skills come from 146 repos.

### Findings so far

- **Forks look like rivals.** In the 0.55-0.8 similarity band most cross-repo pairs share a name and are near-identical, so they are copies of one skill, not competitors. They are excluded from group A and kept as the group D control.
- **Real rivals score lower.** Pairs such as `decompose-plan` and `create-plan` score about 0.41, so the rival threshold has to be low.
- **Junk to filter.** Auto-generated `cluster-N` skills, security-test fixtures, and very short descriptions.

### Known limitations

- Lexical similarity misses paraphrase rivals with different wording. An embedding recall check is planned but not done.
- Some clusters are weak (for example `code-ops` and `milvus` in group C share only generic "Use when..." phrasing), and group B shows the sibling pattern but little real confusion.
- Cross-repo similarity only matters if the skills are installed together, so confusion tests need controlled skill sets.
- Some skills have no license listed. Check `repos.license` before redistributing text.

### Reproducing

- `data/selected200.csv`: the 200 selected skills (group, repo, path, name, stars, license, description, file_sha).
- `scripts/step1_filter.py <out.parquet>`: stream-filter usable skills from the Hugging Face parquet.
- `scripts/step2_neighbors.py`: sample 100K and compute TF-IDF neighbours.
- `scripts/step3_select.py`: build the five groups and write the selection.
- `scripts/run_opencode.py GROUP N OUT.csv`: run a group's golden requests on opencode (set `OPENCODE_MODEL`, and `OPENROUTER_API_KEY` for OpenRouter models). `notebooks/run_opencode.ipynb` is the same runner in a notebook.
- `scripts/metrics.py RESULTS.csv`: pass@k and pass^k from a results file.
- `results/A_qwen.csv`, `B_qwen.csv`, `C_qwen.csv`: per-trial results.

The scripts read and write under `data/` relative to the working directory and need `duckdb`, `pandas`, `pyarrow` and `scikit-learn`. Step 1 writes `skills_clean.parquet`, which step 2 expects at `data/skills_clean.parquet`. Descriptions in the CSV come from public repositories and stay under each repo's license.

## Phase 2: first agent runs (groups A, B, C)

**These are pilot numbers, not findings.** The golden requests are unvalidated drafts written by one model (Claude), and each result comes from one cheap model run once per setting.

### Setup

- **Agent:** [opencode](https://opencode.ai) with `qwen3-coder-next` (via OpenRouter, paid) on groups A, B and C. Codex was the planned agent (see `results/codex_spike.md`), but the account hit its usage limit, which resets on Nov 24, 2026. A Claude agent was ruled out because Claude drafted the requests.
- **Install:** for each cluster, its 4 skills are written to `.opencode/skills/<name>/SKILL.md` in a fresh git repo, with the real name and description and a stub body.
- **Trials:** 3 per request (48 requests per group, 144 trials per group and model).
- **Scoring:** the first `skill` tool call in opencode's event stream is the chosen skill. A trial is `correct` (gold or acceptable skill), `wrong` (another skill), `no_skill` (the agent never loaded a skill) or `error` (timeout or crash; counted as a failure).

### Results

| Group | Model | pass@1 | pass@3 | pass^3 | Correct | No skill | Wrong | Error |
|---|---|---|---|---|---|---|---|---|
| A. Cross-repo rivals | Qwen3 Coder Next | 0.479 | 0.667 | 0.292 | 69 | 65 | 7 | 3 |
| B. Same-pack siblings | Qwen3 Coder Next | 0.514 | 0.708 | 0.312 | 74 | 66 | 3 | 1 |
| C. Template families | Qwen3 Coder Next | 0.417 | 0.604 | 0.271 | 60 | 77 | 2 | 5 |

### Reading the results

- **Most failures are skipped skills, not confusion.** `no_skill` is 45-53% of Qwen trials, while wrong picks are 1-5%. When Qwen does load a skill it is right 91% (A), 96% (B) and 97% (C) of the time. Other models may skip less, so this needs a second model to confirm.
- **The pass@k / pass^k gap is mostly skipping too.** The same request is sometimes handled with a skill and sometimes without, so pass@3 is 0.60-0.71 and pass^3 only 0.27-0.31. Under the README's reading, a wide gap signals confusion, but here it mostly reflects an agent that does not reliably reach for a skill.

### Why, by group

These are hypotheses from the numbers, not tested explanations.

- **A. Cross-repo rivals.** 7 wrong picks, concentrated in a few pairs: `query-stringdb` → `lifesciences-proteomics` (3 times), `ssl-certs` → `ssl-certificate-checker` (2), and `data-ai-post-training-expert` → `fine-tuning-expert` (1). In each pair the chosen skill covers the same job under a broader or near-identical name, which is the intended rival effect. Cluster results are uneven: A12 was 12/12, A8 and A10 were 10/12, and A7 (2/12) and A9 (1/12) were mostly skipped. Skipping is probably highest where the model can answer from its own knowledge (for example biology or general ML questions) without a skill.
- **B. Same-pack siblings.** The fewest wrong picks (3) and the highest pass@1 of the three. Siblings from one repo have distinct jobs, so choosing between them is easy once the agent loads one. The wrong picks are `integration-ruby` → `integration-python` (2), which differ only by language, and one `hoyeon-browser-work` → `chrome-browser`. Cluster results swing widely: B8 was 12/12 while B7 was 0/12, all skipped. I have not looked at why B7 is skipped, so that cluster should be checked by hand.
- **C. Template families.** The lowest pass@1 and the most skipped trials (77 of 144). All four skills in a cluster open with the same "This skill should be used when the user asks to ..." boilerplate, so the description gives little to match on, and the golden requests are paraphrased, not the trigger phrases. Only 2 trials were wrong, both to the generic `fret-repo-orientation`, which behaves like a catch-all. Five errors are all timeouts, 4 in cluster C2.

### Caveats

- `no_skill` means the agent never called the skill tool. It may still have answered well from its own knowledge, but it counts as a fail here.
- Skill bodies are stubs ("reply done"), so the agent has little reason to load a skill once it has read its description. This may inflate skipping.
- Results vary between runs. Re-running 12 requests changed 2 outcomes (both from `no_skill` to `correct`).
- Errors are counted as failures, so pass@k is slightly low for groups with many timeouts.
- Groups D and E have not been run, so there is no baseline error rate yet.

## Next steps

1. Hand-review the golden requests per group (`docs/golden-review/`) and swap out weak clusters, then rerun.
2. Run groups D (fork-variant control) and E (isolated controls) for a baseline.
3. Rerun on Codex once the usage limit resets, and on a second non-Claude model, so the result does not depend on one agent.
4. Test whether non-stub skill bodies, or asking the agent to name the skill it would use, change the skipping rate.
5. Reduce cost per run (the Qwen runs cost roughly $0.6-0.7 per 144 trials).
