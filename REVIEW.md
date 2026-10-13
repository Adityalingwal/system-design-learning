# Review list (spaced recall)

One line per fact. Quiz at the start of each session on items whose date has come. Correct → roughly double the gap (1 → 3 → 7 → 14 → 30 days). Miss → shorten it. Skills (designing, LLD code) are reviewed by doing, not here.

Har naye message pe (khaas kar gap ke baad) `date` check karo: jo items due hain unka quiz pehle, phir naya topic. Same din ke beech mein purana recall NAHI; sirf "Next review" date aane pe. Learned column mein date + time (IST).

| Item | Learned | Gap (days) | Next review |
|---|---|---|---|
| Design ke 6 steps, order mein: requirements → estimation → core entities → API → high-level design (boxes) → deep dives | 2026-10-12 16:32 | 1 | 2026-10-13 |
| Functional requirement (FR) = actor + kaam ("X should be able to Y"); non-functional (NFR) = wo kaam kitna achha ho | 2026-10-12 16:32 | 1 | 2026-10-13 |
| Achhe NFR ke 4 parts: quality · kaunsa hissa/kaam · number (ya check hone wala rule) · condition (load) | 2026-10-12 16:32 | 1 | 2026-10-13 |
| FR vs NFR test: kharab ho to system kaam band karta hai (FR) ya bura kaam karta hai (NFR)? | 2026-10-12 16:32 | 1 | 2026-10-13 |
| Requirements ke 3 buckets: core · baad mein · out of scope (out of scope khud bol ke likho) | 2026-10-12 16:32 | 1 | 2026-10-13 |
| Estimation sirf tab, jab result se design decision badle; design peak pe banta hai, average pe nahi | 2026-10-12 16:32 | 1 | 2026-10-13 |
| Trade-off ka format: "X liya, Y nahi, kyunki Z. X lene ki keemat: W" (W = X ke saath accept kiya nuksaan, aksar Y ke chhoote faayde). Poora: + saboot (apne naape numbers) + mitigation (W kaise sambhalenge) + revisit trigger (kab faisla dobara kholenge). English: "We chose X over Y because Z. The downside of X is W." (paisa ho to "cost") | 2026-10-12 16:32 | 1 | 2026-10-13 |
| Bottleneck = sabse tang hissa jo poore system ki limit tay karta hai; symptom 2 (latency / capacity), wajah kai; theek karo to agla saamne aata hai | 2026-10-12 21:58 | 1 | 2026-10-13 |
| Bottleneck design pe pakadne ke 3 sawaal: raasta chalo + har kadam ka time · har hisse ki capacity (sabse chhota) · akela kaun hai | 2026-10-12 21:58 | 1 | 2026-10-13 |
| Failure thinking ke 3 sawaal: kaise tootega (band / dheema / galat) → blast radius → pata kaise chalega, kya karenge | 2026-10-12 21:58 | 1 | 2026-10-13 |
| Failure ke 6 tools: timeout · retry (limit ke saath) · fallback · degrade · save partial · fail safe (+ alert) | 2026-10-12 21:58 | 1 | 2026-10-13 |
| 10x rule: aaj ka design 10x tak chhote badlav se chale; 100x pe redesign maan ke chalo (Jeff Dean) | 2026-10-13 07:56 | 1 | 2026-10-14 |
| YAGNI = jo abhi chahiye nahi, mat banao. Test: "abhi nahi banaya to baad mein kitna mehenga?" Sasta darwaza abhi, mehengi building baad mein; trigger limit se pehle | 2026-10-13 07:56 | 1 | 2026-10-14 |
| Storage formula: bitrate × seconds = bits → ÷ 8 = bytes → ÷ 1000 = agla unit. kbps = kilo-*bits* (chhota b), KB = kilo-*bytes* (bada B) | 2026-10-13 16:20 | 1 | 2026-10-14 |
| 128 kbps audio ≈ 1 MB per minute (LiveKit egress default: Opus, 44.1 kHz, 128 kbps) | 2026-10-13 16:20 | 1 | 2026-10-14 |
| Phone call (Twilio SIP default G.711 = PCMU/PCMA): 8 kHz, 64 kbps. Browser (WebRTC): Opus, 48 kHz tak | 2026-10-13 16:20 | 1 | 2026-10-14 |
| Little's Law: ek saath calls = calls per minute × call ki length (minute). Units match karo; sirf aakhri answer upar round | 2026-10-13 16:20 | 1 | 2026-10-14 |
| QPS = requests per din ÷ 1 lakh (1 din ≈ 86,400 s) × peak guna. Calls (lambi) → Little's Law; requests (chhoti) → QPS | 2026-10-13 16:20 | 1 | 2026-10-14 |
| Bandwidth = ek stream ka bitrate × streams per session (voice: 2) × ek saath sessions; phir pipe (jaise 1 Gbps) se compare | 2026-10-13 16:20 | 1 | 2026-10-14 |
| LLM cost: 1 token ≈ 4 characters ≈ ¾ shabd; input + output alag rate; har turn pe prompt + history dobara jaata hai → input cost driver; caching se sasta | 2026-10-13 16:20 | 1 | 2026-10-14 |
| Latency numbers: RAM 100 ns · SSD 4 KB 150 µs · same data center round trip 0.5 ms · aar-paar (CA↔NL) 150 ms. ns→µs→ms→s ×1000 | 2026-10-13 16:20 | 1 | 2026-10-14 |
