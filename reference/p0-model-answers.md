# P0 Model Question Answers

These are all the P0 model answers (design process + estimation) in Q/A format. They are kept in one place for writing notes in a notebook and for practice. They were made during the "hard mode" revision (20–22 Oct 2026): for each question, Aditya answered first, and then we wrote the improved version here.
The examples come from a voice-agent platform (clinics that use our voice agent). Example numbers are made up to explain the idea, unless a source is given.

Related: [design-doc-template.md](design-doc-template.md) · [quality-checklist.md](quality-checklist.md)

---

## 1. Design process

**Q: What are the 6 steps of a system design, in order?**
A: **Requirements → Estimation → Core entities → API → High-level design → Deep dives.**
Deep dives = pick the 1–2 riskiest parts and go deep (bottleneck, failure, scaling) — not a list of all edge cases.
*English:* "Finally, we pick the two riskiest parts of the design and do deep dives on them."

**Q: Why does estimation come after requirements?**
A: **Requirements decide which numbers matter.** We only estimate numbers that can change a design decision.
*Example:* we estimate storage only if we must record calls.

## 2. Requirements

**Q: What is a functional requirement (FR)?**
A: **A functional requirement says what an actor (a user, or another system) should be able to do.** Pattern: *"[Actor] should be able to [action]."*
*Example:* "A clinic should be able to view past calls with their evaluation scores."
*Watch out:* write what the actor can do, not what we will build ("build a dashboard" is a solution, not an FR).

**Q: What is a non-functional requirement (NFR)?**
A: **A non-functional requirement says how well the system must do its job — for example, how fast, reliable, secure or cheap to run it is. We write it with a number, so we can check whether we met it.**
*Example:* "The call history page should load in under 2 seconds, even for a clinic that has 10,000 past calls."
*Hook:* Functional = **WHAT**. Non-functional = **HOW WELL**.

**Q: What are the 4 parts of a good NFR?**
A: **Quality · Scope · Number · Condition.** Every good NFR has all four; if one is missing, we can't check it.

| Part | Meaning | Question to find it |
|---|---|---|
| Quality | The kind of "how well" we care about: speed, reliability, security… | *How well, in what way?* |
| Scope | The task or part of the system it applies to — usually one FR | *For which part or task?* |
| Number | The target that decides pass or fail (a number, or a rule we can test) | *How much, exactly?* |
| Condition | The hardest situation where the system must still meet the target | *Even when what happens?* |

Examples:
1. "The call history page should load in **under 2 seconds**, even for a clinic with **10,000 past calls**." → speed · call history page · under 2 s · 10,000 past calls
2. "The agent should answer **99.9%** of incoming calls **during clinic hours (9 AM–9 PM)**." → availability · answering calls · 99.9% · clinic hours
3. "Only staff of the **clinic that owns the recording** can play it — **even if someone shares the direct link**." → security · playing recordings · same-clinic rule · shared link

*Trick:* add "even when…" / "even if…" — what follows is the condition.

**Q: A clinic says: "The agent said 'booked', but the booking is not on the dashboard." Which quality is broken?**
A: **Reliability** — the system must never say "done" for something that did not happen. This is a "Wrong" failure (see §5).

**Q: Write the NFR for that complaint.**
A: **"Every booking the agent confirms must appear on the clinic dashboard within 5 seconds — even when 100 booking calls happen at the same time."**
→ reliability · saving a confirmed booking · 100% (every), within 5 s · 100 calls at once
*Rule:* **The more one mistake costs, the stricter the number.**

**Q: How do we tell an FR from an NFR?**
A: **Break test: if this requirement fails, does the feature *stop working* (FR) or *work badly* (NFR)?**
*Example:* no booking at all → FR broken; booking shows up late → NFR broken.
*Hook:* **"Stops or gets worse?"**

**Q: What are the 3 requirement buckets?**
A: **Core (in scope) · Later (future) · Out of scope.**
*English:* "For v1, call booking is core. SMS reminders come later. Payments are out of scope."

**Q: Why write "out of scope" down explicitly?**
A: **It stops scope creep, and shows others it was a decision, not something we forgot.**
*English:* "Payments are out of scope for v1 — we chose that on purpose."

## 3. Trade-offs

**Q: What is the basic trade-off sentence?**
A: **"We chose X over Y because Z. The downside of X is W. We handle it with M."**
*Example:* "We chose streaming STT over batch STT because the agent must start replying while the caller is still speaking. The downside is higher cost per minute. We handle it by using batch STT for post-call transcripts."

**Q: What makes the "because" strong?**
A: **Evidence means numbers we measured ourselves that prove our "because".** Without it, a trade-off is just an opinion.
*English:* "We measured it: batch STT added about 1.5 seconds per reply." (example number)

**Q: What is a revisit trigger?**
A: **A clear condition that tells us when to reopen this decision.** Set it *before* we hit the limit.
*Example:* "We'll revisit if STT cost goes above ₹50,000 a month, or if a batch model takes less than 300 ms."

**Q: What is the full trade-off format?**
A: 1. **X over Y** — what we chose, what we didn't · 2. **Because Z + evidence** · 3. **Downside W** · 4. **Mitigation M** · 5. **Revisit trigger**
*Hook (suggestion):* **"Choice, Cause, Cost, Cover, Comeback"**

## 4. Bottlenecks

**Q: What is a bottleneck?**
A: **A bottleneck is the slowest or smallest part of a system — it limits the speed or capacity of the whole system.** Fix it, and the next bottleneck shows up.
*Example:* "In our voice pipeline, the LLM is the bottleneck — it takes most of the reply time."

**Q: Bottleneck vs single point of failure (SPOF)?**
A: **Bottleneck: the system still works, but this part limits its speed or capacity. SPOF: this part has no backup — if it fails, the whole system stops.**
*Hook:* bottleneck = **slow**, SPOF = **stop**. One part can be both (a single LLM provider).

**Q: How do we find bottlenecks at design time?**
A: **Slowest, Smallest, Single.**
1. Follow the request from start to end — which step takes the most time? (latency)
2. Check each part's capacity. Which part has the lowest capacity? (capacity)
3. Look for parts that have only one copy. (SPOF + limit)

**Q: STT handles 500 streams, LLM 100 requests, TTS 300 streams. Which is the capacity bottleneck?**
A: **The system's capacity = the capacity of its smallest part.** LLM (100) < TTS (300) < STT (500) → **LLM.**
*Note:* 100 LLM slots ≠ 100 calls — a call uses the LLM only while the agent prepares its reply.

**Q: The LLM limit goes from 100 to 400. Now what?**
A: **Fixing one bottleneck shows the next one** — now TTS (300). We keep measuring; we don't fix it once and forget.

## 5. Failure thinking

**Q: What are the 3 ways a part can fail?**
A: **Down, Slow, Wrong.** Down = no response · Slow = response comes too late · Wrong = response looks fine but has a mistake in it.

**Q: Which is the most dangerous, and why?**
A: **Wrong — Down and Slow are loud (easy to notice); Wrong is silent (nobody notices).** No alert fires, so we add our own checks: read the details back to the caller, check the DB before saying "done", run evals.

**Q: What is blast radius?**
A: **How much of the system (and how many users) one failure affects.**
*English:* "If the TTS provider goes down, the blast radius is every live call."

**Q: 20 clinics share one LLM API key. One clinic gets a spike and hits the rate limit. Blast radius?**
A: **All 20 clinics.** When everyone shares one resource, a sudden traffic spike from one user can stop service for everyone — the **"noisy neighbour"** problem.

**Q: How do we shrink that blast radius?**
A: **Isolate: give each tenant (each clinic) its own limit (separate keys or per-clinic quotas).** This is called a **bulkhead**.
*Note:* fallback and retry help us recover — they don't shrink the blast radius.

**Q: What are the 3 questions of failure thinking?**
A: 1. **How can it fail?** — Down, Slow, Wrong · 2. **What is the blast radius?** · 3. **How do we detect it, and how do we respond?**

**Q: What are the 6 tools to respond to a failure, in order?**
A: 1. **Timeout** — decide it's stuck · 2. **Retry** — try again, with a limit · 3. **Fallback** — use a backup · 4. **Degrade** — keep running with fewer features · 5. **Save partial** — keep the data we already have · 6. **Fail safe** — end the call politely and alert the team
*Hook (suggestion):* **Wait → Again → Other → Less → Keep → Close**
*English:* "If the LLM call gets stuck, we time out and retry once. Then we fall back to a second provider. If that also fails, we degrade to a fixed script that just takes a message."

## 6. 10x and YAGNI

**Q: What is the 10x rule?**
A: **Today's design should handle 10x the current load with small changes. At 100x, plan to redesign.** (Jeff Dean's rule of thumb)
*Example:* 50 → 500 calls at once: more workers, higher limits. 50 → 5,000: new architecture.

**Q: What is YAGNI, and how do we decide what to build now?**
A: **YAGNI = "You Aren't Gonna Need It" — don't build what you don't need yet. Test: "If we don't build it now, how expensive is it to add later?"** Cheap later → skip it for now. Expensive later → build a cheap door now (a small, low-cost step), and the big building later.
*Example:* an LLM wrapper is a cheap door: 1 hour of work, and later changes become easy. Multi-provider routing is the big building.

**Q: With only one clinic today, should every call row have a `clinic_id`?**
A: **Yes. It's one column now. Later it means a full data migration, and one clinic could see another clinic's calls.** YAGNI doesn't mean "build nothing".

## 7. Estimation

**Q: Peak load or average load — which do we design for?**
A: **Peak — a system built for the average fails exactly at the busiest time.**
*Example:* average 10 calls/hour, Monday 10–11 AM brings 60. Design for 60.

**Q: How much storage does a 5-minute phone call (G.711, 64 kbps) need?**
A: **bitrate × seconds ÷ 8 = bytes.** 64 kbps × 300 s = 19,200 kb → ÷ 8 = 2,400 KB → ÷ 1,000 = **2.4 MB**.
*Rule:* small **b** = bits, big **B** = bytes. Bits → bytes: **divide** by 8.

**Q: Roughly how much storage does 1 minute of 128 kbps audio take?**
A: **About 1 MB per minute.** 128 ÷ 8 = 16 KB/s → × 60 = 960 KB ≈ 1 MB. (Divide by 8 first; the numbers stay smaller.)

**Q: What is sample rate?**
A: **How many times per second we measure the sound.** All digital audio has a sample rate. 8 kHz = 8,000 samples per second.

**Q: What is the Nyquist rule?**
A: **To catch a sound correctly, the sample rate must be at least twice the highest frequency in that sound.** So the highest frequency it can catch is **half** the sample rate.
Phone (G.711) 8 kHz → up to ~4 kHz. Browser (Opus, WebRTC) up to 48 kHz → up to ~20 kHz.

**Q: Why does a phone call sound worse than a browser call, and what does it mean for a voice agent?**
A: **High sounds like "s", "f", "sh" have frequencies above 4 kHz, so phone audio cuts them off.** "Fifteen" and "fifty" can sound the same → STT makes more mistakes on numbers and names → read important details back to the caller.
*Note:* sample rate (how often we measure) ≠ compression (how much we shrink the data).

**Q: What is Little's Law?**
A: **Items in a system = arrival rate × time each item stays.** **L = λ × W.**
Rules: units must match · works for any system · use peak λ for the busiest time · round up only the final answer.
*Examples:* 4 calls/min × 3 min = **12 calls at once**. 10 customers/hour × 0.5 hour = 5 inside. 150 QPS × 0.2 s = 30 requests running at once. 20 LLM req/s × 1.5 s = 30 LLM calls at once → compare with the provider's limit.

**Q: Is Little's Law the same as peak factor?**
A: **No.** Little's Law = how many are running **at once**. Peak factor = how much higher the load is at the busiest time than on average. First find peak arrivals, then apply Little's Law.

**Q: How do we calculate peak QPS?**
A: **QPS = requests per day ÷ 100,000 (1 lakh; 1 day = 86,400 s ≈ 100,000 s) × peak factor.**
*Example:* 5 million/day ÷ 100,000 = 50 QPS × 3 = **150 QPS peak**. (The shortcut gives a number about 15% too low. That's fine; we only need the rough size.)

**Q: When do we use Little's Law and when QPS?**
A: **For calls that last minutes, use Little's Law: how many are open at once. For API requests that take milliseconds, use QPS: how many arrive per second.**

**Q: How do we estimate bandwidth for voice calls?**
A: **Bitrate per stream × streams per call × calls at once**, then compare with the network bandwidth.
*Example:* 64 kbps × 2 × 500 = 64,000 kbps = **64 Mbps = 6.4% of 1 Gbps** → enough. Packet headers add a little extra, so keep some spare bandwidth (headroom).

**Q: In a multi-turn call, what drives LLM cost — input or output tokens?**
A: **Input. We resend the system prompt and the whole history on every turn, so input grows each turn while output stays small.** Fix: **prompt caching**.

**Q: How big is a token?**
A: **1 token ≈ 4 characters ≈ ¾ of a word.** Input and output have separate prices.

**Q: What are the latency numbers to know?**

| Operation | Time |
|---|---|
| Read from RAM | ~100 ns |
| Read 4 KB from SSD (random) | ~150 µs |
| Round trip inside one data center | ~0.5 ms |
| Round trip across the world (California ↔ Netherlands) | ~150 ms |

Units: ns → µs → ms → s, each ×1000. RAM ≈ 1,500× faster than SSD.

**Q: The agent server is in Europe and the LLM is in California. How much time does the distance add to each turn, and how do we fix it?**
A: **~150 ms per LLM round trip, every turn** (~450 ms if STT and TTS were in California too). **Fix: co-locate all pipeline parts in one region.**

## 8. Design doc (theory, 13 Oct — not in this quiz)

**Q: When should we write a design doc?**
A: **When the decision is hard to undo or affects many people — not because the system is big.**

**Q: Where does a good doc show its weak spots?**
A: **Three places: downsides (in trade-offs), failure modes, and open questions.**

**Q: How do we write an open question?**
A: **Question + owner + blocking or non-blocking + default (what we assume until answered) + recommendation.**

Full section list: [design-doc-template.md](design-doc-template.md).

---

**Next:** role-play (gathering requirements) → `designs/01-...md` → review → P0 done.
