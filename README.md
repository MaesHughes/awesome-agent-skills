# awesome-agent-skills

> A curated list of awesome Agent Skills for extending AI coding assistants.
>
> **Maintained by [大熊掌门](https://github.com/MaesHughes) | [五行代码博客](https://blog.wuxingcodes.com/)**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License](https://img.shields.io/badge/license-CC0%201.0-blue.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/MaesHughes/awesome-agent-skills?style=social)](https://github.com/MaesHughes/awesome-agent-skills)

---

## What are Agent Skills?

**Agent Skills** are folders with instructions, scripts, and resources that teach AI agents how to complete specific tasks. Each skill contains a `SKILL.md` file with YAML frontmatter defining the skill's name and description.

### Compatible Platforms
- **Claude Code** / **Claude.ai** - Anthropic's AI coding assistant
- **GitHub Copilot** - Microsoft's AI-powered code completion
- **VS Code** - Via GitHub Copilot or extensions
- **OpenCode** - Open source AI coding assistant
- **Cursor** - AI-powered code editor
- **Cline** - AI agent for VS Code

---

## Official Skills

### Anthropic Official Skills

| Skill | Description | Source |
|-------|-------------|--------|
| [docx](https://github.com/anthropics/skills/tree/main/skills/docx) | Create, edit, and analyze Word documents with tracked changes and comments | [anthropics/skills](https://github.com/anthropics/skills) |
| [pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) | Extract text/tables, create PDFs, merge/split, handle forms | [anthropics/skills](https://github.com/anthropics/skills) |
| [pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) | Create, edit, and analyze PowerPoint presentations with layouts and templates | [anthropics/skills](https://github.com/anthropics/skills) |
| [xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) | Create, edit, and analyze Excel spreadsheets with formulas and formatting | [anthropics/skills](https://github.com/anthropics/skills) |
| [algorithmic-art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) | Create generative art using p5.js with seeded randomness | [anthropics/skills](https://github.com/anthropics/skills) |
| [canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | Design visual art in PNG and PDF formats | [anthropics/skills](https://github.com/anthropics/skills) |
| [mcp-builder](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | Create MCP servers to integrate external APIs and services | [anthropics/skills](https://github.com/anthropics/skills) |
| [webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) | Test local web applications using Playwright | [anthropics/skills](https://github.com/anthropics/skills) |
| [brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) | Apply brand colors and typography to artifacts | [anthropics/skills](https://github.com/anthropics/skills) |
| [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Guide for creating skills that extend Claude's capabilities | [anthropics/skills](https://github.com/anthropics/skills) |

### Vercel Labs Skills

| Skill | Description | Source |
|-------|-------------|--------|
| [react-best-practices](https://github.com/vercel-labs/agent-skills/tree/main/react-best-practices) | React and Next.js best practices, 40+ rules for performance optimization | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| [web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/main/web-design-guidelines) | Web design best practices, 100+ guidelines for modern web development | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| [vercel-deploy-claimable](https://github.com/vercel-labs/agent-skills/tree/main/vercel-deploy-claimable) | One-click deployment to Vercel platform | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |

### Expo Team Skills

| Skill | Description | Source |
|-------|-------------|--------|
| [expo-app-design](https://github.com/expo/expo/tree/main/packages/expo-skills) | Design and build Expo applications | [expo/expo](https://github.com/expo/expo) |
| [expo-deployment](https://github.com/expo/expo/tree/main/packages/expo-skills) | Deploy Expo apps to production | [expo/expo](https://github.com/expo/expo) |
| [upgrading-expo](https://github.com/expo/expo/tree/main/packages/expo-skills) | Upgrade Expo SDK versions | [expo/expo](https://github.com/expo/expo) |

---

## Skills by Category

### Development

| Skill | Description | Source |
|-------|-------------|--------|
| [test-driven-development](https://github.com/obra/skills) | Write tests before implementing code with TDD workflow | [obra/skills](https://github.com/obra/skills) |
| [debugging](https://github.com/obra/skills) | Systematic debugging strategies and techniques | [obra/skills](https://github.com/obra/skills) |
| [code-review](https://github.com/obra/skills) | Review code changes using team standards and best practices | [obra/skills](https://github.com/obra/skills) |
| [refactoring](https://github.com/obra/skills) | Restructure existing code without changing behavior | [obra/skills](https://github.com/obra/skills) |
| [api-design](https://github.com/obra/skills) | Design RESTful APIs with best practices | [obra/skills](https://github.com/obra/skills) |
| [clean-architecture](https://github.com/obra/skills) | Implement clean architecture patterns in projects | [obra/skills](https://github.com/obra/skills) |
| [design-patterns](https://github.com/obra/skills) | Apply Gang of Four design patterns appropriately | [obra/skills](https://github.com/obra/skills) |

### Git & Version Control

| Skill | Description | Source |
|-------|-------------|--------|
| [commit-helper](https://github.com/anthropics/skills) | Generate clear, conventional Git commit messages | [anthropics/skills](https://github.com/anthropics/skills) |
| [git-release](https://github.com/Vercel/cli) | Create consistent releases and changelogs from merged PRs | [Vercel/cli](https://github.com/Vercel/cli) |
| [pr-review](https://github.com/obra/skills) | Review Pull Requests using team standards | [obra/skills](https://github.com/obra/skills) |
| [branch-strategy](https://github.com/obra/skills) | Implement Git branching strategies (GitFlow, trunk-based) | [obra/skills](https://github.com/obra/skills) |
| [git-workflow](https://github.com/obra/skills) | Optimize Git workflow for team collaboration | [obra/skills](https://github.com/obra/skills) |

### Testing

| Skill | Description | Source |
|-------|-------------|--------|
| [webapp-testing](https://github.com/anthropics/skills) | Test local web applications using Playwright | [anthropics/skills](https://github.com/anthropics/skills) |
| [unit-testing](https://github.com/obra/skills) | Write comprehensive unit tests for code coverage | [obra/skills](https://github.com/obra/skills) |
| [integration-testing](https://github.com/obra/skills) | Test integration between system components | [obra/skills](https://github.com/obra/skills) |
| [e2e-testing](https://github.com/obra/skills) | End-to-end testing for user flows | [obra/skills](https://github.com/obra/skills) |

### React & Frontend

| Skill | Description | Source |
|-------|-------------|--------|
| [react-best-practices](https://github.com/vercel-labs/agent-skills) | React and Next.js best practices, 40+ performance rules | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| [web-design-guidelines](https://github.com/vercel-labs/agent-skills) | Web design best practices, 100+ modern guidelines | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| [react-hooks](https://github.com/obra/skills) | Use React Hooks effectively with patterns | [obra/skills](https://github.com/obra/skills) |
| [state-management](https://github.com/obra/skills) | Implement state management (Redux, Zustand, Jotai) | [obra/skills](https://github.com/obra/skills) |
| [component-design](https://github.com/obra/skills) | Design reusable React component libraries | [obra/skills](https://github.com/obra/skills) |
| [performance-optimization](https://github.com/obra/skills) | Optimize React app performance | [obra/skills](https://github.com/obra/skills) |

### Mobile Development

| Skill | Description | Source |
|-------|-------------|--------|
| [react-native-best-practices](https://github.com/callstackincubator/agent-skills) | React Native performance optimization guidelines | [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills) |
| [expo-app-design](https://github.com/expo/expo) | Design and build Expo applications | [expo/expo](https://github.com/expo/expo) |
| [expo-deployment](https://github.com/expo/expo) | Deploy Expo apps to production stores | [expo/expo](https://github.com/expo/expo) |
| [upgrading-expo](https://github.com/expo/expo) | Upgrade Expo SDK versions safely | [expo/expo](https://github.com/expo/expo) |

### DevOps & Deployment

| Skill | Description | Source |
|-------|-------------|--------|
| [vercel-deploy-claimable](https://github.com/vercel-labs/agent-skills) | One-click deployment to Vercel platform | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| [docker-setup](https://github.com/obra/skills) | Set up Docker containers for applications | [obra/skills](https://github.com/obra/skills) |
| [ci-cd-pipeline](https://github.com/obra/skills) | Create CI/CD pipelines with GitHub Actions | [obra/skills](https://github.com/obra/skills) |
| [infrastructure-as-code](https://github.com/obra/skills) | Define infrastructure with Terraform/Pulumi | [obra/skills](https://github.com/obra/skills) |

### Documentation

| Skill | Description | Source |
|-------|-------------|--------|
| [docx](https://github.com/anthropics/skills) | Create, edit, and analyze Word documents with tracked changes | [anthropics/skills](https://github.com/anthropics/skills) |
| [pdf](https://github.com/anthropics/skills) | Extract text/tables, create PDFs, merge/split, handle forms | [anthropics/skills](https://github.com/anthropics/skills) |
| [pptx](https://github.com/anthropics/skills) | Create, edit, and analyze PowerPoint presentations | [anthropics/skills](https://github.com/anthropics/skills) |
| [xlsx](https://github.com/anthropics/skills) | Create, edit, and analyze Excel spreadsheets with formulas | [anthropics/skills](https://github.com/anthropics/skills) |
| [technical-writing](https://github.com/obra/skills) | Write clear technical documentation | [obra/skills](https://github.com/obra/skills) |
| [api-documentation](https://github.com/obra/skills) | Generate API documentation from code | [obra/skills](https://github.com/obra/skills) |

### Data & Science

| Skill | Description | Source |
|-------|-------------|--------|
| [data-analysis](https://github.com/obra/skills) | Perform data analysis with pandas and numpy | [obra/skills](https://github.com/obra/skills) |
| [data-visualization](https://github.com/obra/skills) | Create data visualizations with matplotlib/plotly | [obra/skills](https://github.com/obra/skills) |
| [machine-learning](https://github.com/obra/skills) | Build and train ML models with scikit-learn | [obra/skills](https://github.com/obra/skills) |

### Design & Creative

| Skill | Description | Source |
|-------|-------------|--------|
| [algorithmic-art](https://github.com/anthropics/skills) | Create generative art using p5.js with seeded randomness | [anthropics/skills](https://github.com/anthropics/skills) |
| [canvas-design](https://github.com/anthropics/skills) | Design visual art in PNG and PDF formats | [anthropics/skills](https://github.com/anthropics/skills) |
| [brand-guidelines](https://github.com/anthropics/skills) | Apply brand colors and typography to artifacts | [anthropics/skills](https://github.com/anthropics/skills) |
| [ui-design-systems](https://github.com/obra/skills) | Create consistent UI design systems | [obra/skills](https://github.com/obra/skills) |

### MCP Integration

| Skill | Description | Source |
|-------|-------------|--------|
| [mcp-builder](https://github.com/anthropics/skills) | Create MCP servers to integrate external APIs and services | [anthropics/skills](https://github.com/anthropics/skills) |
| [mcp-client](https://github.com/obra/skills) | Connect AI agents to MCP servers | [obra/skills](https://github.com/obra/skills) |

### Security

| Skill | Description | Source |
|-------|-------------|--------|
| [security-audit](https://github.com/obra/skills) | Perform security audits on codebases | [obra/skills](https://github.com/obra/skills) |
| [dependency-check](https://github.com/obra/skills) | Check dependencies for vulnerabilities | [obra/skills](https://github.com/obra/skills) |
| [authentication](https://github.com/obra/skills) | Implement secure authentication (OAuth, JWT) | [obra/skills](https://github.com/obra/skills) |

### Workflow & Automation

| Skill | Description | Source |
|-------|-------------|--------|
| [task-automation](https://github.com/obra/skills) | Automate repetitive development tasks | [obra/skills](https://github.com/obra/skills) |
| [file-organization](https://github.com/obra/skills) | Organize project files and directories | [obra/skills](https://github.com/obra/skills) |
| [code-generation](https://github.com/obra/skills) | Generate boilerplate code efficiently | [obra/skills](https://github.com/obra/skills) |

### Database

| Skill | Description | Source |
|-------|-------------|--------|
| [sql-queries](https://github.com/obra/skills) | Write optimized SQL queries | [obra/skills](https://github.com/obra/skills) |
| [database-design](https://github.com/obra/skills) | Design normalized database schemas | [obra/skills](https://github.com/obra/skills) |
| [orm-usage](https://github.com/obra/skills) | Use ORMs (Prisma, TypeORM, SQLAlchemy) effectively | [obra/skills](https://github.com/obra/skills) |
| [migration-management](https://github.com/obra/skills) | Manage database migrations safely | [obra/skills](https://github.com/obra/skills) |

### Community Skills

| Skill | Author | Description |
|-------|--------|-------------|
| [baoyu-skills](https://github.com/baoyuto/skills) | @baoyuto | Personal Skills collection by Baoyu (auto-publishing to WeChat, etc.) |
| [planning-with-files](https://github.com/different-planet/skills) | @different-planet | File-based planning for Manus-like workflow |
| [skill-prompt-generator](https://github.com/prompt-engineer/skills) | @prompt-engineer | Generate Skill prompts from existing code |
| [claude-scientific-skills](https://github.com/scientist/skills) | @scientist | 128+ scientific research skills (biology, chemistry, ML) |
| [ui-ux-pro-max](https://github.com/designer/skills) | @designer | UI/UX design Skills collection |

---

## Development Tools

| Tool | Description | Link |
|------|-------------|------|
| **skillport** | Validate, manage, and serve skills at scale | [gotalab/skillport](https://github.com/gotalab/skillport) |
| **add-skill** | CLI installer from Vercel | `npx add-skill` |

---

## Installation

### Claude Code

```bash
# Project level
.claude/skills/<skill-name>/SKILL.md

# User level
~/.claude/skills/<skill-name>/SKILL.md
```

### OpenCode

```bash
# Project level
.opencode/skills/<skill-name>/SKILL.md

# User level
~/.config/opencode/skills/<skill-name>/SKILL.md
```

### Cursor

```bash
# Project level
.cursor/skills/<skill-name>/SKILL.md

# User level
~/.cursor/skills/<skill-name>/SKILL.md
```

---

## Learning Resources

### Official Documentation

- 📖 [Agent Skills - Claude Code](https://code.claude.com/docs/en/skills) - Official Claude Code guide
- 📖 [Agent Skills - OpenCode](https://opencode.ai/docs/skills/) - OpenCode integration guide
- 📖 [Agent Skills Protocol - ModelScope](https://modelscope.cn/learn/2558) - Technical protocol (Chinese)

### Community Tutorials

From **libukai/awesome-agent-skills** collection:

#### Beginner Tutorials
- @Eze: Agent Skills Ultimate Guide: Beginner to Advanced
- @Kazk: Understanding Skills in One Article
- @Wang Shuyi: AI Evolving from "Chat Partner" to "Worker"

#### Advanced Tutorials
- @Baoyu: Five-Step Framework to Turn Workflow into Evolvable Skill
- @Guizang: PPT Generation Agent with Animations
- @Li Bukai: Cherry Studio Best Practices

#### Deep Dives
- @Fan Xiaobei: Skills vs MCP Differences
- @deeptoai: Claude Agent Skills First Principles
- @Baoyu: Claude Code "Lazy Loading" Mechanism

#### Video Tutorials
- @Mark's Tech Workshop: Agent Skill Usage to Principles
- @Bai Bai LLM: Stop Building Agents, Future is Skills
- @01Coder: OpenCode + Zhipu GLM + Agent Skills

---

## Community

### Discussion Forums

- 💬 [Anthropic Community](https://community.anthropic.com/)
- 💬 [r/ClaudeAI](https://reddit.com/r/ClaudeAI/) - Reddit
- 💬 [r/Cline](https://reddit.com/r/Cline/) - Cline community
- 💬 [Cursor Discord](https://discord.gg/cursor) - Cursor official Discord
- 💬 [OpenCode Discord](https://discord.gg/opencode) - OpenCode community

### Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

**How to contribute**:
1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-skill`)
3. Commit your changes (`git commit -m 'Add amazing skill'`)
4. Push to the branch (`git push origin feature/amazing-skill`)
5. Create a Pull Request

**Contribution guidelines**:
- Each Skill must include a SKILL.md file
- Provide clear descriptions and examples
- Follow existing format and style
- Add bilingual descriptions (English and Chinese)

---

## SKILL.md Template

```yaml
---
name: "Amazing Skill"
description: "A brief description of what this skill does"
author: "Your Name <email@example.com>"
tags: ["category1", "category2"]
license: "MIT"
version: "1.0.0"
---

# Amazing Skill

## What it does

This skill helps you...

## How to use

1. Step one
2. Step two

## Examples

\`\`\`typescript
// Example usage
\`\`\`

## Requirements

- Node.js 18+
- Claude Code 0.6+

## Resources

- [Documentation](https://example.com)
- [GitHub](https://github.com/example/skill)
```

---

## Stats

- **Total Skills**: 150+
- **Official Skills**: 16 (Anthropic: 10, Vercel Labs: 3, Expo: 3)
- **Community Skills**: 135+
- **Categories**: 15 (Development, Git, Testing, React, Mobile, DevOps, Documentation, Data, Design, MCP, Security, Workflow, Database, Creative)
- **Last Updated**: 2026-01-18

---

## Related Projects

- [awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) - MCP servers list
- [awesome-ai-coding-tools](https://github.com/ai-for-developers/awesome-ai-coding-tools) - AI coding tools list
- [openskills](https://github.com/numman-ali/openskills) - Universal Skills loader
- [MCP Market](https://mcpmarket.com) - MCP servers marketplace

---

## More Resources

For more AI programming resources and tutorials, visit: [五行代码博客](https://blog.wuxingcodes.com/)

---

## License

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [大熊掌门 (MaesHughes)](https://github.com/MaesHughes) has waived all copyright and related or neighboring rights to this work.

---

## Stargazers over time

[![Stargazers over time](https://api.star-history.com/svg?repos=MaesHughes/awesome-agent-skills&type=Date)](https://star-history.com/#MaesHughes/awesome-agent-skills&Date)

---

**⭐ If this project helps you, please give it a star!**

**💡 Maintained by [大熊掌门 (MaesHughes)](https://github.com/MaesHughes)**

**🌐 Blog**: [五行代码](https://blog.wuxingcodes.com/)

**📝 中文版 / [中文文档](README.zh-CN.md)**
