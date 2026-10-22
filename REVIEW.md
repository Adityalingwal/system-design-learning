# Review list (spaced recall)

One line per fact. Quiz at the start of each session on items whose date has come. Correct → roughly double the gap (1 → 3 → 7 → 14 → 30 days). Miss → shorten it. Skills (designing, LLD code) are reviewed by doing, not here.

Har naye message pe (khaas kar gap ke baad) `date` check karo: jo items due hain unka quiz pehle, phir naya topic. Same din ke beech mein purana recall NAHI; sirf "Next review" date aane pe. Learned column mein date + time (IST).

| Item | Learned | Gap (days) | Next review |
|---|---|---|---|
| Design ke 6 steps, order mein: requirements → estimation → core entities → API → high-level design (boxes) → deep dives (1-2 riskiest parts, edge-case list nahi) | 2026-10-12 16:32 | 3 | 2026-10-25 |
| Functional requirement (FR) = actor kya kar sake ("X should be able to Y"), hum kya banayenge wo nahi; non-functional (NFR) = HOW WELL (how fast, reliable, secure, cost-effective) + number jo check ho sake | 2026-10-12 16:32 | 1 | 2026-10-23 |
| Achhe NFR ke 4 parts: Quality · Scope (task/FR) · Number (ya testable rule) · Condition (sabse mushkil situation, "even when…") | 2026-10-12 16:32 | 3 | 2026-10-25 |
| FR vs NFR break test: toote to feature ruk jaata hai (FR) ya bura chalta hai (NFR)? Hook: "Stops or gets worse?" | 2026-10-12 16:32 | 1 | 2026-10-23 |
| Requirements ke 3 buckets: core · later · out of scope; out of scope likhna = scope creep roko + dikhao ki faisla tha, bhool nahi | 2026-10-12 16:32 | 3 | 2026-10-25 |
| Estimation sirf tab, jab result se design decision badle (requirements batate hain kaunse numbers); design peak pe banta hai, average pe nahi | 2026-10-12 16:32 | 7 | 2026-10-29 |
| Trade-off 5 parts: X over Y · because Z + evidence (apne naape numbers) · downside W · mitigation M · revisit trigger (limit se pehle). English: "We chose X over Y because Z. The downside of X is W. We handle it with M." | 2026-10-12 16:32 | 1 | 2026-10-23 |
| Bottleneck = slowest/smallest hissa jo poore system ki speed/capacity limit kare; theek karo to agla saamne aata hai. SPOF alag: koi backup nahi, gira to sab ruka (bottleneck = slow, SPOF = stop) | 2026-10-12 21:58 | 1 | 2026-10-23 |
| Bottleneck design pe pakadne ka hook: Slowest (raasta chalo, har kadam ka time) · Smallest (sabse kam capacity) · Single (ek hi copy) | 2026-10-12 21:58 | 1 | 2026-10-23 |
| Failure thinking ke 3 sawaal: kaise tootega (Down / Slow / Wrong) → blast radius → detect + respond. Wrong sabse khatarnaak (chupchaap) | 2026-10-12 21:58 | 1 | 2026-10-23 |
| Failure ke 6 tools, order mein: timeout · retry (limit) · fallback · degrade · save partial · fail safe (+ alert). Hook: Wait → Again → Other → Less → Keep → Close | 2026-10-12 21:58 | 1 | 2026-10-23 |
| 10x rule: aaj ka design 10x tak chhote badlav se chale; 100x pe redesign maan ke chalo (Jeff Dean) | 2026-10-13 07:56 | 3 | 2026-10-25 |
| YAGNI test: "abhi nahi banaya to baad mein kitna mehenga?" Sasta baad mein → skip; mehenga → sasta darwaza abhi (jaise clinic_id column, LLM wrapper) | 2026-10-13 07:56 | 1 | 2026-10-23 |
| Storage formula: bitrate × seconds = bits → ÷ 8 (divide, multiply nahi) = bytes → ÷ 1000 = agla unit. kb = kilobits, KB = kilobytes | 2026-10-13 16:20 | 1 | 2026-10-23 |
| 128 kbps audio ≈ 1 MB per minute (128 ÷ 8 = 16 KB/s × 60 = 960 KB); LiveKit egress default: Opus, 44.1 kHz, 128 kbps | 2026-10-13 16:20 | 1 | 2026-10-23 |
| Phone call (Twilio SIP default G.711 = PCMU/PCMA): 8 kHz, 64 kbps. Browser (WebRTC): Opus, 48 kHz tak. Har digital audio ka sample rate hota hai | 2026-10-13 16:20 | 1 | 2026-10-23 |
| Little's Law: L = λ × W (ek saath kitne = aane ki rate × har ek kitni der rukta). Peak factor se alag. Units match karo; sirf aakhri answer upar round | 2026-10-13 16:20 | 1 | 2026-10-23 |
| QPS = requests per din ÷ 1 lakh (1 din ≈ 86,400 s) × peak guna. Calls (lambi) → Little's Law; requests (chhoti) → QPS | 2026-10-13 16:20 | 3 | 2026-10-25 |
| Bandwidth = ek stream ka bitrate × streams per session (voice: 2) × ek saath sessions; phir pipe (jaise 1 Gbps) se compare, headroom rakho | 2026-10-13 16:20 | 3 | 2026-10-25 |
| LLM cost: 1 token ≈ 4 characters ≈ ¾ shabd; input + output alag rate; har turn pe prompt + history dobara jaata hai → input cost driver; caching se sasta | 2026-10-13 16:20 | 3 | 2026-10-25 |
| Latency numbers: RAM 100 ns · SSD 4 KB 150 µs · same data center round trip 0.5 ms · aar-paar (CA↔NL) 150 ms. ns→µs→ms→s ×1000 | 2026-10-13 16:20 | 1 | 2026-10-23 |
| Blast radius = ek failure kitna system / kitne users ko maarta hai. Shared resource → noisy neighbour; chhota karne ka tareeka = isolation (per-tenant quota/keys) = bulkhead | 2026-10-22 23:21 | 1 | 2026-10-23 |
| NFR ka number: jitni mehengi ek galti, utna sakht number (confirmed booking → every / 100%) | 2026-10-22 23:21 | 1 | 2026-10-23 |
| Sample rate = ek second mein awaaz kitni baar naapi; Nyquist: sirf aadhi frequency tak pakdi jaati hai (8 kHz → ~4 kHz, s/f/sh kat jaate) → phone pe STT galtiyan, details read back karo | 2026-10-22 23:21 | 1 | 2026-10-23 |
| Distance latency fix: co-locate (STT, LLM, TTS ek region mein); doosre region ka LLM = ~150 ms per turn extra | 2026-10-22 23:21 | 1 | 2026-10-23 |
