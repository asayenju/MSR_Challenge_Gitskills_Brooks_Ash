# C. Template families: review sheet

Status: DRAFT by one model (Claude). Not yet blind-labelled by a second model.

Mark each row **Agree** (gold is right), **Alt** (another installed skill also acceptable: name it) or **Rewrite** (ambiguous or leaks the answer). Decide from the descriptions only, as the agent would.


## C1

Installed skills:

- **fret-workstream-lifecycle** (Latias94/fret): This skill should be used when the user asks to "start a new workstream", "resume a fearless refactor lane", "record workstream progress", "split a narrow follow-on", or "close out a lane". Provides a lightweight workstream lifecycle for Fret: scaffold the right docs, keep lane state explicit, resume existing lanes with an assumptions-first evidence pass, attach repro/gate/evidence to each slice, and leave closeout notes without reopening scope by accident.
- **fret-mobile-real-device-debug** (Latias94/fret): This skill should be used when the user asks to "debug on real mobile devices", "run the smallest Android/iOS target", "verify Vulkan/Metal constraints", or "capture mobile diagnostics evidence". Provides a real-device workflow (Android + iOS) to reproduce issues, capture bundles, and archive evidence for ADRs/workstreams.
- **fret-boundary-checks** (Latias94/fret): This skill should be used when the user asks to "run layering checks", "verify crate boundaries", "prevent winit/wgpu leakage", or "refactor across crates safely". Provides a guardrail workflow (layering checks, forbidden-dep spot checks, drift reports) to keep contract crates portable during refactors.
- **fret-repo-orientation** (Latias94/fret): This skill should be used when the user asks to "find the right crate/layer", "locate entry points", "choose the smallest runnable target", or "get oriented in the Fret repo". Provides a navigation workflow to map an intent to the correct layer and pick the fastest runnable demo/harness to iterate.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| C-C1-001 | I paused a big refactor effort last week. Pick it back up and re-check what's still true before touching anything. | fret-workstream-lifecycle |  | clear | ok | |
| C-C1-002 | This line of work is finished. Write the wrap-up notes so nobody accidentally reopens its scope. | fret-workstream-lifecycle |  | clear | ok | |
| C-C1-003 | The rendering glitch only reproduces on my Pixel and an iPhone. Get the smallest build running on both and collect logs I can attach to the design record. | fret-mobile-real-device-debug |  | clear | ok | |
| C-C1-004 | Check that our GPU backend assumptions actually hold on physical phones, not simulators. | fret-mobile-real-device-debug |  | boundary | ok | |
| C-C1-005 | Before I start restructuring code that spans several crates, make sure the platform windowing library hasn't leaked into the portable core. | fret-boundary-checks |  | clear | ok | |
| C-C1-006 | Did my last change break any crate layering rules? Report any drift. | fret-boundary-checks |  | clear | ok | |
| C-C1-007 | I'm new to this codebase. Where should a keyboard-shortcut feature live, and what's the quickest demo to try it in? | fret-repo-orientation |  | clear | ok | |
| C-C1-008 | Which crate owns text input, and what's the fastest thing I can run to iterate on it? | fret-repo-orientation |  | boundary | ok | |

## C2

Installed skills:

- **indexing** (zilliztech/milvus-marketplace): Use when user needs to create collections, indexes in Milvus. Triggers on: indexing, collection, create index, HNSW, IVF, schema, Milvus collection, vector storage.
- **embedding** (zilliztech/milvus-marketplace): Use when user needs to convert text/images to vectors. Triggers on: embedding, vectorize, encode, text-to-vector, model selection, sentence-transformers, OpenAI embeddings, BGE, CLIP.
- **rag** (zilliztech/milvus-marketplace): Use when user wants to build RAG, Q&A system, or knowledge base with documents. Triggers on: RAG, retrieval augmented generation, Q&A system, knowledge base, document Q&A, chat with docs, ChatGPT for docs, LLM + retrieval, semantic search over documents, ground LLM with facts, reduce hallucination, enterprise search.
- **pilot** (zilliztech/milvus-marketplace): Use when user wants to build AI applications, data pipelines, or any development project. Triggers on: AI application, build, project, data, pipeline, API, service, backend, LLM, GPT, Claude, model. Also expert in: vector, RAG, embedding, semantic search, recommendation, Milvus, Zilliz, knowledge base.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| C-C2-009 | Create a collection with an HNSW index in Milvus for 768-dimensional vectors. | indexing |  | clear | ok | |
| C-C2-010 | I have 10 million vectors. Should I use IVF or HNSW, and how should the schema look? | indexing |  | boundary | ok | |
| C-C2-011 | Convert my product photos and their captions into vectors. Which model should I use? | embedding |  | clear | ok | |
| C-C2-012 | Compare BGE and OpenAI embeddings for encoding my support tickets. | embedding |  | clear | name:embedding | |
| C-C2-013 | Build a chat-with-our-docs system over the company wiki that reduces hallucination. | rag |  | clear | ok | |
| C-C2-014 | I want semantic search over our contract PDFs that grounds the model's answers in the text. | rag |  | boundary | ok | |
| C-C2-015 | I want to build a backend API for a movie recommendation service. | pilot |  | boundary | ok | |
| C-C2-016 | Help me design a data pipeline for an LLM-powered application. | pilot |  | boundary | ok | |

## C3

Installed skills:

- **qa-auth** (baddenboy12/GroundWork): Automated QA testing for authentication flows including Keycloak sign-in, sign-up, callback handling, and session management
- **qa-sites** (baddenboy12/GroundWork): Automated QA testing for site management including create, edit, delete, sidebar, location picker, and team deletion voting
- **qa-landing** (baddenboy12/GroundWork): Automated QA testing for the GroundWork landing page, hero section, pricing carousel, navigation, and responsive layout
- **qa-export** (baddenboy12/GroundWork): Automated QA testing for PDF, Excel, and CSV export features including themes, filters, tier gating, and download verification

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| C-C3-017 | Test the sign-in and sign-up flows end to end, including the callback after login. | qa-auth |  | clear | ok | |
| C-C3-018 | Verify that a user whose session times out gets handled correctly when they come back. | qa-auth |  | clear | ok | |
| C-C3-019 | Test creating, editing and deleting a site, including the sidebar and location picker. | qa-sites |  | clear | ok | |
| C-C3-020 | Make sure the team vote works when someone wants to delete a site. | qa-sites |  | boundary | ok | |
| C-C3-021 | Test the marketing homepage hero and pricing carousel at mobile widths. | qa-landing |  | clear | ok | |
| C-C3-022 | Check that the top navigation links on the public front page all work. | qa-landing |  | clear | ok | |
| C-C3-023 | Verify the PDF, Excel and CSV downloads come out right when filters are applied. | qa-export |  | clear | 4gram:pdf excel and csv | |
| C-C3-024 | Check that free accounts can't download spreadsheet exports but paid tiers can. | qa-export |  | boundary | ok | |

## C4

Installed skills:

- **google-local-services-search** (FinpeakInc/frevana-skills): Use when the user wants Google Local Services results through Frevana, including local service categories, job type filters, and place/provider identifiers.
- **ebay-search** (FinpeakInc/frevana-skills): Use when the user wants eBay product listing search results through Frevana, including keyword search, category-specific search, eBay domain selection, pagination, or result-count control.
- **google-videos-search** (FinpeakInc/frevana-skills): Use when the user wants Google Videos results through Frevana, including localization, language restriction, safe search, advanced filters, pagination, or device-specific results.
- **local-knowledge** (FinpeakInc/frevana-skills): Use when the user wants to query specific information inside a local directory or file, turn local documents into a private local knowledge base, install local embedding dependencies, index files with a local sentence-transformers-compatible embedding model, search relevant passages, or retrieve context for an agent to answer questions without uploading source documents by default.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| C-C4-025 | Find plumbers near Austin from Google's local services listings, filtered by job type. | google-local-services-search |  | clear | ok | |
| C-C4-026 | Get the provider identifiers for HVAC services in this city. | google-local-services-search |  | clear | ok | |
| C-C4-027 | Search eBay UK for vintage film cameras and give me 50 results. | ebay-search |  | clear | ok | |
| C-C4-028 | List the first two pages of eBay listings for a mechanical keyboard in the electronics category. | ebay-search |  | clear | ok | |
| C-C4-029 | Get video search results for 'sourdough starter' in French with safe search on. | google-videos-search |  | clear | ok | |
| C-C4-030 | Pull mobile-specific video results for this topic, filtered to the past month. | google-videos-search |  | clear | ok | |
| C-C4-031 | Index the markdown files in this folder so I can privately ask questions over them. | local-knowledge |  | clear | ok | |
| C-C4-032 | Search my local PDF folder for passages about the warranty terms. | local-knowledge |  | boundary | ok | |

## C5

Installed skills:

- **code-standards** (saitarrun/devforge-ai): This skill should be used when the user mentions keywords related to code-standards.
- **cloud-infra** (saitarrun/devforge-ai): This skill should be used when the user mentions keywords related to cloud-infra.
- **requirements** (saitarrun/devforge-ai): This skill should be used when the user asks to "write requirements", "create user stories", "define acceptance criteria", "decompose a feature", "analyze an issue", "write a PRD", "create user stories", "acceptance criteria", "roadmap", "feature spec", or discusses "INVEST" criteria, "ambiguity", or "story estimation".
- **code-review** (saitarrun/devforge-ai): This skill should be used when the user mentions keywords related to code-review.

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| C-C5-033 | Write user stories and acceptance criteria for a password reset feature. | requirements |  | clear | ok | |
| C-C5-034 | Break this vague feature request down into stories I can estimate. | requirements |  | clear | ok | |
| C-C5-035 | Check this module against our team's naming and style conventions. | code-standards | code-review | boundary | ok | |
| C-C5-036 | Set up the coding conventions we should follow across this repo. | code-standards |  | boundary | ok | |
| C-C5-037 | Plan the cloud infrastructure for deploying this service, including networking and autoscaling. | cloud-infra |  | clear | ok | |
| C-C5-038 | Set up the VPC and load balancer for the app on AWS. | cloud-infra |  | clear | ok | |
| C-C5-039 | Review this diff for bugs before I merge it. | code-review | code-standards | boundary | ok | |
| C-C5-040 | Give me feedback on the quality of this pull request. | code-review | code-standards | boundary | ok | |

## C6

Installed skills:

- **using-mozg-pipelines** (DoctorMozg/claude-pipelines): ALWAYS invoke when user asks which mozg skill/plugin to use, says 'what plugins do I have', 'which pipeline fits', 'route this'. Maps task phrases to skills across mz-dev-base, mz-dev-pipe, mz-dev-git, mz-research-pipe, mz-memory, mz-biz-outreach, mz-job-outreach, mz-creative, mz-gov.
- **vault-answer** (DoctorMozg/claude-pipelines): ALWAYS invoke when asking a question that should be answered from vault notes with inline wikilink citations. Triggers: what does my vault say about, answer from notes, search my vault for, grounded answer.
- **vault-connect** (DoctorMozg/claude-pipelines): ALWAYS invoke when finding missing wikilinks for a note, suggesting connections between notes, discovering which vault notes should link to the current note, or improving a note's link density. Triggers: link notes, suggest wikilinks, find connections, improve link density.
- **init-rules** (DoctorMozg/claude-pipelines): ALWAYS invoke when the user wants to install development rules for a project or globally. Triggers:"init rules","set up rules","install rules","configure coding rules","onboard project".

| ID | Request | Gold | Also acceptable | Tier | Lint | Your verdict |
|---|---|---|---|---|---|---|
| C-C6-041 | Which of my installed plugins fits a task like drafting outreach emails to candidates? | using-mozg-pipelines |  | clear | ok | |
| C-C6-042 | Tell me which pipeline suits this task. | using-mozg-pipelines |  | boundary | ok | |
| C-C6-043 | What do my notes say about the Q3 pricing decision? Cite the notes you use. | vault-answer |  | clear | ok | |
| C-C6-044 | Answer from my vault: when did we decide to move to Postgres? | vault-answer |  | boundary | ok | |
| C-C6-045 | Which of my other notes ought to point to this one? | vault-connect |  | clear | ok | |
| C-C6-046 | This note feels isolated. Suggest connections to my other notes. | vault-connect |  | clear | ok | |
| C-C6-047 | Install our development rules for this project. | init-rules |  | clear | ok | |
| C-C6-048 | Onboard this repo with the coding rules, and set them up globally if possible. | init-rules |  | boundary | ok | |
