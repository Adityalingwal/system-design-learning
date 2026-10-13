# System Design Glossary

Is workspace ki canonical language. Term tabhi judta hai jab Aditya use sahi use kar sake.

## Design process

**Functional requirement (FR)**:
Ek line jo batati hai ki system kya kare: ek actor aur uska kaam, "X should be able to Y".
_Avoid_: feature list, use case (jab FR matlab ho)

**Non-functional requirement (NFR)**:
Ek line jo batati hai ki koi kaam kitna achha ho: quality, kaunsa hissa, number (ya check hone wala rule), aur condition.
_Avoid_: quality goal, "-ilities" (jab NFR matlab ho)

**Actor**:
Koi bhi jo system use karta hai, bahar ka (caller, business owner) ya andar ka (engineer, ops).
_Avoid_: user (jab sirf ek type ka matlab na ho)

**Trade-off**:
Ek choice jisme kuch paane ke liye kuch dena padta hai, is format mein: "X liya, Y nahi, kyunki Z. X lene ki keemat: W." Z kisi requirement se aata hai; W wo nuksaan hai jo X ke saath accept kiya. "Trade-off" poore faisle ka naam hai, sirf W ka nahi.
_Avoid_: "iske badle W chhoda" (Y aur W mix ho jaate hain), "best option"
