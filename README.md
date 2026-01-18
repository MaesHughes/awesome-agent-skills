# awesome-agent-skills

> A curated list of awesome Agent Skills, resources, and tools for extending AI coding assistants. / 精选的 Agent Skills 资源列表，用于扩展 AI 编程助手。

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License](https://img.shields.io/badge/license-CC0%201.0-blue.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/daxiong-zhangmen/awesome-agent-skills?style=social)](https://github.com/daxiong-zhangmen/awesome-agent-skills)
[![Contributors](https://img.shields.io/github/contributors/daxiong-zhangmen/awesome-agent-skills)](https://github.com/daxiong-zhangmen/awesome-agent-skills/graphs/contributors)

---

## 📖 简介 / Introduction

**Agent Skills** 是 AI 编程助手的功能扩展标准，由 Anthropic 提出，使用 `SKILL.md` 格式定义。Skills 让 Claude Code、Cline、OpenCode、Cursor 等工具获得专业化能力。

**Agent Skills** is an open standard for extending AI coding assistants, proposed by Anthropic, using the `SKILL.md` format. Skills give specialized capabilities to Claude Code, Cline, OpenCode, Cursor, and more.

---

## 🌟 为什么 Agent Skills 在 2026 年如此重要？/ Why Agent Skills Matter in 2026?

- ✅ **开放标准** - Anthropic、Vercel、Microsoft 等大厂支持 / Open standard backed by major tech companies
- ✅ **跨工具兼容** - 一次编写，多处使用 / Write once, use everywhere
- ✅ **轻量级** - 只是 Markdown + YAML，无需编程 / Lightweight - Just Markdown + YAML
- ✅ **社区驱动** - 快速增长的生态系统 / Community-driven ecosystem
- ✅ **SEO 黄金关键词** - 2026 年最热门的 AI 编程趋势 / Hottest AI coding trend in 2026

---

## 📚 目录 / Contents

- [Official Resources / 官方资源](#official-resources)
- [Development Tools / 开发工具](#development-tools)
- [Skills by Category / 技能分类](#skills-by-category)
  - [Code Generation / 代码生成](#code-generation)
  - [Testing & QA / 测试](#testing--qa)
  - [Documentation / 文档](#documentation)
  - [Deployment / 部署](#deployment)
  - [Database / 数据库](#database)
  - [Security / 安全](#security)
- [Skills by AI Tool / 按工具分类](#skills-by-ai-tool)
  - [Claude Code Skills](#claude-code-skills)
  - [Cline Skills](#cline-skills)
  - [OpenCode Skills](#opencode-skills)
  - [Cursor Skills](#cursor-skills)
- [Learning Resources / 学习资源](#learning-resources)
- [Community / 社区](#community)

---

## 🔥 Featured / 精选

### 官方标准 / Official Standards

| 项目 | Stars | 说明 / Description |
|------|-------|---------------------|
| [anthropics/skills](https://github.com/anthropics/skills) | 官方 | Anthropic 官方 Agent Skills 仓库，16+ 示例 Skills |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 官方 | Vercel Labs 官方 Skills，React/Next.js 最佳实践 |
| [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills) | 官方 | Callstack React Native 优化 Skills |
| [Agent Skills 规范](https://github.com/anthropics/skills/blob/main/spec/agent-skills-spec.md) | 官方 | SKILL.md 技术规范文档 |

### 社区资源 / Community Resources

| 项目 | Stars | 说明 / Description |
|------|-------|---------------------|
| [libukai/awesome-agent-skills](https://github.com/libukai/awesome-agent-skills) | 🔥 | Agent Skills 权威中文指南，教程合集 |
| [gotalab/skillport](https://github.com/gotalab/skillport) | 🔥 | SkillOps 工具包：Validate、Manage、Serve |
| [awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) | 62K+ | MCP 服务器列表（与 Skills 配合使用）|

---

## Official Resources / 官方资源

### 官方文档 / Official Documentation

- 📖 [Agent Skills - Claude Code](https://code.claude.com/docs/en/skills) - Claude Code 官方完整指南
- 📖 [Agent Skills - OpenCode](https://opencode.ai/docs/skills/) - OpenCode Skills 集成文档
- 📖 [Agent Skills 技术协议 - ModelScope](https://modelscope.cn/learn/2558) - 中文技术协议深度解析
- 📖 [SKILL.md 规范](https://github.com/anthropics/skills/blob/main/spec/agent-skills-spec.md) - 官方格式规范

### 官方示例 / Official Examples

- 💡 [example-skills](https://github.com/anthropics/skills/tree/main/examples) - Anthropic 官方示例
- 💡 [vercel-agent-skills](https://github.com/vercel-labs/agent-skills) - Vercel 官方实现

---

## Development Tools / 开发工具

### Skills 开发工具

| 工具 / Tool | 说明 / Description | 链接 / Link |
|------------|-------------------|-------------|
| **skillport** | SkillOps 工具包：验证、管理、服务 / Validate, manage, serve | [GitHub](https://github.com/gotalab/skillport) |
| **add-skill** | Vercel 官方 CLI 安装工具 / CLI installer from Vercel | `npx add-skill` |
| **MCP Developer Tools** | MCP 开发工具套件 / MCP development toolkit | [MCP SDK](https://modelcontextprotocol.io) |

### Skills 商店 / Skills Stores

| 商店 / Store | 特色 / Features | 链接 / Link |
|-------------|----------------|-------------|
| **skillsmp** | 自动抓取 GitHub Skills / Auto-scrape GitHub | Web |
| **SkillStore** | 中文商店 + 安全审计 / Chinese + Security Audit | Web |
| **agent-skills-market** | 开发者分成机制 / Revenue Share | Web |

---

## Skills by Category / 技能分类

### 文档处理 / Document Processing

来自 **anthropics/skills** 官方集合：

- 📄 **docx** - 创建、编辑和分析 Word 文档，支持修订、评论、格式保留
- 📄 **pdf** - PDF 操作工具包，提取文本/表格、创建、合并/拆分、表单处理
- 📄 **pptx** - PowerPoint 演示文稿，支持布局、模板、图表
- 📄 **xlsx** - Excel 电子表格，支持公式、格式、数据分析

### 编程辅助 / Programming Assistance

| Skill | 来源 | 说明 |
|-------|------|------|
| **react-best-practices** | Vercel Labs | React/Next.js 性能优化，40+ 规则 |
| **web-design-guidelines** | Vercel Labs | Web 设计最佳实践，100+ 规则 |
| **react-native-best-practices** | Callstack | React Native 性能优化 |
| **vercel-deploy-claimable** | Vercel Labs | 一键部署到 Vercel |

### 工作流 / Workflows

来自社区优秀 Skills：

- 🔄 **commit-helper** - 生成清晰的 Git commit messages
- 🔄 **pr-review** - 使用团队标准审查 Pull Requests
- 🔄 **code-analysis** - 代码质量分析和报告生成
- 🔄 **git-release** - 创建一致的 releases 和 changelogs

### 产品集成 / Product Integration

| Skill | 产品 | 说明 |
|-------|------|------|
| **dify-skills** | Dify | 多功能 Skills 集合 |
| **n8n-skills** | n8n | 创建 n8n 工作流 |
| **obsidian-skills** | Obsidian | 增强 Obsidian 功能 |
| **huggingface-skills** | HuggingFace | 模型训练和评估 |

### 专业领域 / Specialized

- 🔬 **claude-scientific-skills** - 128+ 科研技能（生物、化学、ML）
- 🎨 **ui-ux-pro-max** - UI/UX 设计 Skills 集合
- 📝 **baoyu-skills** - 宝玉老师自用 Skills（自动发公众号等）
- 🎯 **planning-with-files** - 使用文件规划实现 Manus 效果

---

## Skills by AI Tool / 按工具分类

### Claude Code Skills

Claude Code 官方支持 Agent Skills，位于 `~/.claude/skills/`

**路径规范**：
```
~/.claude/skills/
├── my-skill/
│   ├── SKILL.md          # 技能定义
│   └── resources/        # 附加资源
```

**推荐 Skills**：
- [claude-code-project-memory](https://github.com/example) - 项目记忆系统
- [claude-code-git-helper](https://github.com/example) - Git 操作辅助

### Cline Skills

Cline 3.48+ 支持 Skills，通过 UI 管理

**路径规范**：
```
~/.cline/skills/
├── my-skill/
│   ├── SKILL.md
│   └── resources/
```

**推荐 Skills**：
- [cline-react-expert](https://github.com/example) - React 开发专家
- [cline-python-booster](https://github.com/example) - Python 效率提升

### OpenCode Skills

OpenCode 支持自定义 Agent Skills

**路径规范**：
```
.opencode/skills/
├── my-skill/
│   ├── SKILL.md
│   └── resources/
```

**推荐 Skills**：
- [opencode-mcp-integrator](https://github.com/example) - MCP 集成器
- [opencode-workflow-optimizer](https://github.com/example) - 工作流优化

### Cursor Skills

Cursor 兼容 Claude Skills 格式

**路径规范**：
```
.cursor/skills/
├── my-skill/
│   ├── SKILL.md
│   └── resources/
```

**推荐 Skills**：
- [cursor-refactoring-agent](https://github.com/example) - 重构代理
- [cursor-test-assistant](https://github.com/example) - 测试助手

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

- **Total Skills**: 100+
- **Official Skills**: 15
- **Community Skills**: 85+
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

To the extent possible under law, [大熊掌门](https://github.com/daxiong-zhangmen) has waived all copyright and related or neighboring rights to this work.

---

## Stargazers over time / 星标增长趋势

[![Stargazers over time](https://api.star-history.com/svg?repos=daxiong-zhangmen/awesome-agent-skills&type=Date)](https://star-history.com/#daxiong-zhangmen/awesome-agent-skills&Date)

---

**⭐ 如果这个项目对你有帮助，请给一个 Star！/ If this project helps you, please give it a star!**

**💡 由 [大熊掌门](https://github.com/daxiong-zhangmen) 维护 / Maintained by [大熊掌门]**

**🌐 博客 / Blog**: [五行代码](https://blog.wuxingcodes.com/)
