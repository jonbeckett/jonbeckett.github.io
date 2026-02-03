---
name: Writing Style Guidelines
description: Voice, tone, structure, and content standards for jonbeckett.com blog posts including narrative style, technical depth requirements, and content organization
---

# Writing Style and Content Guidelines

This skill defines the voice, tone, structure, and content standards for jonbeckett.com blog posts.

## Voice and Tone

- **Perspective**: First person plural ("we") or third person analytical
- **Tone**: Professional but accessible, technical yet readable
- **Style**: Narrative-driven with technical depth
- **Balance**: Blend storytelling with technical analysis

## Content Depth and Length

- **Target Length**: 2,000-5,000+ words for substantive posts
- **Comprehensiveness**: Provide comprehensive coverage from multiple angles
- **Historical Context**: Include evolution and background where relevant
- **Practical Applications**: Offer real-world examples and implementations
- **Forward-Looking**: Present future implications and emerging trends
- **Evidence-Based**: Support arguments with specific examples and data

## Content Structure

1. **Opening Hook**: Start with a compelling scenario or observation
2. **Historical Context**: Often includes technology evolution and history
3. **Technical Deep Dive**: Detailed explanations with code/architecture examples
4. **Practical Applications**: Real-world implications and use cases
5. **Future Outlook**: Forward-looking analysis and predictions

## Technical Writing Standards

- Use code blocks with proper syntax highlighting (```language)
- Include detailed technical explanations when discussing concepts
- Reference specific technologies, companies, and products accurately
- Provide architectural context for technical decisions
- Include performance implications and trade-offs
- Use proper Markdown formatting throughout

## Stylistic Patterns

- Often references science fiction (Blade Runner, Philip K. Dick) for metaphorical context
- Uses vivid, sometimes poetic language alongside technical precision
- Employs section headers with descriptive, engaging titles
- Includes historical timelines and evolution of technologies
- Balances optimism with critical analysis

## Markdown Formatting Standards

- Use `##` for main sections (H2)
- Use `###` for subsections (H3)
- Use `####` sparingly for sub-subsections
- Emphasis: `**bold**` for strong emphasis, `*italic*` for subtle emphasis
- Code: `` `inline code` `` for commands, variables, file names
- Lists: Use `-` for unordered lists, maintain consistent indentation
- Links: Use descriptive link text, not "click here"

### List vs. Paragraph Formatting (CRITICAL)

- **ALWAYS use bullet lists when presenting multiple related points, especially when each starts with a bold term.**

❌ **Wrong** - Multiple paragraphs with bold lead-ins:
```markdown
**Performance**: The system handles thousands of requests per second with minimal latency.

**Scalability**: Horizontal scaling allows for unlimited growth potential.

**Reliability**: Built-in redundancy ensures 99.99% uptime guarantees.
```

✅ **Correct** - Use bullet lists for series of related points:
```markdown
- **Performance**: The system handles thousands of requests per second with minimal latency
- **Scalability**: Horizontal scaling allows for unlimited growth potential  
- **Reliability**: Built-in redundancy ensures 99.99% uptime guarantees
```

### When to Use Lists vs. Paragraphs

**Use bullet lists for**:
- Multiple related points or concepts
- Features, benefits, or characteristics
- Step-by-step processes (consider numbered lists)
- Any series starting with bold terms or key phrases
- Comparisons or contrasting elements

**Use paragraphs for**:
- Narrative explanations and storytelling
- Detailed analysis requiring multiple sentences
- Flowing, connected thoughts
- Historical context and evolution
- Complex technical explanations

## Common Writing Patterns

### Opening Paragraph Pattern
Start with an engaging scenario or observation that sets up the topic:
```markdown
In the sprawling headquarters of a Fortune 500 company, something remarkable 
is happening. Hundreds of AI agents are working around the clock...
```

### Historical Context Pattern
Include evolution and historical perspective:
```markdown
## The Promethean Fire: Turing's Vision (1940s-1950s)

In 1950, Alan Turing published a paper that would echo through decades...
```

### Technical Explanation Pattern
Provide deep technical detail with context:
```markdown
The breakthrough came with brute force tree searching—the computer equivalent 
of exploring every possible future simultaneously. But the real algorithmic 
revolution was alpha-beta pruning...
```

### Code Example Pattern
When including code, provide context and explanation:
```markdown
The implementation relies on TypeScript's type system:

```typescript
interface AgentConfig {
  name: string;
  capabilities: string[];
  model: ModelType;
}
```

This approach ensures type safety while maintaining flexibility...
```

## Author Context

Jonathan Beckett is a software/web developer with expertise in:
- Microsoft ecosystem (document/content management, PowerShell, Power Automate)
- Modern JavaScript/TypeScript development
- BDD with Cucumber/Gherkin
- Web automation with Playwright
- DevOps and pipeline optimization
- Linux and open source software background
- Creator of early blogging platform

When suggesting content or code examples, draw from these areas of expertise while maintaining the established writing style.