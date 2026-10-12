# System Design Learning List

Goal: senior engineer level — koi bhi system khud design kar sako (HLD + LLD), strong AI/ML/LLM focus.

Tags: 🟢 Deep (khud design + trade-off) · 🟡 Working (kab use karna pata ho) · ⚪ Awareness (naam + kaunsi problem solve karta hai)
Markers: 🆕 = discussion mein joda · 🔍 = research gap-check (Claude + Codex, 12 Oct 2026) se joda/badla
Resources har section ke liye: [RESOURCES.md](RESOURCES.md)

## 1. Networking & Communication

| Topic | Tag |
|---|---|
| REST / gRPC / GraphQL / WebSockets / SSE: kab kya use karna | 🟢 |
| 🔍 Polling vs long-polling vs webhooks; push vs pull | 🟢 |
| 🔍 Load balancer: L4 vs L7, algorithms (round-robin, least-conn, hash), LB vs reverse proxy vs API gateway | 🟢 |
| API design: versioning, idempotency, pagination, errors | 🟢 |
| Rate limiting: token bucket, sliding window, leaky bucket | 🟢 |
| TCP/IP basics | 🟡 |
| HTTP/1.1 vs 2 vs 3 | 🟡 |
| DNS resolution flow | 🟡 |
| Backpressure | 🟡 |
| 🔍 Real-time media transport: UDP vs TCP (head-of-line blocking), WebRTC basics (ICE/STUN/TURN, RTP/SRTP, Opus, jitter buffer), topology: P2P mesh vs SFU vs MCU | 🟡 |
| 🔍 Encoding & schema evolution: Protobuf/Avro, backward/forward compatibility | 🟡 |
| TLS handshake | ⚪ |

## 2. Databases & Storage

| Topic | Tag |
|---|---|
| SQL vs NoSQL: kab kya use karna (🔍 NoSQL types: KV, document, wide-column, graph) | 🟢 |
| Indexing: B-tree, hash, composite, covering | 🟢 |
| Replication: primary-replica, read replicas | 🟢 |
| Sharding: range, hash, hotspot problem | 🟢 |
| CAP theorem, practical matlab | 🟢 |
| Data modeling: read-heavy vs write-heavy (🔍 + normalization vs denormalization) | 🟢 |
| 🔍 Consistency models: linearizability, eventual, read-your-writes — kis operation ko kaunsi chahiye (🟡 → 🟢) | 🟢 |
| ACID + isolation levels | 🟡 |
| 🔍 Multi-leader & leaderless replication (quorum read/write), PACELC | 🟡 |
| LSM tree vs B-tree | 🟡 |
| Redis, DynamoDB, etcd | 🟡 |
| Event sourcing & CQRS | 🟡 |
| Cassandra, CockroachDB, Spanner internals | ⚪ |

## 3. Caching

| Topic | Tag |
|---|---|
| Cache strategies: cache-aside, write-through, write-behind | 🟢 |
| Invalidation: TTL, event-driven, version-based | 🟢 |
| Cache stampede / thundering herd | 🟢 |
| Consistent hashing | 🟢 |
| In-memory vs distributed cache | 🟡 |
| CDN | 🟡 |
| Eviction: LRU, LFU (LRU cache code karna → LLD section) | 🟡 |

## 4. Message Queues & Async Processing

| Topic | Tag |
|---|---|
| Kafka vs RabbitMQ vs SQS: kab kya use karna | 🟢 |
| Delivery guarantees: at-most / at-least / exactly-once | 🟢 |
| Partitioning, ordering, consumer groups | 🟢 |
| 🔍 Stream processing: windowing, event-time, watermarks (Flink, Spark Streaming) (⚪ → 🟡) | 🟡 |
| Pub/Sub pattern | 🟡 |
| Dead letter queue, replay | 🟡 |
| Outbox pattern | 🟡 |
| 🆕 CDC (change data capture) | 🟡 |

## 5. Distributed Systems Core

| Topic | Tag |
|---|---|
| Idempotency | 🟢 |
| 🔍 Timeouts | 🟢 |
| Retries: exponential backoff + jitter | 🟢 |
| Circuit breaker, bulkhead, fallback | 🟢 |
| Graceful degradation, blast radius | 🟢 |
| Saga pattern | 🟢 |
| 🔍 Load shedding, cascading failure | 🟡 |
| 🔍 Distributed lock / lease (Redis, ZooKeeper) + fencing token | 🟡 |
| 🔍 Unique ID generation: Snowflake, UUID trade-offs | 🟡 |
| 2PC (two-phase commit) | 🟡 |
| Leader election, quorum, split-brain | 🟡 |
| Raft (high-level flow) | 🟡 |
| Heartbeat failure detection | 🟡 |
| Paxos | ⚪ |
| Logical / vector clocks | ⚪ |
| Gossip protocol | ⚪ |
| Phi accrual, TCC | ⚪ |

## 6. Architecture Patterns

| Topic | Tag |
|---|---|
| Monolith vs modular monolith vs microservices: asli trade-offs (🔍 modular monolith isi row mein merge) | 🟢 |
| Event-driven architecture | 🟢 |
| Multi-tenant isolation: row / schema / DB level | 🟢 |
| 🔍 Workflow engine / durable execution (Temporal, Step Functions) | 🟡 |
| API Gateway vs Service Mesh | 🟡 |
| Service discovery | 🟡 |
| Serverless (Lambda) | 🟡 |
| DDD basics: bounded contexts | 🟡 |

## 7. Reliability & Operations

| Topic | Tag |
|---|---|
| Back-of-envelope estimation: QPS, storage, bandwidth (🔍 + latency numbers to know) | 🟢 |
| Observability: metrics, logs, distributed tracing (🔍 + voice: per-turn latency waterfall, P95 not average, call quality: jitter / packet loss / MOS) | 🟢 |
| Redundancy, failover, DR (RTO/RPO) | 🟢 |
| 🆕 Deploy strategies: rolling, blue-green, canary, feature flags | 🟢 |
| 🔍 SLO / SLI / error budget (🟡 → 🟢) | 🟢 |
| Multi-AZ, multi-region | 🟡 |
| Alerting: signal vs noise | 🟡 |
| Load testing, capacity planning | 🟡 |
| 🆕 Zero-downtime DB schema change | 🟡 |
| Chaos engineering | ⚪ |
| 🔍 Incident response + postmortem | ⚪ |

## 8. Security

| Topic | Tag |
|---|---|
| Authentication: OAuth 2.0, JWT | 🟢 |
| 🔍 Authorization: RBAC, ABAC (🟡 → 🟢) | 🟢 |
| Encryption: at rest, in transit | 🟡 |
| Secrets management | 🟡 |
| Input validation: SQL injection, XSS | 🟡 |
| API security: API keys, IP allowlisting | 🟡 |
| Threat modeling (STRIDE) | ⚪ |
| SAML | ⚪ |

(AI security — prompt injection, agent permissions — Section 11B mein)

## 9. Cloud & Infrastructure

| Topic | Tag |
|---|---|
| Horizontal vs vertical scaling, auto-scaling (🔍 + stateful vs stateless services) | 🟢 |
| 🔍 Docker (🟢 → 🟡: roz use alag baat, design depth 🟡 kaafi) | 🟡 |
| Kubernetes: pods, services, ingress, HPA | 🟡 |
| AWS core: EC2, S3, RDS, Lambda, EKS, CloudFront | 🟡 |
| CI/CD pipelines | 🟡 |
| Cost awareness: spot instances, data tiering, right-sizing | 🟡 |
| Infrastructure as Code (Terraform) | ⚪ |
| IaaS / PaaS / SaaS | ⚪ |
| Predictive auto-scaling | ⚪ |

## 10. Performance Engineering

| Topic | Tag |
|---|---|
| Latency vs throughput | 🟢 |
| p50 / p95 / p99: tail latency | 🟢 |
| DB query optimization: EXPLAIN, N+1 problem | 🟢 |
| Batch vs real-time processing | 🟢 |
| 🆕 OS basics: process vs thread, blocking vs async I/O, event loop | 🟡 |
| Connection pooling, keep-alive | 🟡 |
| Profiling: CPU, memory, I/O | 🟡 |
| Compression: gzip, brotli, snappy | ⚪ |
| Zero-copy, memory-mapped files | ⚪ |

## 11A. ML System Design

| Topic | Tag |
|---|---|
| 🆕 ML design framework: problem → data → features → model → serving → monitoring | 🟢 |
| 🔍 ML evaluation metrics: offline (precision/recall, AUC, NDCG) vs online (CTR, business metric) | 🟢 |
| 🔍 Training data quality: labels, label delay, class imbalance, data leakage | 🟢 |
| Model serving: batch vs real-time inference | 🟢 |
| 🆕 Training-serving skew | 🟢 |
| A/B testing, canary for models | 🟢 |
| Drift detection | 🟢 |
| 🔍 Feedback loop / data flywheel / continual learning (LLM apps pe bhi lagta hai) | 🟡 |
| 🔍 Feature engineering basics, embeddings / two-tower | 🟡 |
| Model registry | 🟡 |
| Feature stores (Feast) | 🟡 |
| Data pipelines: batch (Spark) vs streaming (Kafka + Flink) | 🟡 |
| 🆕 Recommendation: candidate generation + ranking | 🟡 |
| 🔍 Distributed training: data / model / pipeline parallelism (🟡 → ⚪, LLM-app role ke liye) | ⚪ |
| Gradient sync: AllReduce | ⚪ |
| GPU cluster scheduling | ⚪ |

## 11B. LLM / AI System Design

| Topic | Tag |
|---|---|
| RAG pipeline: chunking, embedding, vector DB (🔍 + ingestion/parsing, metadata, update/delete/re-index, freshness) | 🟢 |
| 🔍 Permission-aware retrieval: har user ko sirf uske documents (ACL), multi-tenant RAG | 🟢 |
| 🆕 Hybrid search (keyword + vector) + reranking | 🟢 |
| 🔍 Prompting vs RAG vs fine-tuning/distillation: kab kya chunna | 🟢 |
| 🔍 Context engineering: context window management, truncation/summarization, long-session token budget | 🟢 |
| Agent orchestration: tool calling, state, error recovery (🔍 + workflow patterns: chaining, routing, orchestrator-workers; structured outputs) | 🟢 |
| 🔍 Agent action authorization: least privilege, human approval, sandbox | 🟢 |
| 🔍 Model selection: API vs self-hosted (build vs buy), model cascades | 🟢 |
| 🆕 LLM gateway: model routing, fallback, token budgets (🔍 + request queue, per-user fairness) | 🟢 |
| 🆕 Eval pipelines: offline / online, LLM-as-judge (🔍 + agent evals: tool traces, task success, side effects) | 🟢 |
| 🆕 Guardrails + AI security: prompt injection (🔍 + PII / system-prompt leakage, unbounded consumption — OWASP LLM Top 10) | 🟢 |
| 🔍 LLM caching: prompt cache, semantic cache (🟡 → 🟢) | 🟢 |
| 🔍 Token streaming: cancel, reconnect (🟡 → 🟢) | 🟢 |
| 🔍 LLM observability: tracing, token/cost tracking (🟡 → 🟢) | 🟢 |
| 🔍 LLM inference trade-offs: TTFT/TPOT, prefill vs decode, KV-cache, continuous batching, quantization (🟡 → 🟢) | 🟢 |
| 🆕 Agent memory: short-term, long-term | 🟡 |
| 🆕 Prompt versioning | 🟡 |
| Vector DB internals: HNSW, ANN | 🟡 |
| Inference tools: vLLM, speculative decoding | 🟡 |
| 🔍 Multimodal ingestion: image / video / document input pipeline | 🟡 |
| 🔍 MCP (Model Context Protocol) | ⚪ |
| 🔍 LoRA / PEFT internals | ⚪ |
| TensorRT-LLM | ⚪ |
| **— Voice AI —** | |
| 🔍 Voice agent architecture: cascaded STT→LLM→TTS vs speech-to-speech (realtime) vs full-duplex + backend delegation — kab kya chunna | 🟢 |
| 🔍 Voice latency budget: mouth-to-ear vs platform turn gap, per-stage budget (endpointing, STT, LLM TTFT, TTS TTFB, network + jitter buffer), P50/P95 measure karna | 🟢 |
| 🔍 Streaming har stage pe: STT partials, sentence aggregation → TTS, preemptive generation, slow tool se pehle filler / acknowledgement | 🟢 |
| 🔍 Turn-taking: VAD → endpointing delay → audio/semantic turn detector (ya STT-native endpointing); fast reply vs user ko kaatna trade-off | 🟢 |
| 🔍 Interruption (barge-in): cancellable pipeline, TTS/playout buffer flush, backchannel vs asli interruption, context ko "user ne jo suna" tak truncate karna | 🟢 |
| 🔍 Voice transport choice: WebRTC vs WebSocket vs SIP/PSTN; edge routing, media server (SFU), agent ko user ke paas rakhna | 🟢 |
| 🔍 Telephony call flow: SIP trunk → dispatch rule → room/agent, DTMF/IVR, cold vs warm transfer, outbound + AMD (voicemail detection), recording | 🟢 |
| 🔍 Voice agent scaling: long-lived stateful sessions, worker pool + job dispatch, load-based admission, prewarm idle pool, deploy pe long drain, per-call process isolation, serverless kyun nahi; per-minute cost model | 🟢 |
| 🔍 Voice evals + observability: per-turn latency waterfall, WER vs task / field accuracy, barge-in recovery, simulated callers (text vs audio mode), failed calls → regression set | 🟢 |
| 🔍 Inference placement: STT / TTS / orchestrator ko media edge ke paas colocate, regional APIs, self-host GPU vs API, STT+TTS co-host risk | 🟡 |
| 🔍 Voice failure handling: STT/LLM/TTS provider fallback, mid-call crash → re-dispatch, reconnect, dead air / timeout | 🟡 |
| 🔍 Audio basics: PCM, sample rate (8k phone / 16k STT / 24-48k TTS), codec, resampling, echo cancellation, noise suppression | 🟡 |
| 🔍 Multilingual + code-switching (Hinglish): STT/TTS choice, mid-call language switch, names / numbers accuracy | 🟡 |
| 🔍 Voice frameworks + vendor internals: LiveKit Agents, Pipecat, Vapi / Retell / Bland / Bolna; speech-to-speech model internals | ⚪ |

## 12. Design Process (week 1 se saath-saath chalega, last mein nahi)

| Topic | Tag |
|---|---|
| 🆕 Standard flow: requirements → estimation → API → data model → boxes → deep-dive → bottlenecks | 🟢 |
| Requirements clarify karna: functional + non-functional | 🟢 |
| Trade-off reasoning: "X liya, Y nahi, kyunki Z" | 🟢 |
| Bottleneck jaldi pehchanna | 🟢 |
| Failure thinking: kya toota to kya hoga | 🟢 |
| Next 10x ke liye design | 🟡 |
| YAGNI: bina zaroorat complexity mat daalo | 🟡 |
| Design doc / RFC likhna: choices + trade-offs saaf likhna (🟡 → 🟢, assignment-style kaam ka core) | 🟢 |

(Back-of-envelope estimation → Section 7. Senior level pe kya expect hota hai → [NOTES.md](NOTES.md))

## 13. 🆕 Special Storage & Data Structures

| Topic | Tag |
|---|---|
| 🔍 Geo indexing: geohash (🟡 → 🟢, Uber/Yelp ke bina nahi banta) | 🟢 |
| 🔍 Quadtree (geohash se alag kiya) | 🟡 |
| Object / blob storage (S3): chunked upload, metadata alag (🔍 + presigned URLs, multipart upload) | 🟡 |
| Search: inverted index, Elasticsearch | 🟡 |
| OLTP vs OLAP, data warehouse, columnar storage (Parquet) | 🟡 |
| Bloom filter | 🟡 |
| Trie | 🟡 |
| 🔍 Time-series DB: Prometheus, InfluxDB (⚪ → 🟡) | 🟡 |
| HyperLogLog, Count-min sketch | ⚪ |
| Merkle tree | ⚪ |
| 🔍 CRDT / OT (collaborative editing) | ⚪ |

## 14. 🆕 LLD (Low-Level Design)

### 14A. OOP, Principles, Design Patterns

| Topic | Tag |
|---|---|
| OOP: encapsulation, abstraction, inheritance, polymorphism | 🟢 |
| SOLID principles | 🟢 |
| Composition over inheritance, interfaces pe code likhna | 🟢 |
| Strategy, Observer, State patterns | 🟢 |
| Factory pattern | 🟢 |
| Builder, Singleton | 🟡 |
| Adapter, Decorator, Facade | 🟡 |
| Command, Chain of Responsibility | 🟡 |
| 🔍 Template Method, Proxy, Iterator, Composite (⚪ → 🟡) | 🟡 |
| DRY, KISS | 🟡 |
| Baaki GoF patterns (Visitor, Flyweight, Memento...) | ⚪ |

### 14B. LLD Process, Concurrency, Diagrams

| Topic | Tag |
|---|---|
| LLD flow: requirements → entities → relationships → classes → methods → patterns | 🟢 |
| Threads, race condition, locks / mutex | 🟢 |
| Deadlock: kaise banta hai, kaise bachein | 🟢 |
| Producer-consumer, thread-safe queue | 🟢 |
| Optimistic vs pessimistic locking | 🟢 |
| 🔍 Class diagram (UML) + relationships (association, aggregation, composition) + state machine diagram (🟢 → 🟡: notation 🟡, responsibilities LLD flow mein 🟢) | 🟡 |
| Sequence diagram | 🟡 |
| Atomic operations, CAS (compare-and-swap) | 🟡 |
| Semaphore, read-write lock, thread pool (🔍 + condition variable, livelock) | 🟡 |
| Python async/await, GIL | 🟡 |
| Clean code: naming, chhote functions, testable code | 🟡 |

## 15. Practice Problems (🟢 zaroor · 🟡 time ho to · ⚪ optional)

### 15A. HLD

| # | System | Tag |
|---|---|---|
| 1 | URL Shortener | 🟢 |
| 2 | Rate Limiter (distributed) | 🟢 |
| 3 | Chat / WhatsApp | 🟢 |
| 4 | News Feed | 🟢 |
| 5 | Notification System | 🟢 |
| 6 | 🆕 Ride-sharing (Uber) | 🟢 |
| 7 | 🆕 Ticket Booking (BookMyShow) | 🟢 |
| 8 | Payment System | 🟢 |
| 9 | File Storage (Dropbox) | 🟢 |
| 10 | 🆕 Video Streaming (YouTube) (🔍 🟡 → 🟢) | 🟢 |
| 11 | 🔍 Proximity Service / Yelp / Nearby Friends | 🟡 |
| 12 | 🔍 Metrics Monitoring & Alerting | 🟡 |
| 13 | 🔍 Top-K / Trending / Leaderboard | 🟡 |
| 14 | 🔍 Unique ID Generator | 🟡 |
| 15 | 🆕 Search Autocomplete | 🟡 |
| 16 | 🆕 Web Crawler | 🟡 |
| 17 | 🆕 Distributed Job Scheduler | 🟡 |
| 18 | Real-time Analytics / Ad Click Counter | 🟡 |
| 19 | Distributed Cache / Key-Value Store | 🟡 |
| 20 | Multi-tenant SaaS | 🟡 |
| 21 | 🆕 Google Docs (collaborative editing) (🔍 ⚪ → 🟡) | 🟡 |
| 22 | 🔍 Distributed Message Queue (Kafka jaisa) | ⚪ |
| 23 | 🔍 Flash Sale / Online Auction | ⚪ |
| 24 | 🔍 Instagram / Twitter | ⚪ |
| 25 | 🔍 S3-like Object Storage | ⚪ |
| 26 | 🔍 Online Judge (LeetCode) | ⚪ |

### 15B. 🆕 LLD (code likh ke karne hain)

| # | Problem | Tag |
|---|---|---|
| 1 | Parking Lot | 🟢 |
| 2 | LRU Cache | 🟢 |
| 3 | Elevator System | 🟢 |
| 4 | BookMyShow (LLD) | 🟢 |
| 5 | Splitwise | 🟢 |
| 6 | Rate Limiter (class, thread-safe) | 🟢 |
| 7 | 🔍 Thread-safe TTL Cache | 🟡 |
| 8 | 🔍 File System / Unix File Search | 🟡 |
| 9 | 🔍 ATM | 🟡 |
| 10 | 🔍 Amazon Locker / Shipping Locker | 🟡 |
| 11 | Vending Machine | 🟡 |
| 12 | Logging Framework | 🟡 |
| 13 | In-memory Pub/Sub | 🟡 |
| 14 | Bounded Blocking Queue | 🟡 |
| 15 | Tic-tac-toe / Snake & Ladder (ek kaafi) | 🟡 |
| 16 | Hotel / Library Management | 🟡 |
| 17 | Text Editor with Undo | ⚪ |
| 18 | Chess | ⚪ |
| 19 | 🔍 Inventory / Grocery Store, Restaurant Management | ⚪ |
| 20 | 🔍 Car Rental / Task Management / Digital Wallet | ⚪ |

### 15C. 🆕 AI / LLM / ML

| # | System | Tag |
|---|---|---|
| 1 | Recommendation Engine (Netflix/YouTube) | 🟢 |
| 2 | Real-time Fraud Detection | 🟢 |
| 3 | Search / Feed Ranking | 🟡 |
| 4 | Ad Click Prediction | 🟡 |
| 5 | Distributed Training Platform | ⚪ |
| 6 | 🔍 Similar Items / Visual Search | ⚪ |
| 7 | 🔍 People You May Know / Bot Detection | ⚪ |
| 8 | LLM Chat Platform (ChatGPT jaisa) | 🟢 |
| 9 | RAG Document Q&A / Enterprise Knowledge Agent (🔍 + per-user ACL, update/delete, freshness) | 🟢 |
| 10 | AI Agent Platform | 🟢 |
| 11 | LLM Gateway | 🟢 |
| 12 | LLM Eval System (🔍 + agent-run evals) | 🟢 |
| 13 | Mini Agent Framework (LLD, code mein) | 🟡 |
| 14 | 🔍 Domain Assistant: prompt vs RAG vs fine-tune choose karo + eval se prove karo | 🟡 |
| 15 | 🔍 Real-time Voice Agent (web + phone; P95 first-audio target, turn detection, barge-in, tool filler; deep-dive: multi-region placement) (🟡 → 🟢) | 🟢 |
| 16 | Customer Support AI Bot | 🟡 |
| 17 | Self-hosted LLM Serving (vLLM) | 🟡 |
| 18 | Content Moderation at Scale | 🟡 |
| 19 | Code Assistant / Smart Compose (🔍 ⚪ → 🟡) | 🟡 |
| 20 | 🔍 Multimodal Video Understanding Pipeline | ⚪ |
| 21 | 🔍 Telephony Call-Center Voice Agent: SIP inbound, IVR/DTMF, warm transfer to human, recording + PII redaction | 🟢 |
| 22 | 🔍 Voice Agent Eval / Benchmark Harness: simulated callers (text + audio), latency waterfall, regression set | 🟢 |
| 23 | 🔍 Outbound Voice Calling at Scale: campaign dialer, concurrency / carrier limits, AMD, retry ladder, consent / DND compliance | 🟡 |

## Order (LOCKED 12 Oct 2026) — dependency ke hisaab se

### Schedule (Option A: saath-saath, 2 track)
- Mon–Sat (2-3 hr): HLD topics (lesson → source → recall → practice)
- Sunday (7-8 hr): LLD — 1 problem poora code mein
- Phase poora hone wale Sunday: pehle LLD (~4-5 hr), phir 1 HLD design doc (~2-3 hr) — timer nahi, doc likh ke (English)

### Weekday track (HLD) — har phase agle ki neev
- **P0** Design Process (12) + back-of-envelope estimation (7) — week 1 se, har phase ke saath chalta rahega
- **P1** OS basics (10 ka hissa) → Networking (1) — request ka safar
- **P2** Databases (2) → Caching (3) — data kahan rahega, tez kaise mile
- **P3** Queues (4) → Distributed Core (5) — kai machines, async, failure
- **P4** Architecture (6) → Cloud (9) → Reliability (7) → Security (8) → Performance (10, baaki) → Special Storage (13)
- **P5** ML System Design (11A)
- **P6** LLM/AI (11B) → Voice AI (11B voice block)

AI last kyun: LLM gateway = LB + rate limit + cache; RAG = DB + search; voice agent = networking + scaling + failure handling. Neeche ke phase pakke → P6 tez.

### Sunday track (LLD)
14A: OOP → SOLID → patterns → 14B: LLD flow + concurrency → 15B problems order mein (Parking Lot → LRU → Elevator → ...). Concurrency tak P1 ke OS basics ho chuke honge.

### Design doc milestones (phase ke baad)
- P2 → URL Shortener
- P3 → Rate Limiter, Chat
- P4 → News Feed, Ticket Booking, Payment, Uber, YouTube (baaki 15A 🟢 bhi)
- P5 → Recommendation, Fraud Detection
- P6 → AI + voice problems (15C 🟢)
