---
title: "The Karpathy Guidelines: Taming AI Coding Agents With Structured Discipline"
layout: single
date: 2026-05-19
categories:
  - artificial-intelligence
  - software-development
tags:
  - ai-agents
  - coding-assistants
  - llm-limitations
  - software-engineering
  - best-practices
  - ai-guardrails
excerpt: "The Karpathy Guidelines offer a structured pre-coding checklist designed to counteract the most common and costly mistakes AI coding agents make — from over-engineering solutions to silently acting on wrong assumptions."
header:
  overlay_image: "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80"
  overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.5) 100%)"
  caption: "Photo by [Kevin Ku](https://unsplash.com/@ikukevk) on [Unsplash](https://unsplash.com)"
  teaser: "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80"
---

# The Karpathy Guidelines: Taming AI Coding Agents With Structured Discipline

You ask your AI coding agent to add a validation check to a form field. Five minutes later, you're staring at a brand-new validation framework — complete with a plugin architecture, a custom error message localisation system, three new utility classes, and a configuration file you never asked for. The original form field? It now validates correctly. But so does every hypothetical form field in every hypothetical future feature that nobody has requested yet. Your simple task has metastasised into an over-engineered monument to premature abstraction.

If this sounds familiar, you're not alone. In January 2026, Andrej Karpathy — the former head of AI at Tesla and founding member of OpenAI — published a now-famous thread describing his experience coding extensively with AI agents. His observations were sharp, specific, and instantly recognisable to anyone who had spent time working alongside these tools. The community's response was immediate: the thread accumulated over 40,000 reposts and sparked a wave of practical frameworks aimed at addressing the problems he described.

Among the most effective of those frameworks is a set of behavioural guidelines that have come to bear his name — the *Karpathy Guidelines*. Published as part of the [Claude Code Playbook](https://ao92265.github.io/claude-code-playbook/skills/karpathy-guidelines/SKILL/), they provide a structured pre-coding checklist designed to be injected into AI agent instructions, forcing the agent to slow down, think critically, and resist its worst impulses before writing a single line of code.

---

## What Karpathy Observed

Karpathy's original thread didn't mince words about the current state of AI-assisted coding. Despite describing the shift to agent-driven development as "easily the biggest change to my basic coding workflow in ~2 decades of programming," he catalogued a litany of recurring failures:

> "The mistakes have changed a lot — they are not simple syntax errors anymore, they are subtle conceptual errors that a slightly sloppy, hasty junior dev might do. The most common category is that the models make wrong assumptions on your behalf and just run along with them without checking."

This is the central problem. The errors AI agents make are no longer the kind a compiler catches. They are errors of *judgement* — the kind that require understanding intent, context, and the broader architecture of a system to detect. Karpathy continued:

> "They also don't manage their confusion, they don't seek clarifications, they don't surface inconsistencies, they don't present tradeoffs, they don't push back when they should, and they are still a little too sycophantic."

And on the question of code quality:

> "They also really like to overcomplicate code and APIs, they bloat abstractions, they don't clean up dead code after themselves... They will implement an inefficient, bloated, brittle construction over 1000 lines of code and it's up to you to be like 'umm couldn't you just do this instead?' and they will be like 'of course!' and immediately cut it down to 100 lines."

These observations describe a pattern that anyone working with AI agents will recognise. The agent is simultaneously brilliant and reckless — capable of producing remarkable solutions at speed, but equally capable of producing remarkable messes with the same confidence. The Karpathy Guidelines exist to address exactly this tension.

---

## The Five-Step Pre-Coding Checklist

The Guidelines are structured as a five-step checklist that must be executed before any code is written. For trivial single-line changes, steps one and two may be abbreviated, but the principle remains: *think before you type*. Each step targets a specific category of LLM failure mode.

### Step 1: Surface Assumptions and Ambiguities

> 1. List every assumption the implementation will rely on.
> 2. Check whether each assumption is explicit in the request or inferred.
>    - If inferred and consequential: state it aloud and ask for confirmation before proceeding.
>    - If inferred and obvious: note it briefly, then continue.
> 3. Check whether multiple valid interpretations of the request exist.
>    - If yes: present them as numbered options. Do not pick silently. Wait for the user to select one.
>    - If no: continue.
> 4. Check whether a simpler approach exists than what was asked for.
>    - If yes: surface it. Push back if warranted. Do not silently implement the more complex path.
>    - If no: continue.
> 5. If anything remains unclear after the above checks, stop. Name exactly what is confusing. Ask.

**What this prevents:** This step directly targets the single most common failure Karpathy identified — models making wrong assumptions and running with them without checking. Current LLMs are trained to produce confident, fluent responses. They are optimised for helpfulness and coherence, not for expressing uncertainty. When faced with an ambiguous request, an LLM will almost never say "I'm not sure what you mean." Instead, it will silently choose an interpretation — often the most complex one — and execute it with full confidence.

**Why it matters:** A human developer who misunderstands a requirement will typically discover the misunderstanding during a conversation with a colleague, a code review, or a stand-up meeting. The social dynamics of software teams create natural checkpoints where assumptions get surfaced and corrected. AI agents operate outside these social structures. Without an explicit instruction to surface assumptions, they have no mechanism to course-correct before committing to an approach.

The instruction to check whether a *simpler* approach exists is particularly important. LLMs have been trained on vast codebases full of enterprise-grade abstractions, design patterns, and architectural frameworks. They have internalised the patterns of over-engineered software, and they reproduce those patterns by default. Forcing the agent to consider simplicity before proceeding is an explicit counterweight to this training bias.

---

### Step 2: Apply Simplicity Constraint

> Before writing code, verify the planned implementation passes all of the following:
>
> - Contains no features beyond what was explicitly requested. If any exist, remove them.
> - Contains no abstractions added for a single-use case. If any exist, flatten them.
> - Contains no "flexibility" or "configurability" that was not requested. If any exist, remove them.
> - Contains no error handling for scenarios that cannot occur given the current inputs. If any exist, remove them.
>
> Apply the senior-engineer test: "Would a senior engineer call this overcomplicated?"
>
> - If yes: rewrite to the minimum viable implementation.
> - If no: continue.

**What this prevents:** This step is a direct antidote to the over-engineering problem Karpathy described — the tendency to produce 1,000 lines of code when 100 would suffice. LLMs exhibit a consistent bias toward adding more rather than less. They add error handling for impossible scenarios. They create configuration options nobody asked for. They build abstraction layers to support extension points that will never be used.

This behaviour emerges from the statistical nature of their training. In the vast corpora of code they've been trained on, abstractions, error handling, and configurability appear frequently — because the codebases in public repositories tend to be libraries and frameworks designed for reuse. The model learns that "good code" includes these elements, without understanding the crucial contextual question: *is this a library, or is this a one-off script?*

**Why it matters:** Over-engineered code isn't just aesthetically unpleasant — it's a maintenance liability. Every unnecessary abstraction is a piece of complexity that future developers (or future AI agents) must understand, maintain, and work around. Every unrequested feature is a potential source of bugs in code that serves no purpose. The "senior-engineer test" is a brilliantly practical heuristic: it reframes the question from "is this code good?" to "would someone experienced find this unnecessarily complicated?"

---

### Step 3: Apply Surgical Change Constraint

> Before editing any existing file, apply these rules:
>
> 1. Identify the exact lines the request requires changing. Plan to touch only those lines.
> 2. Do not improve, reformat, or restructure adjacent code, comments, or formatting — even if it would be better.
> 3. Do not refactor code that is not broken.
> 4. Match the existing code style exactly, even if it differs from preferred style.
> 5. If unrelated dead code is noticed, mention it in the response. Do not delete it.
> 6. After changes are drafted, check for orphaned imports, variables, or functions created by the edits.
>    - If found: remove them (these are your mess to clean up).
>    - If pre-existing dead code is found: leave it. Mention it only.
>
> Verify: every changed line traces directly to the user's request. If a line cannot be traced, remove it.

**What this prevents:** This step addresses one of the most insidious behaviours of AI coding agents — making unsolicited changes to code that wasn't part of the request. Karpathy noted that models "still sometimes change/remove comments and code they don't like or don't sufficiently understand as side effects, even if it is orthogonal to the task at hand."

This is not a minor annoyance. In professional software development, every change to a codebase carries risk. Changes must be reviewed, tested, and understood. When an AI agent quietly reformats a file, deletes a comment it considers redundant, or refactors a function it considers inelegant, it creates noise in the version control history that obscures the actual intended change. It may also break things — that "redundant" comment might be a crucial note for a future developer, and that "inelegant" function might work that way for a reason the agent doesn't understand.

**Why it matters:** The distinction between "your mess to clean up" (orphaned imports created by your changes) and "pre-existing dead code" (leave it alone) is particularly astute. It establishes a clear principle of *ownership*: you are responsible for the consequences of your changes, but you are not entitled to "improve" code that someone else wrote and that you were not asked to modify. This mirrors a fundamental principle of professional software engineering — the pull request should contain only what was requested, nothing more.

---

### Step 4: Define Verifiable Success Criteria

> Before executing, transform the task into a concrete, testable goal:
>
> | Vague Goal | Concrete Goal |
> |---|---|
> | "Add validation" | Write tests for invalid inputs, then make them pass |
> | "Fix the bug" | Write a test that reproduces it, then make it pass |
> | "Refactor X" | Ensure tests pass before and after, diff is minimal |
>
> For multi-step tasks, state a brief execution plan before starting:
> ```
> 1. [Step] → verify: [check]
> 2. [Step] → verify: [check]
> 3. [Step] → verify: [check]
> ```
>
> If success criteria cannot be defined without clarification, return to Step 1.

**What this prevents:** This step tackles a fundamental limitation of LLMs — their inability to reliably self-assess. Without concrete success criteria, an AI agent has no objective way to determine whether it has completed its task. It may produce code that *looks* correct, passes a superficial review, and even generates convincing explanatory text — but that doesn't actually satisfy the user's intent.

The instruction to write tests *first* and then make them pass is essentially test-driven development (TDD) applied to AI agents. It's powerful because it transforms a subjective question ("does this code work?") into an objective one ("do the tests pass?"). LLMs are far better at meeting concrete, verifiable goals than vague, open-ended ones — this is precisely why Karpathy observed in his original thread that LLMs are "exceptionally good at looping until they meet specific goals."

**Why it matters:** The fallback instruction — "if success criteria cannot be defined without clarification, return to Step 1" — creates a feedback loop that prevents the agent from proceeding when the task is insufficiently defined. This is crucial because LLMs, left to their own devices, will always find *some* interpretation of a vague request and execute it. The result might be technically valid code, but it may not be what the user wanted. Forcing a return to the clarification step is a structural safeguard against the agent's natural tendency to plough ahead regardless.

---

### Step 5: Execute and Verify

> 1. Implement according to the plan from Steps 1–4.
> 2. Run the verification check defined in Step 4.
> 3. If verification passes: report the result with evidence.
> 4. If verification fails: do not claim completion. Investigate, fix, and re-run from this step.

**What this prevents:** This final step addresses the tendency of AI agents to declare victory prematurely. An LLM will generate code, describe what it does, and present the output with confidence — regardless of whether it actually works. Without an explicit instruction to verify and provide evidence, the agent may claim completion based on its own assessment of the code's correctness, which is unreliable.

The instruction "do not claim completion" if verification fails is critical. LLMs are trained on conversational data where responses tend toward agreement and resolution. They are biased toward producing outputs that feel like conclusions. Left unconstrained, they will often say "Done! The validation has been added" when what they should say is "The tests are still failing. Here's what I've tried so far."

**Why it matters:** This step closes the loop on the entire checklist. Without verification, steps one through four are merely good intentions. The requirement to provide *evidence* of success — not just assertions — transforms the agent's output from "trust me, it works" to "here's proof that it works." In a world where AI agents can generate plausible-sounding explanations for code that doesn't function, evidence-based completion is not optional.

---

## The Inherent Weaknesses These Guidelines Reveal

Reading the Karpathy Guidelines carefully, a picture emerges of the fundamental limitations of current-generation large language models. These aren't bugs that will be fixed in the next release — they are structural characteristics of how these systems work.

### Statistical Pattern Matching, Not Understanding

LLMs generate code by predicting the most likely next token based on patterns in their training data. They don't *understand* code in the way a human developer does. They can't reason about what a programme is supposed to do, only about what similar programmes have done in the past. This means they excel at common patterns and fail unpredictably at novel problems or unusual contexts. The Guidelines' emphasis on surfacing assumptions exists because the model literally cannot distinguish between a valid assumption and an incorrect one — both are equally plausible statistical predictions.

### Sycophancy and the Inability to Push Back

Current LLMs are fine-tuned using reinforcement learning from human feedback (RLHF), which optimises for responses that human evaluators rate highly. This creates a systematic bias toward agreement and helpfulness at the expense of accuracy. When a user makes a request, the model's training incentivises it to fulfil that request rather than question it. The Guidelines' instruction to "push back if warranted" runs against the grain of how these models are trained — it's an explicit attempt to override a deeply embedded behavioural tendency.

### No Metacognition

Human developers constantly monitor their own cognitive state. They notice when they're confused, when they're making assumptions, when they're out of their depth. LLMs have no equivalent capability. They cannot assess the reliability of their own outputs. They generate with equal confidence whether they're producing a well-understood pattern or a novel hallucination. The entire five-step checklist is essentially a *prosthetic metacognition* — an external structure that forces the model to perform the self-assessment it cannot do internally.

### Context Window as Working Memory

LLMs operate within a fixed context window that serves as their only form of working memory. They cannot hold long-term state, recall previous sessions, or maintain an evolving mental model of a codebase across interactions. When the context fills up or shifts, earlier information is effectively forgotten. The Guidelines' structured approach — listing assumptions, defining plans, stating success criteria — serves a dual purpose: it constrains the agent's behaviour, and it creates explicit artefacts within the context window that help maintain coherence across a multi-step task.

### The Training Data Bias Toward Complexity

LLMs are trained disproportionately on open-source libraries, frameworks, and tutorial code — all of which tend toward abstraction, generalisation, and extensibility. Production application code, which is often deliberately simple and specific, is underrepresented in training data because it lives behind corporate firewalls. The result is a systematic bias toward the kind of over-engineered solutions that the simplicity constraint is designed to prevent. The model has literally seen more examples of abstract factory patterns than straightforward if-else statements.

---

## The Broader Lesson

The Karpathy Guidelines are more than a practical checklist for AI-assisted coding. They represent a growing recognition that the challenge of working with AI agents is not primarily a technology problem — it's a *management* problem.

These tools are not autonomous colleagues. They are extraordinarily capable but fundamentally unreliable systems that require structured oversight, clear constraints, and explicit verification. The analogy Karpathy and others have used — that working with AI agents is like managing a tireless but inexperienced junior developer — captures something important. You wouldn't let a junior developer ship code without review. You wouldn't let them make architectural decisions without guidance. You wouldn't accept "it looks right to me" as evidence that the work is done.

The Guidelines encode these management principles into a format that AI agents can follow. They are guardrails — not because the agent is malicious, but because it is *confident without being competent* in the ways that matter most. It can write syntactically correct code all day long. What it cannot do, without external structure, is exercise the judgement needed to write the *right* code.

As AI models continue to improve — and they will — some of these limitations will diminish. Models will become better at expressing uncertainty, at pushing back on ambiguous requests, at producing minimal implementations. But the fundamental architecture of next-token prediction means that many of these tendencies are deeply embedded. For the foreseeable future, frameworks like the Karpathy Guidelines will remain not just useful but essential — a bridge between what AI agents can do and what they should do.

The irony, perhaps, is that the guidelines themselves are remarkably simple. Five steps. A few clear rules. No abstractions, no frameworks, no configuration options. Karpathy would approve.
