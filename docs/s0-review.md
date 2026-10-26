# S0: skill-set review and v2 selection

`data/selected200.csv` v1 (commit `b61ffe6`) was hand-reviewed. Rebuilding steps 1-2 and re-running the unmodified step 3 reproduced v1 exactly (all 200 `file_sha` equal), so v2 differs from v1 only by the exclusions below.

## Exclusions (in `scripts/step3_select.py`)

| Rule | Why |
|---|---|
| Repos `skilld-dev/vue-ecosystem-skills` (v1 B2), `ScotterMonk/AgentAutoFlow` (B9), `oguzhan18/angular-ecosystem-skills` (C2), `skylarsabo/code-ops` (C3) | B2 and C2 are keyed by library/API name so confusion is near zero; B9 and C3 are unrelated skills that only share a repo or boilerplate |
| Names `find-skills`, `skill-tree-root` | Meta-skills that can load on any request and would corrupt the isolated baseline |
| Names `coding`, `qa`, `verification`, `audit`, `research`, `debug`, `review` (group E only) | Generic names that overlap each other |

## Result

Groups A and D are identical to v1. Counts are unchanged (A 48, B 48, C 24, D 24, E 56).

| v2 cluster | Repo | Skills |
|---|---|---|
| B11 (new) | Legal-and-General/canopy | canopy-brand-icon, canopy-carousel, canopy-link, canopy-filter-container |
| B12 (new) | sdemyanov/retriever | filter, from-run, sort, scope |
| C5 (new) | saitarrun/devforge-ai | code-standards, cloud-infra, requirements, code-review |
| C6 (new) | DoctorMozg/claude-pipelines | using-mozg-pipelines, vault-answer, vault-connect, init-rules |
| E1-E14 | various | Reshuffled: the exclusions shifted the random pool, so every E cluster after the first removed skill changed |

Cluster ids B/C/E were renumbered. Do not map v1 ids onto v2.

## Kept deliberately

B5 (language rules), B7 (webhooks per vendor), B10 (Teneo agents) and the Amplitude and Umbraco B clusters are templated siblings keyed by platform or vendor. Expect near-100% pass. They are kept as low-confusion-by-design and should be reported as such.

## Open items for S1

- Names with spaces or capitals (`Vincent - Polymarket for agents`, `S2 Retrieve`, `Sage`) need slug install directories.
- Group D copies share one name; install dirs must be unique (`release-a`…`release-d`).
- B11 and C5/C6 are new and unreviewed by a human; check them before drafting questions.
