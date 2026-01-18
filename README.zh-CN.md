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

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [docx](https://github.com/anthropics/skills/tree/main/skills/docx) | 创建、编辑和分析 Word 文档，支持修订和评论 | [anthropics/skills](https://github.com/anthropics/skills) |
| [pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) | 提取文本/表格、创建 PDF、合并/拆分、处理表单 | [anthropics/skills](https://github.com/anthropics/skills) |
| [pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) | 创建、编辑和分析 PowerPoint 演示文稿 | [anthropics/skills](https://github.com/anthropics/skills) |
| [xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) | 创建、编辑和分析 Excel 电子表格 | [anthropics/skills](https://github.com/anthropics/skills) |
| [algorithmic-art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) | 使用 p5.js 创建生成艺术 | [anthropics/skills](https://github.com/anthropics/skills) |
| [canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | 设计 PNG 和 PDF 格式的视觉艺术 | [anthropics/skills](https://github.com/anthropics/skills) |
| [mcp-builder](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | 创建 MCP 服务器以集成外部 API | [anthropics/skills](https://github.com/anthropics/skills) |
| [webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) | 使用 Playwright 测试本地 Web 应用 | [anthropics/skills](https://github.com/anthropics/skills) |
| [brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) | 应用品牌颜色和字体到内容 | [anthropics/skills](https://github.com/anthropics/skills) |
| [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | 创建扩展 Claude 能力的技能指南 | [anthropics/skills](https://github.com/anthropics/skills) |

### Vercel Labs Skills

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [react-best-practices](https://github.com/vercel-labs/agent-skills/tree/main/react-best-practices) | React 和 Next.js 最佳实践，40+ 性能优化规则 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| [web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/main/web-design-guidelines) | Web 设计最佳实践，100+ 现代开发指南 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| [vercel-deploy-claimable](https://github.com/vercel-labs/agent-skills/tree/main/vercel-deploy-claimable) | 一键部署到 Vercel 平台 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |

### Expo Team Skills

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [expo-app-design](https://github.com/expo/expo/tree/main/packages/expo-skills) | 设计和构建 Expo 应用 | [expo/expo](https://github.com/expo/expo) |
| [expo-deployment](https://github.com/expo/expo/tree/main/packages/expo-skills) | 部署 Expo 应用到生产环境 | [expo/expo](https://github.com/expo/expo) |
| [upgrading-expo](https://github.com/expo/expo/tree/main/packages/expo-skills) | 升级 Expo SDK 版本 | [expo/expo](https://github.com/expo/expo) |

---

## Skills 分类

### 开发工具 / Development

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [test-driven-development](https://github.com/obra/skills) | 使用 TDD 工作流先写测试再实现代码 | [obra/skills](https://github.com/obra/skills) |
| [debugging](https://github.com/obra/skills) | 系统化调试策略和技巧 | [obra/skills](https://github.com/obra/skills) |
| [code-review](https://github.com/obra/skills) | 使用团队标准和最佳实践审查代码 | [obra/skills](https://github.com/obra/skills) |
| [refactoring](https://github.com/obra/skills) | 在不改变行为的情况下重构现有代码 | [obra/skills](https://github.com/obra/skills) |
| [api-design](https://github.com/obra/skills) | 使用最佳实践设计 RESTful API | [obra/skills](https://github.com/obra/skills) |
| [clean-architecture](https://github.com/obra/skills) | 在项目中实施清洁架构模式 | [obra/skills](https://github.com/obra/skills) |
| [design-patterns](https://github.com/obra/skills) | 适当应用四人组设计模式 | [obra/skills](https://github.com/obra/skills) |

### Git 与版本控制 / Git & Version Control

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [commit-helper](https://github.com/anthropics/skills) | 生成清晰、规范的 Git 提交信息 | [anthropics/skills](https://github.com/anthropics/skills) |
| [git-release](https://github.com/Vercel/cli) | 从合并的 PR 创建一致的发布和更新日志 | [Vercel/cli](https://github.com/Vercel/cli) |
| [pr-review](https://github.com/obra/skills) | 使用团队标准审查 Pull Request | [obra/skills](https://github.com/obra/skills) |
| [branch-strategy](https://github.com/obra/skills) | 实施 Git 分支策略（GitFlow、trunk-based） | [obra/skills](https://github.com/obra/skills) |
| [git-workflow](https://github.com/obra/skills) | 优化团队协作的 Git 工作流 | [obra/skills](https://github.com/obra/skills) |

### 测试 / Testing

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [webapp-testing](https://github.com/anthropics/skills) | 使用 Playwright 测试本地 Web 应用 | [anthropics/skills](https://github.com/anthropics/skills) |
| [unit-testing](https://github.com/obra/skills) | 编写全面的单元测试以覆盖代码 | [obra/skills](https://github.com/obra/skills) |
| [integration-testing](https://github.com/obra/skills) | 测试系统组件之间的集成 | [obra/skills](https://github.com/obra/skills) |
| [e2e-testing](https://github.com/obra/skills) | 用户流程的端到端测试 | [obra/skills](https://github.com/obra/skills) |

### React 与前端 / React & Frontend

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [react-best-practices](https://github.com/vercel-labs/agent-skills) | React 和 Next.js 最佳实践，40+ 性能规则 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| [web-design-guidelines](https://github.com/vercel-labs/agent-skills) | Web 设计最佳实践，100+ 现代指南 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| [react-hooks](https://github.com/obra/skills) | 有效使用 React Hooks 和模式 | [obra/skills](https://github.com/obra/skills) |
| [state-management](https://github.com/obra/skills) | 实施状态管理（Redux、Zustand、Jotai） | [obra/skills](https://github.com/obra/skills) |
| [component-design](https://github.com/obra/skills) | 设计可重用的 React 组件库 | [obra/skills](https://github.com/obra/skills) |
| [performance-optimization](https://github.com/obra/skills) | 优化 React 应用性能 | [obra/skills](https://github.com/obra/skills) |

### 移动开发 / Mobile Development

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [react-native-best-practices](https://github.com/callstackincubator/agent-skills) | React Native 性能优化指南 | [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills) |
| [expo-app-design](https://github.com/expo/expo) | 设计和构建 Expo 应用 | [expo/expo](https://github.com/expo/expo) |
| [expo-deployment](https://github.com/expo/expo) | 部署 Expo 应用到生产商店 | [expo/expo](https://github.com/expo/expo) |
| [upgrading-expo](https://github.com/expo/expo) | 安全升级 Expo SDK 版本 | [expo/expo](https://github.com/expo/expo) |

### DevOps 与部署 / DevOps & Deployment

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [vercel-deploy-claimable](https://github.com/vercel-labs/agent-skills) | 一键部署到 Vercel 平台 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| [docker-setup](https://github.com/obra/skills) | 为应用设置 Docker 容器 | [obra/skills](https://github.com/obra/skills) |
| [ci-cd-pipeline](https://github.com/obra/skills) | 使用 GitHub Actions 创建 CI/CD 管道 | [obra/skills](https://github.com/obra/skills) |
| [infrastructure-as-code](https://github.com/obra/skills) | 使用 Terraform/Pulumi 定义基础设施 | [obra/skills](https://github.com/obra/skills) |

### 文档处理 / Documentation

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [docx](https://github.com/anthropics/skills) | 创建、编辑和分析 Word 文档，支持修订 | [anthropics/skills](https://github.com/anthropics/skills) |
| [pdf](https://github.com/anthropics/skills) | 提取文本/表格、创建 PDF、合并/拆分 | [anthropics/skills](https://github.com/anthropics/skills) |
| [pptx](https://github.com/anthropics/skills) | 创建、编辑和分析 PowerPoint 演示文稿 | [anthropics/skills](https://github.com/anthropics/skills) |
| [xlsx](https://github.com/anthropics/skills) | 创建、编辑和分析 Excel 电子表格 | [anthropics/skills](https://github.com/anthropics/skills) |
| [technical-writing](https://github.com/obra/skills) | 编写清晰的技术文档 | [obra/skills](https://github.com/obra/skills) |
| [api-documentation](https://github.com/obra/skills) | 从代码生成 API 文档 | [obra/skills](https://github.com/obra/skills) |

### 数据科学 / Data & Science

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [data-analysis](https://github.com/obra/skills) | 使用 pandas 和 numpy 进行数据分析 | [obra/skills](https://github.com/obra/skills) |
| [data-visualization](https://github.com/obra/skills) | 使用 matplotlib/plotly 创建数据可视化 | [obra/skills](https://github.com/obra/skills) |
| [machine-learning](https://github.com/obra/skills) | 使用 scikit-learn 构建和训练 ML 模型 | [obra/skills](https://github.com/obra/skills) |

### 设计创意 / Design & Creative

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [algorithmic-art](https://github.com/anthropics/skills) | 使用 p5.js 创建生成艺术 | [anthropics/skills](https://github.com/anthropics/skills) |
| [canvas-design](https://github.com/anthropics/skills) | 设计 PNG 和 PDF 格式的视觉艺术 | [anthropics/skills](https://github.com/anthropics/skills) |
| [brand-guidelines](https://github.com/anthropics/skills) | 应用品牌颜色和字体到内容 | [anthropics/skills](https://github.com/anthropics/skills) |
| [ui-design-systems](https://github.com/obra/skills) | 创建一致的 UI 设计系统 | [obra/skills](https://github.com/obra/skills) |

### MCP 集成 / MCP Integration

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [mcp-builder](https://github.com/anthropics/skills) | 创建 MCP 服务器以集成外部 API | [anthropics/skills](https://github.com/anthropics/skills) |
| [mcp-client](https://github.com/obra/skills) | 将 AI 代理连接到 MCP 服务器 | [obra/skills](https://github.com/obra/skills) |

### 安全 / Security

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [security-audit](https://github.com/obra/skills) | 对代码库执行安全审计 | [obra/skills](https://github.com/obra/skills) |
| [dependency-check](https://github.com/obra/skills) | 检查依赖项的漏洞 | [obra/skills](https://github.com/obra/skills) |
| [authentication](https://github.com/obra/skills) | 实施安全认证（OAuth、JWT） | [obra/skills](https://github.com/obra/skills) |

### 工作流自动化 / Workflow & Automation

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [task-automation](https://github.com/obra/skills) | 自动化重复性开发任务 | [obra/skills](https://github.com/obra/skills) |
| [file-organization](https://github.com/obra/skills) | 组织项目文件和目录 | [obra/skills](https://github.com/obra/skills) |
| [code-generation](https://github.com/obra/skills) | 高效生成样板代码 | [obra/skills](https://github.com/obra/skills) |

### 数据库 / Database

| Skill | 描述 | 来源 |
|-------|-------------|--------|
| [sql-queries](https://github.com/obra/skills) | 编写优化的 SQL 查询 | [obra/skills](https://github.com/obra/skills) |
| [database-design](https://github.com/obra/skills) | 设计规范化数据库架构 | [obra/skills](https://github.com/obra/skills) |
| [orm-usage](https://github.com/obra/skills) | 有效使用 ORM（Prisma、TypeORM、SQLAlchemy） | [obra/skills](https://github.com/obra/skills) |
| [migration-management](https://github.com/obra/skills) | 安全管理数据库迁移 | [obra/skills](https://github.com/obra/skills) |

### 社区精选 / Community Skills

| Skill | 作者 | 描述 |
|-------|--------|-------------|
| [baoyu-skills](https://github.com/baoyuto/skills) | @baoyuto | 宝玉老师自用 Skills（自动发公众号等） |
| [planning-with-files](https://github.com/different-planet/skills) | @different-planet | 使用文件规划实现 Manus 效果 |
| [skill-prompt-generator](https://github.com/prompt-engineer/skills) | @prompt-engineer | 从现有代码生成 Skill 提示词 |
| [claude-scientific-skills](https://github.com/scientist/skills) | @scientist | 128+ 科研技能（生物、化学、ML） |
| [ui-ux-pro-max](https://github.com/designer/skills) | @designer | UI/UX 设计 Skills 集合 |

---

## 开发工具 / Development Tools

| 工具 | 描述 | 链接 |
|------|-------------|------|
| **skillport** | 大规模验证、管理和服务技能 | [gotalab/skillport](https://github.com/gotalab/skillport) |
| **add-skill** | Vercel 的 CLI 安装程序 | `npx add-skill` |

---

## 安装方式 / Installation

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

## 学习资源 / Learning Resources

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

## 社区 / Community

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

## 功能说明 / What it does

This skill helps you...

## 使用方法 / How to use

1. Step one
2. Step two

## 示例 / Examples

```typescript
// Example usage
```

## 要求 / Requirements

- Node.js 18+
- Claude Code 0.6+

## 资源 / Resources

- [Documentation](https://example.com)
- [GitHub](https://github.com/example/skill)
```

---

## 统计 / Stats

- **Skills 总数**: 150+
- **官方 Skills**: 16 (Anthropic: 10, Vercel Labs: 3, Expo: 3)
- **社区 Skills**: 135+
- **分类数**: 15 (开发、Git、测试、React、移动、DevOps、文档、数据、设计、MCP、安全、工作流、数据库、创意)
- **最后更新**: 2026-01-18

---

## 🔗 相关项目 / Related Projects

- [awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) - MCP 服务器列表
- [awesome-ai-coding-tools](https://github.com/ai-for-developers/awesome-ai-coding-tools) - AI 编程工具列表
- [openskills](https://github.com/numman-ali/openskills) - 通用 Skills 加载器
- [MCP Market](https://mcpmarket.com) - MCP 服务器市场

---

## 🌐 更多资源 / More Resources

更多 AI 编程资源和教程，请访问：[五行代码博客](https://blog.wuxingcodes.com/)

---

## 许可证 / License

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [大熊掌门 (MaesHughes)](https://github.com/MaesHughes) has waived all copyright and related or neighboring rights to this work.

---

## 星标增长趋势 / Stargazers over time

[![Stargazers over time](https://api.star-history.com/svg?repos=MaesHughes/awesome-agent-skills&type=Date)](https://star-history.com/#MaesHughes/awesome-agent-skills&Date)

---

**⭐ 如果这个项目对你有帮助，请给一个 Star！/ If this project helps you, please give it a star!**

**💡 由 [大熊掌门 (MaesHughes)](https://github.com/MaesHughes) 维护 / Maintained by [大熊掌门]**

**🌐 博客 / Blog**: [五行代码](https://blog.wuxingcodes.com/)
