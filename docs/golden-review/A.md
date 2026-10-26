# A. Cross-repo rivals: review sheet

Status: DRAFT by one model (Claude). Not yet blind-labelled by a second model.

Mark each row **Agree** (gold is right), **Alt** (another installed skill also acceptable: name it) or **Rewrite** (ambiguous or leaks the answer). Decide from the descriptions only, as the agent would.


## A1

Installed skills:

- **analysis-api-create-cherry-pick-issue** (JetBrains/kotlin): Create a KTIJ cherry-pick tracking issue for a KT fix that needs to be cherry-picked to an IntelliJ branch. Use when cherry-picking Analysis API fixes.
- **qa-cherry-picks** (Moonsong-Labs/knowledge-work-plugins): QA cherry-pick tracking documents for polkadot-sdk fork upgrades. Use when auditing, verifying, or updating cherry-pick tables in docs/cherry-picks/, when upgrading to a new polkadot-sdk stable branch, or when checking if a cherry-pick was applied.
- **release-create-tracker-issue** (pytorch/test-infra): Generate (and optionally open) a PyTorch release tracker / cherry-pick tracking issue from a release announcement, like https://github.com/pytorch/pytorch/issues/180506. Triggered by mentions of "release tracker", "release tracking issue", "cherry-pick tracker", or "cut a release branch issue".
- **cherry-pick-release** (tomsej/dotfiles): Create a release branch from main, cherry-pick specific commits from test, and validate the result. Use when preparing a production release by cherry-picking commits, checking scope and parity with the test branch.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| A-A1-001 | I just fixed a bug in the Kotlin Analysis API and it has to be backported to the IntelliJ branch. Can you file the ticket that tracks getting it over there? | analysis-api-create-cherry-pick-issue |  | boundary | ok | |
| A-A1-002 | We're moving our polkadot-sdk fork to the next stable branch. Go through the table of patches we carry and check which ones are already upstream and which still need applying. | qa-cherry-picks |  | clear | ok | |
| A-A1-003 | Turn this PyTorch release announcement into the issue where we'll track everything that lands on the release branch. | release-create-tracker-issue |  | boundary | ok | |
| A-A1-004 | We're getting ready to go live: branch off main, bring across just the approved commits from the test branch, and confirm the result matches what test had. | cherry-pick-release |  | clear | ok | |

## A2

Installed skills:

- **fine-tuning-expert** (Jeffallan/claude-skills): Use when fine-tuning LLMs, training custom models, or adapting foundation models for specific tasks. Invoke for configuring LoRA/QLoRA adapters, preparing JSONL training datasets, setting hyperparameters for fine-tuning runs, adapter training, transfer learning, finetuning with Hugging Face PEFT, OpenAI fine-tuning, instruction tuning, RLHF, DPO, or quantizing and deploying fine-tuned models. Trigger terms include: LoRA, QLoRA, PEFT, finetuning, fine-tuning, adapter tuning, LLM training, model training, custom model.
- **optimizing-models** (gitwalter/antigravity-agent-factory): LoRA/QLoRA/PEFT fine-tuning workflows with Hugging Face transformers
- **finetuning-strategy-advisor** (Cloud-Byte-Consulting/plugins): Decide among prompting, RAG, PEFT/LoRA, full fine-tuning, and continued pretraining, then design a response-masked PEFT workflow and Kubernetes training job. Use for fine-tune-versus-RAG decisions, LoRA/QLoRA/AdaLoRA, adapters, instruction or domain tuning, quantized training, Hugging Face Trainer, target modules, checkpointing, or evaluation of an adapted model.
- **data-ai-post-training-expert** (scanady/nexus-skills): Use when designing or implementing LLM post-training workflows, including supervised fine-tuning, parameter-efficient adaptation, preference optimization, reward modeling, RLHF, distillation, or deployment packaging. Invoke for SFT, LoRA/QLoRA/PEFT, DPO/ORPO/PPO/GRPO, preference dataset preparation, adapter merging, model compression, and serving tradeoffs.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| A-A2-005 | I have a JSONL file of customer-support chats. Set up an adapter-training run for it with sensible hyperparameters, then quantize the result so I can deploy it. | fine-tuning-expert |  | boundary | ok | |
| A-A2-006 | Show me how to fine-tune a Llama model with QLoRA using Hugging Face transformers. | optimizing-models | fine-tuning-expert | boundary | ok | |
| A-A2-007 | Should we tune a model or just use retrieval for our legal Q&A bot? If tuning wins, plan the training job to run on our cluster. | finetuning-strategy-advisor |  | clear | ok | |
| A-A2-008 | We need to align our model with human preference data: build the reward model, run DPO, then package it for serving. | data-ai-post-training-expert |  | clear | ok | |

## A3

Installed skills:

- **train-sft** (OpenPipe/ART): SFT training reference for the ART framework. Use when the user asks to create, write, or help with an SFT training script, fine-tune a model, train from a JSONL dataset, do distillation, or anything related to supervised fine-tuning.
- **tao-finetune-cosmos-reason** (AshishKmj/MJChatSyncs): Cosmos-Reason2-8B video QA supervised fine-tuning with FSDP parallelism. Use when training or evaluating video question-answering models, fine-tuning Cosmos-Reason2 with SFT, or working with Cosmos-RL. Trigger phrases include "fine-tune Cosmos-Reason", "Cosmos-RL SFT", "video QA fine-tune", "Cosmos-Reason2-8B training".
- **tinker_training_usage** (yotaro-shimose/adapter-agent): Comprehensive guide on using Tinker for Reinforcement Learning (trajectories) and Supervised Fine-Tuning (SFT) using optimized look-ahead batching.
- **trl-training** (ARareUsername/tbats-dev): Train and fine-tune transformer language models using TRL (Transformers Reinforcement Learning). Supports SFT, DPO, GRPO, KTO, RLOO and Reward Model training via CLI commands.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| A-A3-009 | Write me a supervised fine-tuning script for the ART framework that trains from this JSONL dataset. | train-sft |  | clear | 4gram:for the art framework | |
| A-A3-010 | I want to adapt Cosmos Reason2 to answer questions about our warehouse videos, sharded across several GPUs. | tao-finetune-cosmos-reason |  | clear | ok | |
| A-A3-011 | Using Tinker, how do I run a reinforcement learning loop over trajectories with efficient batching? | tinker_training_usage |  | clear | ok | |
| A-A3-012 | Kick off a KTO run from the command line on my preference data using TRL. | trl-training |  | boundary | ok | |

## A4

Installed skills:

- **graphite** (lightdash/lightdash): Manage stacked PRs with Graphite CLI (gt) instead of git for branch/PR operations. Auto-detects Graphite repos via .git/.graphite_repo_config. Use when: creating stacked PRs, navigating branches, submitting PRs, syncing with main, restacking after changes, or any gt command usage.
- **stackit** (ok-very/autoart): Manage stacked Git branches with Stackit. Use when creating/managing stacked branches, submitting PRs for branch stacks, navigating branch trees, rebasing stacks, syncing with main/trunk, troubleshooting stack issues, absorbing changes, resolving rebase conflicts, or any workflow involving dependent Git branches. Keywords stackit, stacked changes, stacked PRs, branch stack, restack, absorb, git stack.
- **socle-cli** (benekuehn/socle): Use this skill when you need to guide or automate usage of the socle CLI (the `so` command) for stacked-branch workflows, including installing `so`, tracking branch stacks, navigating up/down/top/bottom, creating stacked branches, restacking, syncing, or submitting stacked PRs.
- **git-spice** (carrieforde/grove): Manage stacked Git branches with Git Spice (gs). Use when working with stacked PRs, managing dependent branches, submitting multiple related PRs, restacking branches after changes, or navigating branch hierarchies. Triggers: gs, git-spice, stacked branches, stacked PRs, restack, upstack, downstack.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| A-A4-013 | This repo has a .graphite_repo_config. I amended the bottom commit of my stack, so restack everything above it and then submit the whole stack. | graphite |  | boundary | name:graphite | |
| A-A4-014 | Absorb my staged fixes into the right branches of my stack, and sort out the rebase conflicts that come up. | stackit |  | clear | ok | |
| A-A4-015 | Install the `so` command, start tracking my branch stack, and move me to the top of it. | socle-cli |  | clear | ok | |
| A-A4-016 | Using gs, show me the downstack of this branch and restack everything upstack of it. | git-spice |  | clear | ok | |

## A5

Installed skills:

- **wordpress-app** (shiaho777/web-to-app): Build a WordPress theme or plugin for the on-device WordPress runtime
- **wordpress-master** (suderman/opencode): Use for WordPress theme, plugin, CPT, custom block, Timber/Twig, Composer/Bedrock-style, WooCommerce, performance, security, migration, or debugging work.
- **wordpress-theme** (michalstaniecko/wp-theme-sardynkibiznesu-2.0): Use this skill when working with WordPress theme files, templates, hooks, filters, or theme architecture. Covers functions.php, template hierarchy, inc/ modules, and theme customization.
- **find-plugin** (PeterBooker/ai-wp-builder): Identify whether an existing WordPress plugin or WordPress Core already covers required functionality before building a custom solution.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| A-A5-017 | Build a plugin for the WordPress that runs on-device on my phone. | wordpress-app |  | clear | ok | |
| A-A5-018 | I need a WooCommerce custom post type with a Timber/Twig template, and a security problem in my Bedrock-style setup fixed. | wordpress-master |  | boundary | ok | |
| A-A5-019 | I'm editing functions.php and need to understand the template hierarchy so I can override the archive page. | wordpress-theme |  | clear | ok | |
| A-A5-020 | Before I code a custom contact form, check whether an existing plugin or core WordPress already does it. | find-plugin |  | clear | ok | |

## A6

Installed skills:

- **certificate-monitoring** (davepoon/buildwithclaude): Use when the user asks about SSL/TLS certificates, certificate expiration, monitoring domains for cert health, or issuing free Let's Encrypt certificates. Triggers include "is my cert expiring", "scan ssl on X", "check certificate", "monitor this domain", "issue a free cert", "renew certificate", "Let's Encrypt", "TLS Radar". This skill picks the right TLS Radar tool for each question.
- **ssl-certs** (KaiserWhoLearns/skillsbench): Manage SSL/TLS certificates and diagnose certificate issues. Use when the user says "cert expiring", "SSL error", "certificate problem", "renew certificate", "check certificate", "HTTPS not working", or asks about TLS/SSL.
- **leet-ssl-cert-create** (pengfeng/leet-ssl-cert-python): Issue an SSL/TLS certificate with leet-ssl-cert. Use when the user asks to create, issue, request, or renew a certificate for one or more domains. The only required input from the user is the domain name; everything else is loaded from .env defaults or sensible presets.
- **ssl-certificate-checker** (mcyork/skillseal-demo-plugin): Check SSL/TLS certificates on remote hosts using openssl s_client

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| A-A6-021 | Scan example.com, tell me when its certificate expires, and keep watching the domain for cert health. | certificate-monitoring | ssl-certificate-checker | boundary | ok | |
| A-A6-022 | My site shows an HTTPS error in the browser and I think the certificate is the problem. Diagnose it. | ssl-certs | certificate-monitoring | boundary | ok | |
| A-A6-023 | Get me a certificate for shop.example.com and api.example.com. | leet-ssl-cert-create | certificate-monitoring | boundary | ok | |
| A-A6-024 | Use openssl to look at the certificate presented by mail.example.org on port 443. | ssl-certificate-checker |  | clear | ok | |

## A7

Installed skills:

- **draft-pr** (ComplianceAsCode/content): Open a pull request in the browser with prefilled title, description, and labels
- **ghpr** (kodingwarrior/minimalism-workflow): Create a GitHub pull request with auto-generated title and body from commits. Use when the user wants to create a PR, open a pull request, or says "ghpr".
- **open-pr** (bhingston-va/dotfiles): Open a draft pull request for the current branch. Use when the user wants to create a PR, open a pull request, or submit work for review. PRs are always created as drafts.
- **create-pr** (kurko/dotfiles): Create a GitHub pull request from the current branch. Use when user asks to create a PR, open a PR, submit a PR, push and create PR, or similar pull request workflows. Activates for phrases like "create a PR", "open a pull request", "submit PR", "push and PR", "make a PR for this", "open a draft PR".

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| A-A7-025 | Open the new pull request page in my browser with the title, body and labels already filled in. | draft-pr |  | clear | ok | |
| A-A7-026 | Draft the pull request text out of my commits and create it on GitHub. | ghpr | create-pr | boundary | ok | |
| A-A7-027 | Submit my work for review, but as a draft since it isn't ready. | open-pr | create-pr | boundary | ok | |
| A-A7-028 | Push my branch and make a PR for this. | create-pr | open-pr, ghpr | boundary | 4gram:a pr for this | |

## A8

Installed skills:

- **hf-bf16-gguf-conversion-jobs** (Mesh-LLM/mesh-llm): Use when converting Hugging Face SafeTensors checkpoints into split BF16 GGUF model repos with skippy-quantize on Hugging Face Jobs or a local machine, then publishing the artifact to Hugging Face.
- **hf-jobs-operator** (BetterAndBetterII/ml-intern-codex): Use this skill for Hugging Face jobs inspection, summarize, and runbook flows.
- **hugging-face-jobs** (bcastelino/agent-skills-kit): This skill should be used when users want to run any workload on Hugging Face Jobs infrastructure. Covers UV scripts, Docker-based jobs, hardware selection, cost estimation, authentication with tokens, scheduled jobs, and result persistence.
- **model-publisher** (Rachasumanth/text2llm001): Package trained checkpoints, generate model cards, and publish releases to Hugging Face Hub with optional GGUF export.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| A-A8-029 | Convert my SafeTensors checkpoint into split BF16 GGUF files with skippy-quantize and push them to the Hub. | hf-bf16-gguf-conversion-jobs |  | clear | 4gram:into split bf16 gguf | |
| A-A8-030 | Summarize the status of my recent Hugging Face jobs and give me a runbook for the ones that failed. | hf-jobs-operator |  | boundary | ok | |
| A-A8-031 | I want to run a Python training script on Hugging Face's cloud hardware. Pick the GPU and estimate the cost. | hugging-face-jobs |  | clear | ok | |
| A-A8-032 | Package my trained checkpoint with a model card and publish it on the Hub, including a GGUF export. | model-publisher |  | boundary | ok | |

## A9

Installed skills:

- **string-database** (google-deepmind/science-skills): Query the STRING database for protein-protein interactions (PPIs), functional enrichment, and homology. Use when the user asks about interactions between specific proteins, interaction evidence, confidence scores, protein interaction partners, or pathway enrichments.
- **query-stringdb** (Runchuan-BU/BioClaw): Query STRING for protein-protein interactions. Use when user asks about protein interactions, interaction networks, binding partners, or interactome. Triggers on "string", "protein interaction", "interaction network", "binding partners", "interactome", "PPI".
- **string-ppi-enrichment** (InternScience/scp): Analyze protein-protein interaction enrichment using STRING database to identify functional networks and pathway associations.
- **lifesciences-proteomics** (donbr/lifesciences-deepagents): Queries protein databases (UniProt, STRING, BioGRID) via MCP tools for protein lookups, protein-protein interactions, functional enrichment analysis, and cross-database ID mapping. Falls back to curl when MCP is unavailable. This skill should be used when the user asks to "find protein interactions", "analyze interaction networks", "perform GO enrichment", "map protein IDs", or mentions PPI networks, UniProt accessions, STRING scores, BioGRID interactions, or protein ID conversion between databases.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| A-A9-033 | What is the confidence score for the interaction between TP53 and MDM2, and what evidence supports it? | string-database |  | clear | ok | |
| A-A9-034 | List the binding partners of BRCA1 and show me the interaction network. | query-stringdb | string-database | boundary | ok | |
| A-A9-035 | Is my list of 40 genes enriched for protein-protein interactions, and which pathways do they cluster in? | string-ppi-enrichment |  | boundary | ok | |
| A-A9-036 | Convert these UniProt accessions to STRING IDs and run GO enrichment on them. | lifesciences-proteomics |  | clear | ok | |

## A10

Installed skills:

- **Vincent - Polymarket for agents** (LeoYeAI/openclaw-master-skills): Polymarket prediction market trading for agents. Use this skill when users want to create a Polymarket wallet, browse markets, place bets, manage positions, or withdraw funds. Triggers on "polymarket", "prediction market", "place bet", "browse markets", "trade prediction", "polymarket wallet", "betting", "market odds".
- **polymarket-market-pulse** (Alchemist-X/all-polymarket-skill): Discover profitable prediction markets on Polymarket by comparing AI-estimated probabilities against market-implied odds. Identifies the top 3 markets with the highest edge, analyzes information flow, resolution clarity, liquidity, and volatility, and provides position sizing recommendations. Use when the user asks about Polymarket opportunities, prediction market bets, daily market pulse, market recommendations, or finding mispriced markets.
- **polymarket-correlation** (captainslab/captains-simmerbot): Detect mispriced correlations between Polymarket prediction markets. Cross-market arbitrage finder for AI agents.
- **get-prediction-markets** (koala73/worldmonitor): Retrieve active prediction-market contracts (Polymarket) with live yes-price probabilities, volume, and close dates, filterable by category or keyword. Use when the user asks what the market odds are on a geopolitical, economic, or election outcome.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| A-A10-037 | Create a wallet for Polymarket and place a bet on the election market. | Vincent - Polymarket for agents |  | clear | ok | |
| A-A10-038 | Which Polymarket markets look mispriced today? Give me the best three with position sizes. | polymarket-market-pulse |  | clear | ok | |
| A-A10-039 | Find pairs of related prediction markets whose prices contradict each other so I can arbitrage them. | polymarket-correlation |  | clear | ok | |
| A-A10-040 | What are the market odds right now on the next central bank rate cut? | get-prediction-markets |  | boundary | ok | |

## A11

Installed skills:

- **tdd-red-green-refactor** (google-labs-code/stitch-sdk): Enforces a disciplined Red-Green-Refactor (TDD) workflow in TypeScript/Node.js. Use this whenever creating new features, fixing bugs, or migrating logic to ensure high-quality, verifiable implementations.
- **afb-tdd** (afbreilyn/afb-tdd): Interactive red-green-refactor TDD workflow. Invoke when writing new features or fixing bugs test-first.
- **tdd-workflow** (noooooooooooooooob/Rift): Test-Driven Development workflow. RED-GREEN-REFACTOR cycle. Use when implementing new features or fixing bugs.
- **tdd-standard-practice** (RyoMurakami1983/skills_repository): Standardize a production TDD workflow with test lists and Red-Green-Refactor.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| A-A11-041 | I'm adding a feature to my Node.js TypeScript service. Drive it strictly with red-green-refactor. | tdd-red-green-refactor |  | clear | ok | |
| A-A11-042 | Let's build this test-first, interactively, walking through each red, green and refactor step together. | afb-tdd | tdd-workflow | boundary | ok | |
| A-A11-043 | Fix this bug test-driven. | tdd-workflow | afb-tdd, tdd-standard-practice, tdd-red-green-refactor | boundary | ok | |
| A-A11-044 | Set up a production-grade TDD process for our team, starting from a test list. | tdd-standard-practice |  | clear | ok | |

## A12

Installed skills:

- **daily_briefing** (siddsachar/row-bot): Compile a morning briefing with weather, calendar, and news headlines.
- **morning** (tnez/dotfiles): Synthesize a morning briefing from GH notifications, calendar, reminders, and inbox.
- **start-the-day** (autonomy-cloud/kairos-interface): Get a personalized daily briefing with weather, news, and actionable insights
- **google_news** (0xmariowu/Autosearch): Current news headlines aggregated across publishers via Google News RSS (English US feed).

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| A-A12-045 | Give me a morning rundown with the weather, my calendar and the headlines. | daily_briefing | start-the-day, morning | boundary | name:morning | |
| A-A12-046 | Start my day: what's in my GitHub notifications, reminders and inbox? | morning |  | clear | ok | |
| A-A12-047 | Give me a personalized briefing for today with the weather and news, plus what I should act on. | start-the-day | daily_briefing | boundary | ok | |
| A-A12-048 | What are the top US news headlines right now? | google_news |  | clear | ok | |
