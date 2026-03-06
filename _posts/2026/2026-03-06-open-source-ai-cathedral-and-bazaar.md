---
title: "The Bazaar Fights Back: Can Open Source AI Overtake the Closed Giants?"
layout: single
date: 2026-03-06
categories:
  - artificial-intelligence
  - open-source
  - technology
tags:
  - open-source
  - ai
  - machine-learning
  - llm
  - transparency
  - community
  - cathedral-and-bazaar
  - innovation
  - software-development
excerpt: "Nearly thirty years ago, Eric Raymond described two models of software development—the Cathedral and the Bazaar. That tension has never felt more relevant than it does today, as open source AI models begin to challenge the dominance of the closed commercial giants."
header:
  overlay_image: "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=1200&h=400&fit=crop&crop=entropy&auto=format&q=80"
  overlay_filter: "linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.5) 100%)"
  caption: "Photo by [Sean Lim](https://unsplash.com/@seanlimm) on [Unsplash](https://unsplash.com)"
  teaser: "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=600&h=300&fit=crop&crop=entropy&auto=format&q=80"
---

# The Bazaar Fights Back: Can Open Source AI Overtake the Closed Giants?

In 1997, Eric S. Raymond published an essay that would become one of the most influential texts in software development history. *The Cathedral and the Bazaar* contrasted two radically different philosophies of building software. The Cathedral: code crafted carefully and in private by a small elite, released to the world only when deemed perfect. The Bazaar: code developed out in the open, chaotically, with contributions from thousands of strangers—and, counterintuitively, often producing the better result.

Raymond's central observation was deceptively simple: "Given enough eyeballs, all bugs are shallow." He called this Linus's Law, in honour of Linus Torvalds, whose open development of the Linux kernel was the essay's primary inspiration. The idea was that a sufficiently large community of developers, each with different perspectives and motivations, would find and fix problems faster than any isolated team—however talented—ever could.

Nearly three decades later, that same tension is playing out again, on a far larger stage. This time the stakes aren't just which operating system runs your server—they're about who controls the most powerful technology humanity has ever built.

## The Cathedral Moment in AI

When the current wave of large language model excitement began in earnest with the release of ChatGPT in late 2022, the dominant players looked very much like cathedral builders. OpenAI, Google DeepMind, and Anthropic constructed their models behind closed doors, trained on proprietary datasets, and deployed them through tightly controlled APIs. The weights—the actual learned parameters that define a model's behaviour—were not shared publicly. Neither, in many cases, were the training datasets, the precise architectures, or the full details of the fine-tuning and alignment techniques used.

There were understandable reasons for this secrecy. Training these models costs tens or hundreds of millions of dollars. The competitive advantage is enormous. And there are genuine safety concerns about releasing highly capable models to anyone who might choose to misuse them. Cathedral builders have always had arguments in their favour.

But secrecy has a cost, and that cost is becoming increasingly apparent.

## Cracks in the Walls

The cathedral model depends on the cathedral's walls holding. In AI, those walls started cracking almost immediately.

Meta's release of the LLaMA model family in 2023 was a watershed moment. When the weights for the first LLaMA model leaked—and then, with subsequent versions, were deliberately made public—it demonstrated something important: that competitive open models were achievable without the full resources of a frontier lab. Suddenly, researchers, hobbyists, and companies worldwide had access to genuinely capable models that they could run locally, fine-tune for specific tasks, and study in depth.

What followed looked exactly like Raymond's bazaar. Within weeks of each LLaMA release, the community had produced fine-tuned variants, quantised versions that ran on consumer hardware, new training techniques, and detailed analyses of exactly what the models had learned. The pace of iteration was extraordinary—not because any single contributor was more talented than the researchers at OpenAI or Google, but because there were simply so many of them, all looking at the problem from different angles simultaneously.

More recently, models from Mistral AI, the Allen Institute for AI, and various academic consortia have continued to close the capability gap with the closed frontier models. DeepSeek, developed in China and released openly, sent shockwaves through the AI industry in early 2025 by demonstrating that frontier-level performance was achievable at a fraction of the previously assumed cost. The cathedral builders found, to their considerable discomfort, that the bazaar was catching up fast.

## Why Open Source Has Structural Advantages

Raymond's insight about bugs and eyeballs applies to AI with even greater force than it did to traditional software, for several reasons.

**Transparency enables trust.** When a closed commercial model produces a biased, dangerous, or simply wrong output, users have no way to understand why. When an open model does the same, researchers can inspect the weights, analyse the training data, trace the failure mode, and propose a fix. Transparency is not just academically desirable—it's operationally essential if AI systems are to be deployed in high-stakes domains like medicine, law, or infrastructure.

**Fine-tuning unlocks specialisation.** A general-purpose commercial model, however capable, is a compromise. It is trained to be broadly useful and to avoid a wide range of potential harms, which inevitably means it is more cautious, more generic, and less useful for specific professional applications than it might otherwise be. An open model can be fine-tuned by domain experts—doctors, lawyers, scientists, engineers—on domain-specific data, to produce systems that are genuinely expert rather than merely generalist. This is not a marginal improvement; for many real-world use cases, it is transformative.

**Community catches what committees miss.** Commercial AI labs have safety teams, red teams, and extensive internal evaluation processes. But they are still small communities of people with shared backgrounds, shared assumptions, and shared blind spots. The open source community is none of these things. It is geographically dispersed, culturally diverse, and motivated by wildly different concerns. This diversity is a feature. The security vulnerabilities, failure modes, and cultural biases that an internal team might never encounter are often discovered quickly when millions of people around the world start experimenting with a model.

**No vendor lock-in.** Organisations that build products on top of closed commercial APIs are at the mercy of those providers. Pricing can change. APIs can be deprecated. Capabilities can be modified without notice. Terms of service can be updated to exclude use cases that were previously permitted. Open models, running on infrastructure you control, eliminate this dependency entirely. In an era when AI is becoming critical business infrastructure, the ability to own your stack is not a luxury—it is a strategic imperative.

**The innovation surface is enormous.** Closed models are innovated upon by their development teams. Open models are innovated upon by everyone. Every researcher who discovers a better training technique, every engineer who finds a more efficient architecture, every practitioner who identifies a new fine-tuning approach—all of these contributions can flow back into the open ecosystem in ways that are simply not possible with proprietary systems.

## Running the Numbers: What Does AI Actually Cost?

The philosophical arguments for open source are compelling enough on their own, but the economic case may ultimately prove the most decisive. Let us look at what AI inference actually costs across the different deployment models, because the numbers tell a striking story.

### Commercial Closed APIs

The frontier commercial providers charge by the token—roughly speaking, by the fragment of text processed. At the time of writing, a model like GPT-4o runs at approximately $2.50 per million input tokens and $10 per million output tokens. Anthropic's Claude 3.5 Sonnet is in broadly similar territory. These prices have fallen substantially compared to two years ago, but they remain non-trivial once you start building anything at scale.

To make this concrete, consider a modest production application—a document processing assistant handling 10,000 queries per day, each consuming around 2,000 input tokens and generating 500 output tokens in response. Running those numbers through a GPT-4o-class model yields somewhere around $50–70 per day, or roughly $1,500–2,000 per month. For a small team building an internal tool, that is manageable. For a startup trying to serve thousands of users, it starts to constrain the business model significantly. For an enterprise processing millions of documents, it becomes genuinely eye-watering.

There is also an unpredictability problem. API pricing is set unilaterally by the provider and can change with relatively little notice. An application that is economically viable today can become unviable tomorrow if the provider revises its pricing structure—or if the model you are relying on is deprecated in favour of a new version with different pricing.

### Hosted Open Source: The Middle Ground

An increasingly popular option sits between fully closed commercial APIs and fully self-hosted models: third-party inference providers that host open source models and charge for access. Services such as Together AI, Fireworks AI, and Groq offer API-compatible endpoints for models like Llama 3, Mistral, and Mixtral at significantly lower prices than the frontier commercial providers—often 80–90% cheaper for comparable capabilities.

Running the same document processing workload on a hosted Llama 3 70B instance through one of these providers might cost $150–300 per month rather than $1,500–2,000. The capability gap for most practical tasks is modest; the cost gap is enormous. You also gain the benefits of open model lineage—the ability to switch providers, to move to a different model, or to ingest a self-hosted option later—while still avoiding the operational complexity of running infrastructure yourself.

The trade-off is that you are still dependent on a third-party provider, even if that dependency is less acute than with a closed commercial API. Your data still leaves your premises. The provider could still change their pricing, deprecate models, or go out of business.

### Self-Hosting on Cloud Infrastructure

For organisations that need data sovereignty or want to eliminate third-party dependencies entirely, the next option is running open models on cloud virtual machine instances with GPU acceleration. This is operationally more complex but economically interesting above certain usage thresholds.

A cloud-hosted NVIDIA A100 80GB instance—powerful enough to run a 70-billion-parameter model comfortably—currently costs in the region of $2.50–3.50 per hour from the major cloud providers, depending on reservation type and provider. A reserved instance commitment for a year might bring this down to around $1.50–2.00 per hour. At roughly 730 hours per month, you are looking at $1,100–2,500 per month for a dedicated GPU instance capable of serving a moderately busy production workload.

That sounds comparable to, or even more expensive than, the commercial API cost calculated above—but the economics change dramatically as usage scales. A single GPU instance serving the same document processing workload but at ten times the volume costs the same $1,100–2,500 per month. The commercial API cost at that volume would be $15,000–20,000 per month. Beyond a certain utilisation threshold, self-hosted open models become dramatically cheaper, often by an order of magnitude.

### The On-Premises Hardware Argument

For organisations with the highest volumes, the most stringent data sovereignty requirements, or simply the longest time horizons, owned hardware makes the economics even more compelling—once you can absorb the upfront capital cost.

An NVIDIA RTX 4090, with its 24GB of VRAM, can run 7–13 billion parameter models at full quality or adequately quantised 70B models with some performance trade-off. It costs around £1,500–2,000 new. Amortised over three years of useful working life, that is roughly £40–55 per month in capital cost. Add electricity at perhaps £20–30 per month for continuous operation, and your total running cost for serving local AI inference is around £60–85 per month. Even accounting for the occasional maintenance overhead and the fact that a single consumer GPU serves lighter workloads, this represents a staggering reduction in per-query cost compared to commercial API pricing.

For larger deployments, a small cluster of four A100 or H100 cards—enough to serve a serious enterprise workload—represents a capital investment of £40,000–80,000 but a monthly running cost of perhaps £500–1,000 in electricity and maintenance. An organisation spending £15,000 per month on commercial API access could recover that hardware investment in three to six months and run for free thereafter.

The catch, of course, is that "free" elides the real costs: engineering time to operate the infrastructure, the expertise required to manage and update models, the responsibility for security and availability, and the opportunity cost of that capital outlay. Not every organisation has a machine learning engineer who can set up and maintain an inference stack, and hiring one is not cheap. The total cost of ownership calculation must be honest about the hidden costs of self-hosting.

### The Break-Even Picture

Laying this out more simply as a rough framework:

| Deployment Model | Monthly Cost (illustrative moderate workload) | Data Sovereignty | Flexibility |
|---|---|---|---|
| Frontier commercial API | £1,200–1,800 | Low | Low |
| Hosted open source API | £120–250 | Medium | Medium |
| Cloud GPU (open model) | £900–2,000 | High | High |
| Owned hardware (open model) | £60–400 | Complete | Complete |

The headline observation from this table is not that any single option is universally correct—it is that the decision space is far wider than most organisations appreciate. The default assumption that AI capability requires paying frontier API prices is simply wrong for a large proportion of practical use cases.

The inflection point at which self-hosting becomes economically rational versus a hosted open source API is relatively modest usage. The inflection point at which owned hardware beats cloud hosting is higher, but not unreachably so for organisations with stable, predictable workloads. And crucially, all of the economically attractive options below the frontier commercial API tier are open models.

The closed commercial providers are, in effect, charging a substantial premium for frontier capability and the convenience of a managed service. For applications where frontier capability is genuinely necessary—the hardest reasoning tasks, the most nuanced language generation—that premium may be justified. But for the much larger class of applications where a well-tuned open model is competitive, it amounts to paying significantly more for less control, less transparency, and a permanent external dependency.

## The Counterarguments

It would be unfair not to acknowledge the genuine strengths of the closed commercial approach.

Frontier capability still largely sits with the closed labs. As of early 2026, the most capable models on the most demanding benchmarks remain those produced by OpenAI, Anthropic, and Google. The sheer computational resources these organisations can deploy—and the engineering talent they can attract—means that the absolute frontier of AI capability is still, for now, behind closed doors.

Safety and alignment research is genuinely hard, and it benefits from coordination. There are reasonable arguments that releasing highly capable models openly, before robust alignment techniques are well understood, creates risks that are difficult to manage once models are in the wild. Raymond's "given enough eyeballs" principle works wonderfully for finding bugs in a web browser. Its applicability to preventing the misuse of a highly capable reasoning system is rather less certain.

And the economics of training foundation models remain formidable. The open source AI ecosystem mostly fine-tunes and adapts models that were originally built with enormous commercial or governmental resources. A fully community-funded effort to train a truly frontier model from scratch has not yet materialised, though organisations like EleutherAI have made impressive attempts. The bazaar is excellent at building on foundations; it is less clear that it can consistently lay them.

## History as a Guide

But history suggests we should not underestimate the bazaar.

Linux was once dismissed as a hobbyist toy, unsuitable for serious enterprise use. Today it runs the vast majority of the world's servers, cloud infrastructure, and mobile devices. Apache, MySQL, Python, and countless other open source projects followed similar trajectories—marginalised initially, then central, then simply assumed.

The pattern tends to follow a characteristic arc. A commercial entity builds something genuinely new and powerful, protected by proprietary advantage. The open source community begins to replicate and then iterate upon it. The gap in capability narrows. At some point the open version becomes "good enough" for most use cases—and when it does, the dynamics shift dramatically, because the open version is not just competitive on capability but overwhelmingly superior on cost, flexibility, and trust.

We may be approaching that inflection point in AI. For many practical applications—customer service automation, document summarisation, code assistance, content generation—open models already offer competitive performance at dramatically lower cost. The remaining gaps are narrowing month by month.

## What This Means for the Future

If the trajectory of the bazaar holds, we should expect several things.

The centre of gravity in AI development will shift progressively toward the open ecosystem. Commercial models will continue to push the absolute frontier of capability, but their practical advantage over open alternatives will shrink until it matters only for the most demanding applications. The vast middle ground—the enormous range of legitimate, valuable AI applications that don't require frontier capability—will be increasingly dominated by open models.

Power will be distributed rather than concentrated. Today, a small number of companies control access to the most capable AI systems. In a world where open models are competitive, that control evaporates. This is profoundly consequential—for competition, for regulation, for national security, and for the simple question of who gets to benefit from AI capability.

Trust and accountability will improve. It is very difficult to hold a closed system accountable. When you cannot see inside it, you cannot verify its claims, audit its behaviour, or understand its failures. Open models, precisely because they are open, are auditable. This matters enormously as AI systems take on roles in healthcare, finance, legal systems, and public administration.

And innovation will accelerate. Raymond was right about this twenty-eight years ago, and the principle has only become more powerful in a world of global connectivity and collaborative tooling. The best ideas in AI will increasingly come not from any single lab, however well-resourced, but from the collective intelligence of a global community of researchers, engineers, and practitioners who can build on each other's work.

## A Bazaar Worth Building

The open source AI movement is not without its own tensions and contradictions. Questions about what "open" actually means—whether releasing weights without training data or code is genuinely open—are live and contested. The relationship between open models and the safety concerns of the alignment community is unresolved. And the structural challenge of funding the enormous compute required to train foundation models remains.

But these are solvable problems, and the community is actively working on them. The alternative—allowing the most powerful technology in human history to remain the exclusive province of a handful of commercial laboratories, accountable primarily to their investors—carries its own profound risks.

Eric Raymond ended *The Cathedral and the Bazaar* with an observation that has aged remarkably well: "Perhaps in the end the open-source culture will triumph not because cooperation is morally right or software is ideologically special, but simply because the closed-source world cannot win an evolutionary arms race with communities that can put orders of magnitude more skilled time into a problem."

The cathedral builders of the AI era are impressive. Their resources are extraordinary and their achievements are real. But the bazaar is vast, it is growing, and it is learning fast.

History suggests you should not bet against it.
