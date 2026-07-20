# PROPHET-AUDIT — 60-Second Verification Protocol for "He Predicted It" Claims

Reusable procedure derived from CS-0001 (World Cup) and the Venezuela/TikTok case.
Runnable by anyone, on any platform, without special tools. Constitutional basis:
RFC-0009 evidence tiers — a claim cannot rise above **E0** until every step passes.

## Step 1 — Demand the object, not the story

**"He predicted it" is not a claim. "This specific post, published at this exact
timestamp, said exactly this" is a claim.**

If what you received is a *profile link*, a screenshot, a re-upload, or a forwarded
video with no permanent post URL, **stop**. There is nothing to verify. This single
step eliminates the majority of viral prophet claims, because the forwarding chain
strips the one thing that would make the claim testable.

## Step 2 — Decode the real timestamp (works on X and TikTok)

Both platforms embed creation time in their numeric IDs (Snowflake-style: the top bits
are a Unix timestamp). Visible dates and captions can be edited or faked; the ID
cannot.

```
timestamp_unix = numeric_id >> 32          # TikTok video/user id
timestamp_ms   = (tweet_id >> 22) + 1288834974657   # X/Twitter
```

Decode the **post** id (proves when the claim was made) *and* the **account** id
(proves the account even existed). An account created after the event cannot have
predicted it — this alone settles many cases instantly.

## Step 3 — Establish the base rate BEFORE judging the hit

Ask: *what was the publicly expected outcome at the moment of the claim?*

A "prophecy" that matches the mainstream expectation of its own moment is not
foresight — it is **reading the news**. Check contemporaneous coverage, official
statements, and prediction-market prices from the claim's date. Publicly telegraphed
intent (EE-004) is the most common source of fake prophecy: powerful actors announce
what they intend to do, and the "prophet" repackages the announcement as revelation.

## Step 4 — Demand the complete prediction set

One surviving hit is meaningless without the denominator. Ask:

- How many predictions did this source make in the same period?
- Are all of them still visible, or can they be silently deleted?
- Is the winner amplified while the losses are unlisted?

**On any platform permitting free deletion, prediction-set completeness is
unobtainable — and without completeness, no forecast skill can be computed, ever.**
The tier stays E0 permanently regardless of how impressive the hit looks.

## Step 5 — Check resolution elasticity

Was the claim falsifiable at the time it was made? "Something big will happen in
[permanently unstable country]" cannot fail. "Argentina beats Spain 3–2 in the 2026
final" can — and did. Elastic claims are unscoreable by design; precise claims are the
only ones that carry evidential weight, whichever way they resolve.

## Step 6 — Follow the funnel

Identify what the claim monetizes: paid group, signals subscription, platform revenue
share, follower growth. Note whether the environment permits public criticism or bans
it. A community that removes people for auditing calls is engineered to prevent
Step 4.

## Verdict scale

| Steps passed | Tier | Meaning |
|---|---|---|
| Fails Step 1 or 2 | **Not a claim** | Nothing to evaluate |
| Passes 1–2, fails 3 | **E0** | Read the news, called it foresight |
| Passes 1–3, fails 4 | **E0** | Possibly real, permanently unprovable |
| Passes 1–5, small n | **E1** | Genuine but not yet skill |
| Passes all, pre-registered set, scored over time | **E2 → E3** | Measurable forecasting skill |

**Nobody in the viral prophet economy has ever reached E2.** Not because they are all
frauds — because the platforms they use structurally cannot produce completeness.
That is the gap SECM's outcome registry and hash-anchored pre-registration exist to
fill (RFC-0009, RFC-0018, CS-0002).
