# awesome-agent-skills

> 精选的 Agent Skills 列表，用于扩展 AI 编程助手。
> A curated list of awesome Agent Skills for extending AI coding assistants.
>
> **Maintained by [大熊掌门](https://github.com/MaesHughes) | [五行代码博客](https://blog.wuxingcodes.com/)**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License](https://img.shields.io/badge/license-CC0%201.0-blue.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/MaesHughes/awesome-agent-skills?style=social)](https://github.com/MaesHughes/awesome-agent-skills)

---

## 什么是 Agent Skills？

**Agent Skills** 是包含指令、脚本和资源的文件夹，用于教 AI 代理如何完成特定任务。每个技能包含一个 `SKILL.md` 文件，该文件使用 YAML 前言定义技能的名称和描述。

### 兼容平台
- **Claude Code** / **Claude.ai** - Anthropic 的 AI 编程助手
- **GitHub Copilot** - 微软的 AI 驱动代码补全工具
- **VS Code** - 通过 GitHub Copilot 或扩展
- **OpenCode** - 开源 AI 编程助手
- **Cursor** - AI 驱动的代码编辑器
- **Cline** - VS Code 的 AI 代理

---

## 官方 Skills

### Anthropic 官方 Skills

| Skill | 描述 | 链接 |
|-------|-------------|------|
| [docx](https://github.com/anthropics/skills/tree/main/skills/docx) | 创建、编辑和分析 Word 文档，支持修订和评论 | [查看](https://github.com/anthropics/skills/tree/main/skills/docx) |
| [pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) | 提取文本/表格、创建 PDF、合并/拆分、处理表单 | [查看](https://github.com/anthropics/skills/tree/main/skills/pdf) |
| [pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) | 创建、编辑和分析 PowerPoint 演示文稿 | [查看](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| [xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) | 创建、编辑和分析 Excel 电子表格 | [查看](https://github.com/anthropics/skills/tree/main/skills/xlsx) |
| [algorithmic-art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) | 使用 p5.js 创建生成艺术 | [查看](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) |
| [canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | 设计 PNG 和 PDF 格式的视觉艺术 | [查看](https://github.com/anthropics/skills/tree/main/skills/canvas-design) |
| [mcp-builder](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | 创建 MCP 服务器以集成外部 API | [查看](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) |
| [webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) | 使用 Playwright 测试本地 Web 应用 | [查看](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) |
| [brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) | 应用品牌颜色和字体到内容 | [查看](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) |
| [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | 创建扩展 Claude 能力的技能指南 | [查看](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |

**来源**: [anthropics/skills](https://github.com/anthropics/skills)

---

### Vercel Labs Skills

| Skill | 描述 | 链接 |
|-------|-------------|------|
| [react-best-practices](https://github.com/vercel-labs/agent-skills/tree/main/react-best-practices) | React 和 Next.js 最佳实践，40+ 性能优化规则 | [查看](https://github.com/vercel-labs/agent-skills/tree/main/react-best-practices) |
| [web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/main/web-design-guidelines) | Web 设计最佳实践，100+ 现代开发指南 | [查看](https://github.com/vercel-labs/agent-skills/tree/main/web-design-guidelines) |
| [vercel-deploy-claimable](https://github.com/vercel-labs/agent-skills/tree/main/vercel-deploy-claimable) | 一键部署到 Vercel 平台 | [查看](https://github.com/vercel-labs/agent-skills/tree/main/vercel-deploy-claimable) |

**来源**: [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)

---

### Expo Team Skills

| Skill | 描述 | 链接 |
|-------|-------------|------|
| [expo-app-design](https://github.com/expo/expo/tree/main/packages/expo-skills) | 设计和构建 Expo 应用 | [查看](https://github.com/expo/expo/tree/main/packages/expo-skills) |
| [expo-deployment](https://github.com/expo/expo/tree/main/packages/expo-skills) | 部署 Expo 应用到生产环境 | [查看](https://github.com/expo/expo/tree/main/packages/expo-skills) |
| [upgrading-expo](https://github.com/expo/expo/tree/main/packages/expo-skills) | 升级 Expo SDK 版本 | [查看](https://github.com/expo/expo/tree/main/packages/expo-skills) |

**来源**: [expo/expo](https://github.com/expo/expo)

---

## 开发工具

| 工具 | 描述 | 链接 |
|------|-------------|------|
| **skillport** | 大规模验证、管理和服务技能 | [gotalab/skillport](https://github.com/gotalab/skillport) |
| **add-skill** | Vercel 的 CLI 安装程序 | `npx add-skill` |

---

## 社区 Skills 集合

### Awesome 列表与精选

| 仓库 | 描述 | Stars |
|------------|-------------|-------|
| [VoltAgent/awesome-claude-skills](https://github.com/VoltAgent/awesome-claude-skills) | 精选 150+ Claude Skills 列表，带直接链接 | [⭐](https://github.com/VoltAgent/awesome-claude-skills) |
| [skillmatic-ai/awesome-agent-skills](https://github.com/skillmatic-ai/awesome-agent-skills) | Agent Skills 权威资源 | [⭐](https://github.com/skillmatic-ai/awesome-agent-skills) |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Claude 可定制工作流 | [⭐](https://github.com/ComposioHQ/awesome-claude-skills) |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | 中文版 Agent Skills 精选列表 | [⭐](https://github.com/heilcheng/awesome-agent-skills) |

### Skills 集合

| 仓库 | 描述 | Stars |
|------------|-------------|-------|
| [hikanner/agent-skills](https://github.com/hikanner/agent-skills) | Kanner 的 Claude Agent Skills 精选集合 | [⭐](https://github.com/hikanner/agent-skills) |
| [meetrais/claude-agent-skills](https://github.com/meetrais/claude-agent-skills) | Claude Agent Skills 示例仓库 | [⭐](https://github.com/meetrais/claude-agent-skills) |
| [GuDaStudio/skills](https://github.com/GuDaStudio/skills) | GudaStudio 的 Agent Skills 集合 | [⭐](https://github.com/GuDaStudio/skills) |

### 工具与实用程序

| 仓库 | 描述 | Stars |
|------------|-------------|-------|
| [numman-ali/openskills](https://github.com/numman-ali/openskills) | AI 编程代理的通用技能加载器（Claude Code、Cursor、Windsurf、Aider、Codex） | [⭐](https://github.com/numman-ali/openskills) |
| [zouyingcao/agentskills-mcp](https://github.com/zouyingcao/agentskills-mcp) | 通过 MCP 将 Anthropic 的 Agent Skills 带到任何 AI 代理 | [⭐](https://github.com/zouyingcao/agentskills-mcp) |
| [SteelMorgan/cursor-anthropic-skills](https://github.com/SteelMorgan/cursor-anthropic-skills) | 将 Anthropic Skills 集成到 Cursor IDE 的框架 | [⭐](https://github.com/SteelMorgan/cursor-anthropic-skills) |

### 规范与文档

| 仓库 | 描述 | Stars |
|------------|-------------|-------|
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | Agent Skills 开放格式的规范和文档 | [⭐](https://github.com/agentskills/agentskills) |
| [zebbern/agent-skills-guide](https://github.com/zebbern/agent-skills-guide) | 创建 agent skill 文件的指南和示例 | [⭐](https://github.com/zebbern/agent-skills-guide) |

### 市场

| 平台 | 描述 | 链接 |
|----------|-------------|------|
| **SkillsMP** | 浏览 71000+ 兼容 Claude Code、Codex CLI 和 ChatGPT 的 agent skills | [skillsmp.com](https://skillsmp.com/) |

---

## 安装方式

### Claude Code

```bash
# 项目级别
.claude/skills/<skill-name>/SKILL.md

# 用户级别
~/.claude/skills/<skill-name>/SKILL.md
```

### OpenCode

```bash
# 项目级别
.opencode/skills/<skill-name>/SKILL.md

# 用户级别
~/.config/opencode/skills/<skill-name>/SKILL.md
```

### Cursor

```bash
# 项目级别
.cursor/skills/<skill-name>/SKILL.md

# 用户级别
~/.cursor/skills/<skill-name>/SKILL.md
```

---

## 学习资源

### 官方文档

- 📖 [Agent Skills - Claude Code](https://code.claude.com/docs/en/skills) - Claude Code 官方指南
- 📖 [Agent Skills - OpenCode](https://opencode.ai/docs/skills/) - OpenCode 集成指南
- 📖 [Agent Skills 规范](https://github.com/anthropics/skills/blob/main/spec/agent-skills-spec.md) - 技术规范
- 📖 [Agent Skills 技术协议 - ModelScope](https://modelscope.cn/learn/2558) - 技术协议（中文）

### 社区资源

- [libukai/awesome-agent-skills](https://github.com/libukai/awesome-agent-skills) - 中文 Agent Skills 指南和教程合集
- [awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) - MCP 服务器列表（与 Skills 配合使用）

---

## 社区

### 讨论区

- 💬 [Anthropic Community](https://community.anthropic.com/)
- 💬 [r/ClaudeAI](https://reddit.com/r/ClaudeAI/) - Reddit
- 💬 [r/Cline](https://reddit.com/r/Cline/) - Cline 社区
- 💬 [Cursor Discord](https://discord.gg/cursor) - Cursor 官方 Discord
- 💬 [OpenCode Discord](https://discord.gg/opencode) - OpenCode 社区

### 贡献指南

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

**贡献方式**：
1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-skill`)
3. 提交更改 (`git commit -m 'Add amazing skill'`)
4. 推送到分支 (`git push origin feature/amazing-skill`)
5. 创建 Pull Request

**贡献规范**：
- 只包含已验证的、指向现有仓库的有效链接
- 提供清晰的说明和示例
- 遵循现有格式和风格
- 尽可能添加中英文双语描述

---

## SKILL.md 模板

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

## 功能说明

This skill helps you...

## 使用方法

1. Step one
2. Step two

## 示例

```typescript
// Example usage
```

## 要求

- Node.js 18+
- Claude Code 0.6+

## 资源

- [Documentation](https://example.com)
- [GitHub](https://github.com/example/skill)
```

---

## 统计

- **官方 Skills**: 16 (Anthropic: 10, Vercel Labs: 3, Expo: 3)
- **社区集合**: 13 个已验证仓库
- **Awesome 列表**: 4 个 (VoltAgent, skillmatic-ai, ComposioHQ, heilcheng)
- **Skills 集合**: 3 个 (hikanner, meetrais, GuDaStudio)
- **工具与实用程序**: 3 个 (openskills, agentskills-mcp, cursor-anthropic-skills)
- **开发工具**: 2 个 (skillport, add-skill)
- **市场**: 1 个 (SkillsMP - 71000+ skills)
- **最后更新**: 2026-01-18

---

## 相关项目

- [awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) - MCP 服务器列表
- [libukai/awesome-agent-skills](https://github.com/libukai/awesome-agent-skills) - 中文 Agent Skills 指南

---

## 更多资源

更多 AI 编程资源和教程，请访问：[五行代码博客](https://blog.wuxingcodes.com/)

---

## 许可证

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [大熊掌门 (MaesHughes)](https://github.com/MaesHughes) has waived all copyright and related or neighboring rights to this work.

---

## 星标增长趋势

[![Stargazers over time](https://api.star-history.com/svg?repos=MaesHughes/awesome-agent-skills&type=Date)](https://star-history.com/#MaesHughes/awesome-agent-skills&Date)

---

**⭐ 如果这个项目对你有帮助，请给一个 Star！**

**💡 由 [大熊掌门 (MaesHughes)](https://github.com/MaesHughes) 维护**

**🌐 博客**: [五行代码](https://blog.wuxingcodes.com/)

**📝 English Version / [英文文档](README.md)**
