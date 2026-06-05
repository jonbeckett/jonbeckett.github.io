# Continue Project Rules

This repository uses local Continue rules in `.continue/rules` to provide skills-like behaviour.

## Included Rules

- `01-project-workflow.md`: baseline task execution and safety guardrails.
- `02-british-english.md`: UK spelling and language standards for content.
- `03-blog-post-authoring.md`: post naming, front matter, and writing structure checks.
- `04-jekyll-site-operations.md`: Jekyll and GitHub Pages compatibility safeguards.
- `05-front-matter-enforcement.md`: always-on required front matter and Unsplash attribution checks for posts.

## How They Are Applied

- Rules are discovered from `.continue/rules`.
- Rules with `alwaysApply: true` are always in scope.
- Rules with `globs` are applied when related files are in context.

## Internet Research (MCP)

- Web research is enabled via `.continue/mcpServers/web-research.yaml`.
- This uses Playwright MCP and is available in Agent mode.
- Requirement: Node.js and `npx` must be available on PATH.
- Usage: ask the agent to research a subject and gather sources; the model can open and read live web pages via tool calls.

## Source Alignment

These rules are aligned to the existing Copilot skills under `.github/skills`:

- `blog-post-author`
- `content-editor`
- `web-developer`
