# awesome-agent-skills

> A curated list of awesome Agent Skills for extending AI coding assistants.
> 精选的 Agent Skills 列表，用于扩展 AI 编程助手。
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

### Development / 开发工具

| Skill | Description | Source |
|-------|-------------|--------|
| [test-driven-development](https://github.com/obra/skills) | Write tests before implementing code with TDD workflow | [obra/skills](https://github.com/obra/skills) |
| [debugging](https://github.com/obra/skills) | Systematic debugging strategies and techniques | [obra/skills](https://github.com/obra/skills) |
| [code-review](https://github.com/obra/skills) | Review code changes using team standards and best practices | [obra/skills](https://github.com/obra/skills) |
| [refactoring](https://github.com/obra/skills) | Restructure existing code without changing behavior | [obra/skills](https://github.com/obra/skills) |
| [api-design](https://github.com/obra/skills) | Design RESTful APIs with best practices | [obra/skills](https://github.com/obra/skills) |
| [clean-architecture](https://github.com/obra/skills) | Implement clean architecture patterns in projects | [obra/skills](https://github.com/obra/skills) |
| [design-patterns](https://github.com/obra/skills) | Apply Gang of Four design patterns appropriately | [obra/skills](https://github.com/obra/skills) |

### Git & Version Control / Git 版本控制

| Skill | Description | Source |
|-------|-------------|--------|
| [commit-helper](https://github.com/anthropics/skills) | Generate clear, conventional Git commit messages | [anthropics/skills](https://github.com/anthropics/skills) |
| [git-release](https://github.com/Vercel/cli) | Create consistent releases and changelogs from merged PRs | [Vercel/cli](https://github.com/Vercel/cli) |
| [pr-review](https://github.com/obra/skills) | Review Pull Requests using team standards | [obra/skills](https://github.com/obra/skills) |
| [branch-strategy](https://github.com/obra/skills) | Implement Git branching strategies (GitFlow, trunk-based) | [obra/skills](https://github.com/obra/skills) |
| [git-workflow](https://github.com/obra/skills) | Optimize Git workflow for team collaboration | [obra/skills](https://github.com/obra/skills) |

### Testing / 测试

| Skill | Description | Source |
|-------|-------------|--------|
| [webapp-testing](https://github.com/anthropics/skills) | Test local web applications using Playwright | [anthropics/skills](https://github.com/anthropics/skills) |
| [unit-testing](https://github.com/obra/skills) | Write comprehensive unit tests for code coverage | [obra/skills](https://github.com/obra/skills) |
| [integration-testing](https://github.com/obra/skills) | Test integration between system components | [obra/skills](https://github.com/obra/skills) |
| [e2e-testing](https://github.com/obra/skills) | End-to-end testing for user flows | [obra/skills](https://github.com/obra/skills) |

### React & Frontend / React 前端

| Skill | Description | Source |
|-------|-------------|--------|
| [react-best-practices](https://github.com/vercel-labs/agent-skills) | React and Next.js best practices, 40+ performance rules | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| [web-design-guidelines](https://github.com/vercel-labs/agent-skills) | Web design best practices, 100+ modern guidelines | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| [react-hooks](https://github.com/obra/skills) | Use React Hooks effectively with patterns | [obra/skills](https://github.com/obra/skills) |
| [state-management](https://github.com/obra/skills) | Implement state management (Redux, Zustand, Jotai) | [obra/skills](https://github.com/obra/skills) |
| [component-design](https://github.com/obra/skills) | Design reusable React component libraries | [obra/skills](https://github.com/obra/skills) |
| [performance-optimization](https://github.com/obra/skills) | Optimize React app performance | [obra/skills](https://github.com/obra/skills) |

### Mobile Development / 移动开发

| Skill | Description | Source |
|-------|-------------|--------|
| [react-native-best-practices](https://github.com/callstackincubator/agent-skills) | React Native performance optimization guidelines | [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills) |
| [expo-app-design](https://github.com/expo/expo) | Design and build Expo applications | [expo/expo](https://github.com/expo/expo) |
| [expo-deployment](https://github.com/expo/expo) | Deploy Expo apps to production stores | [expo/expo](https://github.com/expo/expo) |
| [upgrading-expo](https://github.com/expo/expo) | Upgrade Expo SDK versions safely | [expo/expo](https://github.com/expo/expo) |

### DevOps & Deployment / 运维部署

| Skill | Description | Source |
|-------|-------------|--------|
| [vercel-deploy-claimable](https://github.com/vercel-labs/agent-skills) | One-click deployment to Vercel platform | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| [docker-setup](https://github.com/obra/skills) | Set up Docker containers for applications | [obra/skills](https://github.com/obra/skills) |
| [ci-cd-pipeline](https://github.com/obra/skills) | Create CI/CD pipelines with GitHub Actions | [obra/skills](https://github.com/obra/skills) |
| [infrastructure-as-code](https://github.com/obra/skills) | Define infrastructure with Terraform/Pulumi | [obra/skills](https://github.com/obra/skills) |

### Documentation / 文档

| Skill | Description | Source |
|-------|-------------|--------|
| [docx](https://github.com/anthropics/skills) | Create, edit, and analyze Word documents with tracked changes | [anthropics/skills](https://github.com/anthropics/skills) |
| [pdf](https://github.com/anthropics/skills) | Extract text/tables, create PDFs, merge/split, handle forms | [anthropics/skills](https://github.com/anthropics/skills) |
| [pptx](https://github.com/anthropics/skills) | Create, edit, and analyze PowerPoint presentations | [anthropics/skills](https://github.com/anthropics/skills) |
| [xlsx](https://github.com/anthropics/skills) | Create, edit, and analyze Excel spreadsheets with formulas | [anthropics/skills](https://github.com/anthropics/skills) |
| [technical-writing](https://github.com/obra/skills) | Write clear technical documentation | [obra/skills](https://github.com/obra/skills) |
| [api-documentation](https://github.com/obra/skills) | Generate API documentation from code | [obra/skills](https://github.com/obra/skills) |

### Data & Science / 数据科学

| Skill | Description | Source |
|-------|-------------|--------|
| [data-analysis](https://github.com/obra/skills) | Perform data analysis with pandas and numpy | [obra/skills](https://github.com/obra/skills) |
| [data-visualization](https://github.com/obra/skills) | Create data visualizations with matplotlib/plotly | [obra/skills](https://github.com/obra/skills) |
| [machine-learning](https://github.com/obra/skills) | Build and train ML models with scikit-learn | [obra/skills](https://github.com/obra/skills) |

### Design & Creative / 设计创意

| Skill | Description | Source |
|-------|-------------|--------|
| [algorithmic-art](https://github.com/anthropics/skills) | Create generative art using p5.js with seeded randomness | [anthropics/skills](https://github.com/anthropics/skills) |
| [canvas-design](https://github.com/anthropics/skills) | Design visual art in PNG and PDF formats | [anthropics/skills](https://github.com/anthropics/skills) |
| [brand-guidelines](https://github.com/anthropics/skills) | Apply brand colors and typography to artifacts | [anthropics/skills](https://github.com/anthropics/skills) |
| [ui-design-systems](https://github.com/obra/skills) | Create consistent UI design systems | [obra/skills](https://github.com/obra/skills) |

### MCP Integration / MCP 集成

| Skill | Description | Source |
|-------|-------------|--------|
| [mcp-builder](https://github.com/anthropics/skills) | Create MCP servers to integrate external APIs and services | [anthropics/skills](https://github.com/anthropics/skills) |
| [mcp-client](https://github.com/obra/skills) | Connect AI agents to MCP servers | [obra/skills](https://github.com/obra/skills) |

### Security / 安全

| Skill | Description | Source |
|-------|-------------|--------|
| [security-audit](https://github.com/obra/skills) | Perform security audits on codebases | [obra/skills](https://github.com/obra/skills) |
| [dependency-check](https://github.com/obra/skills) | Check dependencies for vulnerabilities | [obra/skills](https://github.com/obra/skills) |
| [authentication](https://github.com/obra/skills) | Implement secure authentication (OAuth, JWT) | [obra/skills](https://github.com/obra/skills) |

### Workflow & Automation / 工作流自动化

| Skill | Description | Source |
|-------|-------------|--------|
| [task-automation](https://github.com/obra/skills) | Automate repetitive development tasks | [obra/skills](https://github.com/obra/skills) |
| [file-organization](https://github.com/obra/skills) | Organize project files and directories | [obra/skills](https://github.com/obra/skills) |
| [code-generation](https://github.com/obra/skills) | Generate boilerplate code efficiently | [obra/skills](https://github.com/obra/skills) |

### Database / 数据库

| Skill | Description | Source |
|-------|-------------|--------|
| [sql-queries](https://github.com/obra/skills) | Write optimized SQL queries | [obra/skills](https://github.com/obra/skills) |
| [database-design](https://github.com/obra/skills) | Design normalized database schemas | [obra/skills](https://github.com/obra/skills) |
| [orm-usage](https://github.com/obra/skills) | Use ORMs (Prisma, TypeORM, SQLAlchemy) effectively | [obra/skills](https://github.com/obra/skills) |
| [migration-management](https://github.com/obra/skills) | Manage database migrations safely | [obra/skills](https://github.com/obra/skills) |

### Community Skills / 社区精选

| Skill | Author | Description |
|-------|--------|-------------|
| [baoyu-skills](https://github.com/baoyuto/skills) | @baoyuto | 宝玉老师自用 Skills（自动发公众号等） |
| [planning-with-files](https://github.com/different-planet/skills) | @different-planet | 使用文件规划实现 Manus 效果 |
| [skill-prompt-generator](https://github.com/prompt-engineer/skills) | @prompt-engineer | 从现有代码生成 Skill 提示词 |
| [claude-scientific-skills](https://github.com/scientist/skills) | @scientist | 128+ 科研技能（生物、化学、ML） |
| [ui-ux-pro-max](https://github.com/designer/skills) | @designer | UI/UX 设计 Skills 集合 |

---

## Development Tools / 开发工具

| Tool | Description | Link |
|------|-------------|------|
| **skillport** | Validate, manage, and serve skills at scale | [gotalab/skillport](https://github.com/gotalab/skillport) |
| **add-skill** | CLI installer from Vercel | `npx add-skill` |

---

## Installation / 安装方式

### Claude Code

```bash
# Project level / 项目级别
.claude/skills/<skill-name>/SKILL.md

# User level / 用户级别
~/.claude/skills/<skill-name>/SKILL.md
```

### OpenCode

```bash
# Project level / 项目级别
.opencode/skills/<skill-name>/SKILL.md

# User level / 用户级别
~/.config/opencode/skills/<skill-name>/SKILL.md
```

### Cursor

```bash
# Project level / 项目级别
.cursor/skills/<skill-name>/SKILL.md

# User level / 用户级别
~/.cursor/skills/<skill-name>/SKILL.md
```

---

## Learning Resources / 学习资源

### 官方教程 / Official Tutorials

- 🎓 [Claude Code Skills 完整指南](https://code.claude.com/docs/en/skills) - Anthropic 官方文档
- 🎓 [OpenCode Skills 集成文档](https://opencode.ai/docs/skills/) - OpenCode 官方指南
- 🎓 [Agent Skills 技术协议](https://modelscope.cn/learn/2558) - 中文技术深度解析

### 社区教程 / Community Tutorials

来自 **libukai/awesome-agent-skills** 中文教程合集：

#### 喂饭教程
- @一泽 Eze：Agent Skills 终极指南：入门、精通、预测
- @数字生命卡兹克：一文带你看懂 Skills
- @王树义：AI 从「嘴替」升级成「打工人」

#### 进阶教程
- @宝玉：五步框架把 Workflow 变成可进化的 Skill
- @歸藏：带动效的 PPT 生成 Agent
- @李不凯正在研究：Cherry Studio 最佳实践

#### 深度分析
- @凡人小北：Skills vs MCP 的区别
- @deeptoai：Claude Agent Skills 第一性原理
- @宝玉：Claude Code 的"懒加载"机制

#### 视频教程
- @马克的技术工作坊：Agent Skill 从使用到原理
- @白白说大模型：别再造 Agent 了，未来是 Skills 的
- @01Coder：OpenCode + 智谱 GLM + Agent Skills

---

## Community / 社区

### 讨论区 / Discussion Forums

- 💬 [Anthropic Community](https://community.anthropic.com/)
- 💬 [r/ClaudeAI](https://reddit.com/r/ClaudeAI/) - Reddit
- 💬 [r/Cline](https://reddit.com/r/Cline/) - Cline 社区
- 💬 [Cursor Discord](https://discord.gg/cursor) - Cursor 官方 Discord
- 💬 [OpenCode Discord](https://discord.gg/opencode) - OpenCode 社区

### 贡献指南 / Contributing

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

**贡献方式**：
1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-skill`)
3. 提交更改 (`git commit -m 'Add amazing skill'`)
4. 推送到分支 (`git push origin feature/amazing-skill`)
5. 创建 Pull Request

**贡献规范**：
- 每个 Skill 必须包含 SKILL.md 文件
- 提供清晰的说明和示例
- 遵循现有格式和风格
- 添加中英文双语描述

---

## SKILL.md 模板 / SKILL.md Template

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

## What it does / 功能说明

This skill helps you...

## How to use / 使用方法

1. Step one
2. Step two

## Examples / 示例

\`\`\`typescript
// Example usage
\`\`\`

## Requirements / 要求

- Node.js 18+
- Claude Code 0.6+

## Resources / 资源

- [Documentation](https://example.com)
- [GitHub](https://github.com/example/skill)
```

---

## Stats / 统计

- **Total Skills**: 150+
- **Official Skills**: 16 (Anthropic: 10, Vercel Labs: 3, Expo: 3)
- **Community Skills**: 135+
- **Categories**: 15 (Development, Git, Testing, React, Mobile, DevOps, Documentation, Data, Design, MCP, Security, Workflow, Database, Creative)
- **Last Updated**: 2026-01-18

---

## 🔗 Related Projects / 相关项目

- [awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) - MCP 服务器列表
- [awesome-ai-coding-tools](https://github.com/ai-for-developers/awesome-ai-coding-tools) - AI 编程工具列表
- [openskills](https://github.com/numman-ali/openskills) - 通用 Skills 加载器
- [MCP Market](https://mcpmarket.com) - MCP 服务器市场

---

## 🌐 More Resources / 更多资源

更多 AI 编程资源和教程，请访问：[五行代码博客](https://blog.wuxingcodes.com/)

---

## License / 许可证

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [大熊掌门 (MaesHughes)](https://github.com/MaesHughes) has waived all copyright and related or neighboring rights to this work.

---

## Stargazers over time / 星标增长趋势

[![Stargazers over time](https://api.star-history.com/svg?repos=MaesHughes/awesome-agent-skills&type=Date)](https://star-history.com/#MaesHughes/awesome-agent-skills&Date)

---

**⭐ 如果这个项目对你有帮助，请给一个 Star！/ If this project helps you, please give it a star!**

**💡 由 [大熊掌门 (MaesHughes)](https://github.com/MaesHughes) 维护 / Maintained by [大熊掌门]**

**🌐 博客 / Blog**: [五行代码](https://blog.wuxingcodes.com/)
