# Quality (non-functional) checklist

Kisi bhi naye system / assignment / project ke shuru mein ye list upar se neeche dekho. Har group ke liye ek sawaal: **"is system mein ye matter karta hai? Kitna? Number kya?"**

Ye list yaad nahi karni, har baar dekhni hai. Claude ko bhi project context ke saath ye list reference ki tarah milti hai.

Source: [ISO/IEC 25010 product quality model](https://iso25000.com/en/iso-25000-standards/iso-25010) (9 groups, sub-parts wahin se) + [Hello Interview delivery framework](https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery) (8-item checklist, jo inhi ka chhota rasta hai). Voice AI / agent examples hamare apne hain.

## Kaise use karna hai

1. Har group ke liye likho: **High / Medium / Low / N/A**.
2. High wale 3-5 ke liye **number** likho (jaise "turn latency 1-2 s", "peak pe 20 calls").
3. Jo cheez baad mein badalna mehenga hai (data kahan save hoga, security, consent), unhe pehle soch lo.
4. Baaki cheezein jaise-jaise solution banta hai, jahan fit hoti hain wahan dekhte jao.
5. Jo pata nahi (jaise compliance), use "client se confirm karna hai" likho. Chhodo mat.

## 1. Functional suitability: sahi kaam, poora kaam

| Part | Matlab | Voice / agent example |
|---|---|---|
| Completeness | Saare zaroori kaam system mein hain | Qualify, contact collect, human handoff, sab hain |
| Correctness | Result sahi aaye | Lead sahi qualified / unqualified mark ho |
| Appropriateness | Kaam ke liye features suitable hain | Caller ko sirf wahi sawaal jo us visa ke liye chahiye |

## 2. Performance efficiency: speed, resources, capacity

| Part | Matlab | Voice / agent example |
|---|---|---|
| Time behaviour | Response time, throughput | Bolna band kiya → agent ki awaaz 1-2 s mein, har turn pe |
| Resource utilization | CPU, memory, network kitna lagta hai | Ek worker pe kitni calls |
| Capacity | Maximum limit | Ek saath maximum kitni calls |

## 3. Compatibility: doosre systems ke saath

| Part | Matlab | Voice / agent example |
|---|---|---|
| Co-existence | Same environment mein doosron ko tang na kare | Ek hi worker pe kai agents / clients |
| Interoperability | Information exchange kar sake | CRM, webhook, telephony provider se judna |

## 4. Interaction capability: use karna kitna aasaan

| Part | Matlab | Voice / agent example |
|---|---|---|
| Appropriateness recognizability | User samajh sake ki ye uske kaam ka hai | Agent shuru mein batata hai wo kya kar sakta hai |
| Learnability | Seekhna aasaan | Business owner dashboard jaldi samajh le |
| Operability | Chalana aur control karna aasaan | Prompt / config badalna aasaan |
| User error protection | User ki galti se bachaye | Caller ne galat email bola to confirm kare |
| User engagement | Interaction inviting lage | Agent ka tone natural, robotic nahi |
| Inclusivity | Alag-alag log use kar sakein | Alag accent / language wale callers |
| User assistance | Madad mile | Agent na samjhe to human handoff |
| Self-descriptiveness | Bina manual ke clear ho | Dashboard pe call ka status saaf dikhe |

## 5. Reliability: chalu rahe, fail ho to sambhale

| Part | Matlab | Voice / agent example |
|---|---|---|
| Faultlessness | Normal chalte samay galti na ho | Call flow bina bug ke chale |
| Availability | Jab chahiye tab chalu | Kisi bhi time call uthe |
| Fault tolerance | Fault ke baad bhi chale | Primary STT / LLM fail → secondary |
| Recoverability | Failure ke baad data aur state wapas | Call beech mein kate to partial lead save rahe |

## 6. Security: kaun kya dekhe, data safe

| Part | Matlab | Voice / agent example |
|---|---|---|
| Confidentiality | Sirf authorized ko data | Recording / transcript sirf allowed logon ko |
| Integrity | Data bina ijazat badle nahi | Lead data koi edit na kar sake |
| Non-repudiation | Kaam hua, ye saabit ho sake | Consent liya gaya, uska record |
| Accountability | Kisne kiya, ye trace ho | Kisne dashboard pe record badla |
| Authenticity | Pehchaan saabit ho | Webhook sach mein apne provider se aaya |
| Resistance | Attack mein bhi chale | Abuse / spam calls se bachav |

## 7. Maintainability: badalna aasaan

| Part | Matlab | Voice / agent example |
|---|---|---|
| Modularity | Ek hissa badle, baaki na toote | Router / agent / prompt alag-alag hissa |
| Reusability | Doosri jagah kaam aaye | Contact collection agent kai clients mein |
| Analysability | Problem kahan hai, samajh aaye | Kisi turn pe latency kahan gayi, dikhe |
| Modifiability | Bina bug ke badal sako | Naya visa type jodna |
| Testability | Test aasaan | Simulated call se test |

## 8. Flexibility: naye load / environment pe dhale

| Part | Matlab | Voice / agent example |
|---|---|---|
| Adaptability | Naye environment pe chale | Nayi telephony / cloud |
| Scalability | Load badhe ya ghate to capacity badle | 5 calls se 500 calls |
| Installability | Install / uninstall aasaan | Naya worker deploy karna |
| Replaceability | Doosre product ki jagah le sake | Vapi → LiveKit migration |

## 9. Safety: insaan ko nuksaan

| Part | Matlab | Voice / agent example |
|---|---|---|
| Operational constraint | Safe limit ke andar rahe | Aam taur pe voice AI mein kam relevant |
| Risk identification | Risk pehchane | Medical / emergency wali call ho to |
| Fail safe | Fail ho to safe mode mein jaaye | Samajh na aaye to human ko hand off |
| Hazard warning | Risk ki warning de | Emergency keywords pe alert |
| Safe integration | Jodne pe bhi safe | Kisi aur system se judne pe |

## Ye ISO list mein nahi, par real kaam mein aati hain

| Cheez | Matlab | Voice / agent example |
|---|---|---|
| Cost | Kharcha | Ek call ka kharcha (STT + LLM + TTS + telephony) |
| Observability | Kya ho raha hai, kaise dikhega | Logs, metrics, per-turn latency waterfall |
| Answer quality / evals | Model ka jawab sahi hai, kaise naapein | Hallucination, script follow hua ya nahi |
| Latency budget | Total latency ko hisson mein baantna | STT / LLM / TTS / network ka alag-alag budget |

## Project template (copy karke bharo)

| Group | Importance | Number / target | Notes |
|---|---|---|---|
| Functional suitability | | | |
| Performance efficiency | | | |
| Compatibility | | | |
| Interaction capability | | | |
| Reliability | | | |
| Security | | | |
| Maintainability | | | |
| Flexibility | | | |
| Safety | | | |
| Cost / Observability / Evals | | | |
