# P0 Notes — Design Process + Estimation

These are the full P0 notes. Each topic has a **plain explanation**, a **diagram**, **voice-agent examples**, **common mistakes**, and **how to say it in English**. Everything we learned in chat during the hard-mode revision (20–22 Oct 2026) is here in one place. This file alone is enough to understand the topic.
For Q/A practice only: [p0-model-answers.md](p0-model-answers.md). Example numbers are made up to explain the idea, unless a source is given.

**Example world:** we run a voice-agent platform. Clinics (our business customers) use our agent; a patient calls, the agent books an appointment, and the clinic sees its calls and bookings on its dashboard.

---

## 1. Design process — 6 steps

```
1. Requirements      → what to build, and how well
2. Estimation        → how much load, how much storage (only numbers that change the design)
3. Core entities     → the main things in the system (Call, Booking, Clinic…)
4. API               → how the outside world talks to the system
5. High-level design → boxes + arrows
6. Deep dives        → the 1–2 riskiest parts, in depth
```

- **Deep dives** do not mean a long list of edge cases. They mean: pick the **1–2 hardest / riskiest parts** of the design and go deep on them (bottleneck, failure, scaling). This is what interviewers expect at senior level.
- **Why does estimation come after requirements?** Because requirements tell us **which numbers matter**. If there is no recording requirement, estimating storage is wasted effort.

> **English:** "Finally, we pick the two riskiest parts of the design and do deep dives on them."
> **English:** "Requirements tell us which numbers matter. If there's no recording requirement, we don't estimate storage."

---

## 2. Requirements

### 2.1 Functional requirement (FR) = WHAT

An FR says **what an actor (a user, or another system) can do**. Pattern: *"[Actor] should be able to [action]."*

- ✅ "A clinic should be able to view past calls with their evaluation scores." → a capability (something the actor can do)
- ❌ "Task = build a dashboard" → this is **our solution**, not an FR. A dashboard is just one way to do it; tomorrow it could be an email report or a CSV. If we put the solution into the FR, we lose the other options.

### 2.2 Non-functional requirement (NFR) = HOW WELL

> **A non-functional requirement says how well the system must do its job — for example, how fast, reliable, secure or cheap to run it is. We write it with a number, so we can check whether we met it.**

- Speed, reliability, security and cost are only **examples** — not the full list (availability, scalability, privacy… → [quality-checklist.md](quality-checklist.md)).
- "Clean" or "how it looks" is not an NFR: we can't measure "clean", and the look is UI design.
- **Hook:** Functional = **WHAT**. Non-functional = **HOW WELL**. (Careful: don't make the mistake of writing "functional … how well".)

### 2.3 The 4 parts of a good NFR

**Every good NFR has all four; only the values change. If even one is missing, we can't check it.**

| Part | Meaning | Question to find it |
|---|---|---|
| **Quality** | the kind of "how well" we care about: speed, reliability, security… | *How well, in what way?* |
| **Scope** | which task / part of the system it applies to — often one FR | *For which part or task?* |
| **Number** | the target that decides pass/fail (a number, or a rule we can test) | *How much, exactly?* |
| **Condition** | **the hardest situation** where the system must still meet the target | *Even when what happens?* |

```
"The call history page should load in under 2 seconds, even for a clinic that has 10,000 past calls."
      └─ scope ─────────┘  └quality┘ └─ number ─┘  └──────── condition ────────────┘
                              (speed)
```

**The same structure across three qualities:**

| NFR | Quality | Scope | Number | Condition |
|---|---|---|---|---|
| Call history page should load in under 2 s, even for a clinic with 10,000 past calls | speed | call history page | under 2 s | 10,000 past calls |
| The agent should answer 99.9% of incoming calls during clinic hours (9 AM–9 PM) | availability | answering calls | 99.9% | clinic hours |
| Only staff of the clinic that owns the recording can play it — even if someone shares the direct link | security | playing recordings | same-clinic **rule** | shared link |

- **Security** often has no number; instead it has a **rule we can check**. That's why "Number" means whatever decides pass/fail.
- **Condition** = the hardest situation. For speed, it is load. For availability, it is a time window. For security, it is a tricky case. A condition like "every request" is weak (it only says "always").
- **Trick:** add "even when…" / "even if…" to the sentence — whatever comes after it is the condition.
- **Number vs condition:** the number tells us *what* result counts as a pass. The condition tells us *when* (in which situation) we must still get that result.
- **Scope = task:** the scope is often just an FR. The FR says *what*; the NFR says *how well* that same task must work.

```
FR:  "Staff should be able to play a call recording."                                         ← WHAT
NFR: "Only staff of the clinic that owns the recording can play it, even via a shared link."  ← HOW WELL (scope = that FR)
```
The scope should name the task, not the work we do to build it ("build a call list page" ❌ → "loading the call history page" ✅).

### 2.4 Complaint → NFR (worked example)

**Complaint:** *"The agent says 'booked', but sometimes the booking never shows up on the dashboard."*

1. **Quality:** **Reliability** — the system said "done" for something that never happened. (This is the **Wrong** case from failure thinking.)
2. **Scope:** saving a booking after the agent says "booked".
3. **Number:** 99% is too low — 1 patient in 100 would reach the clinic and find no slot. **The more one mistake costs, the stricter the number** → *every* confirmed booking, within 5 s.
4. **Condition:** "past 1,000 bookings" is wrong (copied from the speed example) — old bookings don't make saving a new one harder. The hard situations are: **100 booking calls at the same time** (peak), the database/API being slow or down, and the call dropping right after the agent says "booked". Use the most realistic hard case in the NFR. List the other cases under **failure modes**.

> **Final NFR:** "Every booking the agent confirms must appear on the clinic dashboard within 5 seconds — even when 100 booking calls happen at the same time."

Careful: "the dashboard should show which calls were booked" → this is a new **FR** (a new capability), not an NFR.

### 2.5 FR or NFR? — Break test

```
Requirement breaks →  the feature STOPS working?               → FR
                   →  it still works, but BADLY (slow/unsafe)? → NFR
```
- "Patient should be able to book" breaks → no booking can happen at all → FR
- "Booking appears within 5 s" breaks → the booking happens, but late → NFR

**Hook:** **"Stops or gets worse?"**

### 2.6 Three buckets

```
1. Core / In scope   → we build it in v1
2. Later / Future    → we build it later (v2)
3. Out of scope      → we don't build it at all
```
**Why write "out of scope" down on purpose?**
- It stops **scope creep** (the scope slowly grows, and the work never finishes).
- **What others will assume:** if we stay silent, the clinic owner assumes "you're adding payments too, right?", and the reviewer thinks we missed it. Once it's written down, everyone can see **it was a decision, not something we forgot.**

> **English:** "For v1, call booking is core. SMS reminders come later. Payments are out of scope — we chose that on purpose."

---

## 3. Trade-offs

**5 parts:**
```
1. X over Y        → what we chose, and what we didn't
2. Because Z       → the reason + EVIDENCE (numbers we measured ourselves)
3. Downside W      → the cost of X that we accept
4. Mitigation M    → how we will handle W
5. Revisit trigger → when we reopen the decision (BEFORE we hit the limit)
```
Hook (suggestion): **Choice, Cause, Cost, Cover, Comeback.**

**Example:**
> "We chose **streaming STT** over **batch STT** because **the agent must start replying while the caller is still speaking**. We measured it: batch added about 1.5 seconds per reply. The downside is **higher cost per minute**. We handle it by **using batch STT for post-call transcripts**. We'll revisit if **STT cost goes above ₹50,000 a month**, or if a batch model takes less than 300 ms."

(STT = speech-to-text. Streaming = text arrives while the caller is still speaking; batch = text arrives only after the audio ends. The numbers are examples.)

- **Why evidence?** Without proof, "because" is just an opinion; a number we measured makes it a real decision. Z often comes from an NFR ("reply starts within 1 s"); the evidence proves that claim.
- Set the **revisit trigger** before we hit the limit, so there is time to think and change the plan.

---

## 4. Bottlenecks

**Bottleneck = the slowest or smallest part of the system, which limits the speed or capacity of the whole system.** Like the neck of a bottle: however big the bottle is, water only flows out as fast as the neck allows.

```
Caller → STT (200 ms) → LLM (900 ms) → TTS (300 ms) → reply
                        ^^^^^^^^^^^^ bottleneck — make STT 2x faster: little gain; make the LLM faster: the reply gets faster
```

### Bottleneck vs Single point of failure (SPOF)
```
Bottleneck = the system still RUNS, but this part LIMITS speed/capacity   → slow
SPOF       = this part has no BACKUP; if it fails, the WHOLE system stops → stop
```
An LLM with only one provider can be both: the slowest part, and a part with no backup. That's why the hook includes "Single" — but the two ideas are different.

### Catching it at design time — Slowest, Smallest, Single
| Word | Question | Catches |
|---|---|---|
| **Slowest** | Follow the request from start to end — how long does each step take? | latency bottleneck |
| **Smallest** | How much can each part handle at once? Which one handles the least? | capacity bottleneck |
| **Single** | Which part has only one copy? | SPOF + limit |

### Example: capacity
```
STT 500 · LLM 100 (rate limit) · TTS 300   → system capacity = the smallest = LLM (100)
LLM raised from 100 → 400                  → now TTS (300) is the bottleneck
```
- **System capacity = the capacity of its smallest part.**
- **The bottleneck moves** — fix one, and the next one shows up. Keep measuring.
- **Senior point:** 100 LLM slots ≠ 100 calls. The LLM runs only while the agent prepares its reply. While the caller is speaking, the LLM does nothing. To find how many calls fit, use Little's Law.

---

## 5. Failure thinking

### Three questions
```
1. How can it break?                  → Down · Slow · Wrong
2. How far does it spread?            → blast radius
3. How do we notice it, and respond?  → detect + respond
```

### Down, Slow, Wrong
```
Down  → the TTS API is down, no response at all
Slow  → the LLM takes 8 s instead of 900 ms; the caller hears only silence
Wrong → STT heard "10 o'clock" as "2 o'clock"; the booking is saved at the wrong time
```
**Wrong is the most dangerous** — Down and Slow are loud (easy to notice); Wrong is silent (nobody notices). No alert fires, so the damage goes on until a person catches it. So we need extra checks:
- **Read** the booking time **back** to the caller ("Tomorrow at 10, is that right?")
- **Before** saying "booked", confirm in the DB that the booking was saved
- **Evals:** check a sample of calls

### Blast radius
**How much of the system (and how many users) one failure affects.**
- 20 clinics, **one shared LLM API key**, a spike at one clinic → rate limit → **all 20** clinics down. This is called a **noisy neighbour**.
- **How to shrink it — isolate (bulkhead):** a separate key for each clinic (or group), or a per-clinic quota in our own gateway (e.g. max 30 calls at once). Then a spike at one clinic only blocks that clinic. The name comes from ships: a ship is split into separate rooms (compartments), so a hole in one room doesn't sink the whole ship.
- A backup LLM / retry helps with **recovery**, but does **not** shrink the blast radius (the busy clinic will fill up the backup too; and if another clinic has used up the limit, retrying is useless).
- **Tenant** = one customer of a shared system (here, each clinic).

### The 6 response tools — one story (the LLM call is stuck)
```
1. Timeout      → no answer in 3 s, assume it's stuck   (this comes first — without it, when would we retry?)
2. Retry        → try again once or twice (with a limit)
3. Fallback     → switch to a second LLM provider
4. Degrade      → keep running with fewer features (fixed script: "Let me take a message, the clinic will call you back")
5. Save partial → save whatever we already have: the caller's name/number
6. Fail safe    → end the call politely + alert the team
```
Hook: **Wait → Again → Other → Less → Keep → Close.** (Full name of Degrade: graceful degradation.)

> **English:** "If the LLM call gets stuck, we time out and retry once. Then we fall back to a second provider. If that also fails, we degrade to a fixed script that just takes a message."

---

## 6. 10x and YAGNI

### 10x rule (Jeff Dean)
**Today's design should handle 10x with small changes; at 100x, expect a redesign.** The rule does not say "build for 10x today".
- 50 → 500 calls at once: add workers, raise limits
- 50 → 5,000: new architecture (multi-region, our own STT…)

### YAGNI — You Aren't Gonna Need It
Don't build what you don't need yet. **Test question:** *"If we don't build it now, how expensive will it be to add later?"*
```
CHEAP later     (a change in 1 place)        → don't build it now
EXPENSIVE later (50 places, data migration)  → build a CHEAP DOOR now
```
- **LLM wrapper:** a cheap door — a small step now that makes the later change easy. It takes 1 hour: we call the provider through one function. Multi-provider routing = the expensive building; build it only when we reach its revisit trigger.
- **`clinic_id` column (1 clinic today):** build it now. Today it is one column. Later it means a full data migration and a filter in every query. Miss it in one place, and **one clinic sees another clinic's calls** (Wrong + security).
- **YAGNI ≠ build nothing.** If it's cheap later, skip it for now; if it's expensive later, do it now.

---

## 7. Estimation

### 7.1 Peak, not average
If we design for the average, the system fails **exactly at the busiest time**. A clinic gets 10 calls per hour on average, but 60 on Monday from 10–11 AM. **Design for 60.**

### 7.2 Storage
```
bitrate × seconds = bits(kb) → ÷ 8 = bytes(KB) → ÷ 1000 = MB
```
- kbps is a **rate**; multiply by seconds → the "per second" cancels out → only **kb** is left.
- **÷ 8, not × 8:** 1 byte = 8 bits; a byte is the bigger box → the count gets smaller. (80 rupees in 10-rupee notes → 8 notes.)
- **Small b = bits, big B = bytes** — kb and KB differ by 8x.

**Example (phone call, G.711 64 kbps, 5 min):** 64 × 300 = 19,200 kb → ÷ 8 = 2,400 KB → **2.4 MB**
**Example (128 kbps, 1 min) — "divide by 8 first" trick:** 128 ÷ 8 = 16 KB/s → × 60 = 960 KB ≈ **1 MB/min** → 10,000 min ≈ 10 GB.

### 7.3 Codecs, sample rate, Nyquist
- **Sample rate** = how many times per second we measure the sound (one "photo" each time). **All digital audio has a sample rate** — browser audio too.
- **Nyquist rule:** to catch a sound correctly, the sample rate must be at least **2x** the highest frequency → so the highest frequency it can catch is **half** the sample rate.
```
Phone (G.711, Twilio SIP):  8 kHz, 64 kbps  → sound up to ~4 kHz
Browser (Opus, WebRTC):     up to 48 kHz    → sound up to ~20 kHz (humans hear up to ~20 kHz)
```
- "s", "f", "sh" have frequencies above 4 kHz → phone audio cuts them off → "fifteen" and "fifty" sound alike. **STT makes more mistakes on phone calls** (numbers, names) → **read back** the important details.
- **Compression ≠ sample rate:** sample rate = how often we measure; compression (Opus) = how much we shrink the measured data.

### 7.4 Little's Law
**L = λ × W** — how many are in the system at once = arrival rate × how long each one stays.

```
4 steps: find λ → find W (measure it, or make a good guess) → match units → multiply
```
- 4 calls/min × 3 min = **12 calls at once** (every call that came in during the last 3 min is still running)
- 10 customers/hour × 0.5 hour = 5 inside the shop
- 150 QPS × 0.2 s (assumed response time) = **30 requests running at once**
- 20 LLM req/s × 1.5 s = **30 LLM calls at once** → compare with the provider's limit (= capacity bottleneck check)

Rules: units must match · works for any system · use peak λ for the busiest time · round up only the final answer.
**Not the same as peak factor:** peak factor = how much higher the load is at the busiest time than on average; Little's Law = how many at once. First find peak λ, then apply Little's Law.

### 7.5 QPS
```
QPS = requests per day ÷ 100,000 (1 lakh; 1 day = 86,400 s ≈ 100,000 s) × peak factor
```
5 million/day ÷ 100,000 = 50 QPS avg × 3 = **150 QPS peak**. The shortcut gives a number about 15% too low. That's fine; we only need the rough size (tens, hundreds or thousands).

**When to use which:**
```
Phone call  → lasts minutes, holds the line → "how many are OPEN at once?"   → Little's Law
API request → done in ms                    → "how many ARRIVE each second?" → QPS
```

### 7.6 Bandwidth
```
bitrate per stream × streams per call (voice: 2) × calls at once → compare with the network bandwidth
```
64 kbps × 2 × 500 = 64,000 kbps = **64 Mbps = 0.064 Gbps = 6.4% of 1 Gbps** → plenty. Units: kbps ÷1000 Mbps ÷1000 Gbps. Packet headers add a little extra, so keep some spare bandwidth (**headroom**).

### 7.7 LLM cost
- 1 token ≈ 4 characters ≈ ¾ of a word. Input and output have different prices.
- **In multi-turn calls, input is the main cost.** The LLM has no memory, so we resend the full history on every turn:
```
Turn 1:  system prompt + turn 1
Turn 2:  system prompt + turn 1 + turn 2
Turn 10: system prompt + turn 1 … turn 10   ← input keeps growing
Output:  a short reply every turn           ← output stays small
```
- **Fix: prompt caching** — the repeated part (the system prompt) is charged at a lower price.

### 7.8 Latency numbers
| Operation | Time |
|---|---|
| Read from RAM | ~100 ns |
| Read 4 KB from SSD (random) | ~150 µs |
| Same data center round trip | ~0.5 ms |
| Across the world (California ↔ Netherlands) | ~150 ms |

- ns → µs → ms → s, each step ×1000. RAM ≈ 1,500× faster than SSD → keep often-used data in RAM (cache).
- **Apply:** agent in Europe, LLM in California → **~150 ms extra on every turn** (~450 ms if STT and TTS were in California too). In voice, we have about 1 s for the whole reply → distance alone uses 15% of it.
- **Fix: co-locate** — put STT, LLM and TTS in the same region (use the LLM's EU region, or move the agent to the same region as the LLM). "Edge" is a different idea: edge = close to the user; here we need the pipeline parts close to each other.

---

## 8. Design doc (theory, 13 Oct)

- **When to write one:** when the **decision is hard to undo or affects many people** — not because the system is big.
- **Show weak spots in 3 places:** downsides in trade-offs · failure modes · open questions.
- **Open question format:** question + owner + blocking/non-blocking + default (what we assume until it's answered) + recommendation.
- Sections + template: [design-doc-template.md](design-doc-template.md).

---

**Next step:** revise on your own (practice page: `p0-practice.html`) → role-play (gathering requirements) → `designs/01-...md` → review → P0 done → P1.
