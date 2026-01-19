<div align="center">

# Awesome Agent Skills


<p align="center">
  <img src="banner_zh.png" alt="Awesome Agent Skills Banner" width="1280">
</p>

精选的 Agent Skills 资源列表，涵盖官方团队仓库、社区独立技能、聚合项目、配套工具和学习教程。

> 💡 **为什么要关注 Agent Skills？** Skills 正在成为 AI 代理的新标准——让 Claude、Codex、Gemini 等工具通过模块化知识包获得专业能力。One agent. Unlimited specializations.

<p align="center">
  <a href="https://awesome.re">
    <img src="https://awesome.re/badge.svg" alt="Awesome" />
  </a>
  <a href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="https://img.shields.io/badge/license-CC0%201.0-blue.svg" alt="License: CC0 1.0" />
  </a>
</p>

<p align="center">
  <a href="https://blog.wuxingcodes.com">
    <img src="https://img.shields.io/badge/博客-五行代码-orange" alt="五行代码博客" />
  </a>
</p>
<p align="center">
  <a href="README.md">English</a> | <a href="README.zh-CN.md">中文</a>
</p>

</div>

---

## 快速入门

### 什么是 Agent Skills？

**Agent Skills** 是由 Anthropic 推动的开放标准，通过将专业知识打包为可复用的技能模块，让 AI 代理按需加载特定能力。

**核心优势：**
- 🧠 **渐进式加载** - 仅在需要时加载相关技能，节省上下文
- 🔧 **跨平台通用** - 同一技能适用于 Claude、Codex、Copilot 等
- 📦 **模块化设计** - 写一次，到处使用
- 🚀 **零成本分发** - 通过 Git 仓库共享和版本控制

### 支持的平台

| 平台 | 项目路径 | 全局路径 | 官方文档 |
|------|---------|---------|---------|
| **Claude Code** | `.claude/skills/` | `~/.claude/skills/` | [文档](https://code.claude.com/docs/en/skills) |
| **GitHub Copilot** | `.github/skills/` | `~/.copilot/skills/` | [文档](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |
| **Cursor** | `.cursor/skills/` | `~/.cursor/skills/` | [文档](https://cursor.com/docs/context/skills) |
| **OpenCode** | `.opencode/skills/` | `~/.config/opencode/skills/` | [文档](https://opencode.ai/docs/skills) |
| **Windsurf** | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` | [文档](https://docs.windsurf.com/windsurf/cascade/skills) |

---

## 目录

- [官方团队仓库](#官方团队仓库) - Anthropic、Vercel Labs、OpenAI 等官方技能集合
- [社区独立技能](#社区独立技能) - 按分类整理的优质独立技能仓库
- [聚合项目](#聚合项目) - 收集多个技能的精选列表
- [配套工具](#配套工具) - 技能管理、安装和开发工具
- [学习资源](#学习资源) - 教程、指南和最佳实践

---

## 官方团队仓库

### Anthropic 官方 Skills

| Skill | 描述 | 链接 |
|-------|------|------|
| **docx** | 创建、编辑和分析 Word 文档，支持修订、评论、格式保留 | [查看 →](https://github.com/anthropics/skills/tree/main/skills/docx) |
| **pdf** | 提取文本和表格、创建新 PDF、合并/拆分文档、处理表单 | [查看 →](https://github.com/anthropics/skills/tree/main/skills/pdf) |
| **pptx** | 创建、编辑和分析 PowerPoint 演示文稿，支持布局和模板 | [查看 →](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| **xlsx** | 创建、编辑和分析 Excel 电子表格，支持公式和图表 | [查看 →](https://github.com/anthropics/skills/tree/main/skills/xlsx) |
| **algorithmic-art** | 使用 p5.js 创建算法艺术和生成艺术 | [查看 →](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) |
| **mcp-builder** | 创建高质量的 MCP 服务器以集成外部 API 和服务 | [查看 →](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) |
| **webapp-testing** | 使用 Playwright 测试本地 Web 应用的前端功能 | [查看 →](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) |
| **skill-creator** | 创建有效 Agent Skills 的指南和最佳实践 | [查看 →](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |

**仓库**: [anthropics/skills](https://github.com/anthropics/skills) | **Skills 数量**: 16+

---

### Vercel Labs Skills

| Skill | 描述 | 链接 |
|-------|------|------|
| **react-best-practices** | React 和 Next.js 的最佳实践，适用于现代 Web 开发 | [查看 →](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) |
| **web-design-guidelines** | Web 设计指南和 UI/UX 最佳实践 | [查看 →](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) |
| **vercel-deploy-claimable** | Vercel 部署和项目管理技能 | [查看 →](https://github.com/vercel-labs/agent-skills/tree/main/skills/claude.ai/vercel-deploy-claimable) |

**仓库**: [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | **Skills 数量**: 3

---

### 其他官方团队仓库

| 组织 | 仓库 | Skills 数量 | 描述 |
|------|------|-----------|------|
| **OpenAI** | [openai/skills](https://github.com/openai/skills) | ? | OpenAI Codex 官方技能集合 |
| **Hugging Face** | [huggingface/skills](https://github.com/huggingface/skills) | ? | 在 HuggingFace 上使用 Skills 训练大模型 |

---

## 社区独立技能

### 📄 文档处理

| 仓库 | 描述 | 作者 |
|------|------|------|
| [claude-epub-skill](https://github.com/smerchek/claude-epub-skill) | 将 Markdown 文档转换为专业 EPUB 电子书 | [@smerchek](https://github.com/smerchek) |

---

### 💻 开发与代码工具

| 仓库 | 描述 | 作者 |
|------|------|------|
| [aws-skills](https://github.com/zxkane/aws-skills) | AWS 开发与 CDK 最佳实践，成本优化和服务器less架构 | [@zxkane](https://github.com/zxkane) |
| [claude-d3js-skill](https://github.com/chrisvoncsefalvay/claude-d3js-skill) | 教 Claude 生成 D3 图表和交互式数据可视化 | [@chrisvoncsefalvay](https://github.com/chrisvoncsefalvay) |
| [playwright-skill](https://github.com/lackeyjb/playwright-skill) | Playwright 浏览器自动化，用于测试和验证 Web 应用 | [@lackeyjb](https://github.com/lackeyjb) |
| [ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill) | 与 iOS 模拟器交互，用于测试和调试 iOS 应用 | [@conorluddy](https://github.com/conorluddy) |
| [claude-code-terminal-title](https://github.com/bluzername/claude-code-terminal-title) | 为每个 Claude Code 终端窗口提供动态标题 | [@bluzername](https://github.com/bluzername) |
| [move-code-quality-skill](https://github.com/1NickPappas/move-code-quality-skill) | 分析 Move 语言包的代码质量 | [@1NickPappas](https://github.com/1NickPappas) |
| [ffuf_claude_skill](https://github.com/jthack/ffuf_claude_skill) | 集成 ffuf Web 模糊测试工具进行漏洞分析 | [@jthack](https://github.com/jthack) |
| [ui-skills](https://github.com/ibelick/ui-skills) | 构建界面的约束指南和最佳实践 | [@ibelick](https://github.com/ibelick) |
| [pypict-claude-skill](https://github.com/omkamal/pypict-claude-skill) | 使用 PICT 设计成对测试，生成优化测试套件 | [@omkamal](https://github.com/omkamal) |
| [claude-bootstrap](https://github.com/alinaqi/claude-bootstrap) | 安全优先的项目初始化和开发环境配置 | [@alinaqi](https://github.com/alinaqi) |
| [the-unofficial-swift-concurrency-migration-skill](https://github.com/kylehughes/the-unofficial-swift-concurrency-migration-skill) | Swift 并发迁移指南 | [@kylehughes](https://github.com/kylehughes) |
| [obsidian-plugin-skill](https://github.com/gapmiss/obsidian-plugin-skill) | Obsidian 插件开发 | [@gapmiss](https://github.com/gapmiss) |

---

### 📊 数据与分析

| 仓库 | 描述 | 作者 |
|------|------|------|
| [csv-data-summarizer-claude-skill](https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill) | 自动分析 CSV 文件并生成可视化洞察，无需用户提示 | [@coffeefuelbump](https://github.com/coffeefuelbump) |
| [ai-skills](https://github.com/sanjay3290/ai-skills) | PostgreSQL 查询、深度研究和 Google Imagen 集成 | [@sanjay3290](https://github.com/sanjay3290) |

---

### 🔄 协作与项目管理

| 仓库 | 描述 | 作者 |
|------|------|------|
| [claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) | Git 操作自动化、代码实现评估、测试失败修复 | [@mhattingpete](https://github.com/mhattingpete) |
| [superpowers-lab](https://github.com/obra/superpowers-lab) | TDD、Git worktree、开发分支完成、调试、根因追踪、头脑风暴、子代理驱动开发 | [@obra](https://github.com/obra) |
| [linear-claude-skill](https://github.com/wrsmith108/linear-claude-skill) | Linear 问题管理集成 | [@wrsmith108](https://github.com/wrsmith108) |
| [x-article-publisher-skill](https://github.com/wshuyi/x-article-publisher-skill) | 发布文章到 X/Twitter | [@wshuyi](https://github.com/wshuyi) |
| [notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) | 使用 NotebookLM 进行基于文档的对话 | [@PleasePrompto](https://github.com/PleasePrompto) |

---

### 🧪 测试与开发

| 仓库 | 描述 | 作者 |
|------|------|------|
| [vexor](https://github.com/scarletkc/vexor) | 向量驱动的 CLI 语义文件搜索 | [@scarletkc](https://github.com/scarletkc) |
| [dev-agent-skills](https://github.com/fvadicamo/dev-agent-skills) | Git/GitHub 工作流，Conventional Commits 和 PR 管理 | [@fvadicamo](https://github.com/fvadicamo) |
| [react-native-best-practices](https://github.com/callstackincubator/agent-skills) | React Native 最佳实践 | [@callstackincubator](https://github.com/callstackincubator) |
| [makepad-skills](https://github.com/ZhangHanDong/makepad-skills) | Makepad UI 开发（Rust 应用） | [@ZhangHanDong](https://github.com/ZhangHanDong) |

---

### 🔧 上下文工程

| 仓库 | 描述 | 作者 |
|------|------|------|
| [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | 上下文工程技能集（8 个技能），构建生产级 AI 系统 | [@muratcankoylan](https://github.com/muratcankoylan) |
| [context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 提示工程、软件架构、SADD（子代理驱动开发）、Kaizen（持续改进） | [@NeoLabHQ](https://github.com/NeoLabHQ) |

---

### 🧬 专业领域

| 仓库 | 描述 | 作者 |
|------|------|------|
| [claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | 面向科研工作者的技能集合（128+ 科研技能） | [@K-Dense-AI](https://github.com/K-Dense-AI) |
| [clarity-gate](https://github.com/frmoretto/clarity-gate) | RAG 系统的预摄入验证 | [@frmoretto](https://github.com/frmoretto) |
| [materials-simulation-skills](https://github.com/HeshamFS/materials-simulation-skills) | 计算材料科学（数值稳定性、时间步进等） | [@HeshamFS](https://github.com/HeshamFS) |
| [varlock-claude-skill](https://github.com/wrsmith108/varlock-claude-skill) | Varlock 项目管理 | [@wrsmith108](https://github.com/wrsmith108) |

---

### 🔒 安全与系统

| 仓库 | 描述 | 作者 |
|------|------|------|
| [cloudflare-skill](https://github.com/dmmulroy/cloudflare-skill) | Cloudflare 安全集成 | [@dmmulroy](https://github.com/dmmulroy) |

---

### ✍️ 写作与内容

| 仓库 | 描述 | 作者 |
|------|------|------|
| [claude-family-history-research-skill](https://github.com/emaynard/claude-family-history-research-skill) | 家族历史研究 | [@emaynard](https://github.com/emaynard) |
| [tapestry-skills-for-claude-code](https://github.com/michalparkola/tapestry-skills-for-claude-code) | Tapestry 写作技能（文章提取、YouTube 转录、Ship Learn Next、知识网络） | [@michalparkola](https://github.com/michalparkola) |
| [claude-code-tips](https://github.com/ykdojo/claude-code-tips) | Claude Code 使用技巧（含 Reddit fetch） | [@ykdojo](https://github.com/ykdojo) |
| [notebooklm-py](https://github.com/teng-lin/notebooklm-py) | NotebookLM Python 控制 | [@teng-lin](https://github.com/teng-lin) |
| [baoyu-skills](https://github.com/JimLiu/baoyu-skills) | 宝玉老师的自用 Skills 集合 | [@JimLiu](https://github.com/JimLiu) |
| [skill-prompt-generator](https://github.com/huangserva/skill-prompt-generator) | Skill 提示词生成器 | [@huangserva](https://github.com/huangserva) |
| [NanoBanana-PPT-Skills](https://github.com/op7418/NanoBanana-PPT-Skills) | 基于 NanoBanana 生成 PPT | [@op7418](https://github.com/op7418) |

---

### 🏢 企业工作流

| 仓库 | 描述 | 作者 |
|------|------|------|
| [dify](https://github.com/langgenius/dify) | Dify 官方 Skills 集合 | [@langgenius](https://github.com/langgenius) |
| [obsidian-skills](https://github.com/kepano/obsidian-skills) | 增强 Obsidian 功能的 Skills 集合 | [@kepano](https://github.com/kepano) |

---

### 🧑‍💻 编程辅助

| 仓库 | 描述 | 作者 |
|------|------|------|
| [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX 设计最佳实践 | [@nextlevelbuilder](https://github.com/nextlevelbuilder) |
| [planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 使用文件实现长期规划 | [@OthmanAdi](https://github.com/OthmanAdi) |

---

### 🧪 开发与测试工具

| 仓库 | 描述 | 作者 |
|------|------|------|
| [dev-browser](https://github.com/SawyerHood/dev-browser) | 开发者浏览器工具 | [@SawyerHood](https://github.com/SawyerHood) |
| [skillport](https://github.com/gotalab/skillport) | Skills 端口工具 | [@gotalab](https://github.com/gotalab) |
| [sheets-cli](https://github.com/gmickel/sheets-cli) | Google Sheets CLI | [@gmickel](https://github.com/gmickel) |
| [SkillsBench](https://github.com/benchflow-ai/SkillsBench) | Skills 基准测试 | [@benchflow-ai](https://github.com/benchflow-ai) |
| [pomodoro](https://github.com/jakedahn/pomodoro) | 番茄钟技能 | [@jakedahn](https://github.com/jakedahn) |
| [Mind-Cloning-Engineering](https://github.com/yzfly/Mind-Cloning-Engineering) | 思维克隆工程 | [@yzfly](https://github.com/yzfly) |

---

### 🤖 自动化与集成

| 仓库 | 描述 | 作者 |
|------|------|------|
| [n8n-skills](https://github.com/czlonkowski/n8n-skills) | n8n 工作流自动化技能集（7 个技能） | [@czlonkowski](https://github.com/czlonkowski) |
| [n8n-skills](https://github.com/haunchen/n8n-skills) | n8n 工作流自动化技能集（另一个实现） | [@haunchen](https://github.com/haunchen) |

---

### 🛠️ 配套工具

| 仓库 | 描述 | 类型 |
|------|------|------|
| [openskills](https://github.com/numman-ali/openskills) | Skills 全局加载工具，支持 Claude Code、Cursor、Windsurf 等多种 AI 工具 | CLI 工具 |
| [Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | 自动化抓取文档网站、GitHub 仓库和 PDF 文件转换为 Agent Skills | 自动化工具 |
| [agentskills-mcp](https://github.com/zouyingcao/agentskills-mcp) | 通过 MCP 将 Agent Skills 带到任何 MCP 兼容的 AI 代理 | MCP 服务器 |
| [agent-skills-guard](https://github.com/brucevanfdm/agent-skills-guard) | Agent Skills 可视化管理 + 精选仓库 + 安全扫描 | 管理工具 |
| [skillmaster](https://github.com/davidyangcool/agent-skill) | 通过终端管理、安装和使用 Agent Skills | CLI 工具 |
| [skild.sh](https://skild.sh) | 在多个工具中安装、管理和同步 Skills 的命令行工具 | 网站 |

---

## 学习资源

### 官方文档

- [Agent Skills 规范](https://agentskills.io) - 开放格式规范和文档
- [What Are Skills](https://agentskills.io/what-are-skills) - 技能概念详解
- [Specification](https://agentskills.io/specification) - 格式规范详情
- [Creating Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills) - 创建技能指南

### 创建指南

- [Skill Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) - 官方最佳实践
- [agent-skills-guide](https://github.com/zebbern/agent-skills-guide) - 社区创建指南

### 工程深度解析

- [Equipping agents for the real world](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - Anthropic 工程博客
- [Skills explained: How Skills compares](https://claude.com/blog/skills-explained) - Skills 与其他方式的对比
- [Extending Claude's capabilities](https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers) - 技能与 MCP 的结合

---

## 贡献指南

欢迎提交 Pull Request 添加新的 Agent Skills 仓库！

### 提交规范

1. **Fork 本仓库** 并创建特性分支
2. **添加技能** 到对应分类下，按字母顺序排列
3. **格式要求**:
   ```markdown
   | [仓库名](https://github.com/xxx/yyy) | 简短描述 | [@作者](https://github.com/xxx) |
   ```
4. **质量标准**:
   - ✅ 包含 `SKILL.md` 文件的独立仓库（至少 **5 stars**）
   - ✅ 官方组织仓库（Anthropic、Vercel Labs、OpenAI、Dify 等）
   - ❌ 不收录个人/社区聚合仓库（避免重复）
   - ❌ 不收录纯文档/教程项目（放入学习资源）
   - ❌ 不收录少于 5 stars 的项目（质量把控）

### 本地预览

```bash
# 克隆仓库
git clone https://github.com/MaesHughes/awesome-agent-skills.git
cd awesome-agent-skills

# 安装依赖
npm install -g markdown-link-check

# 检查链接
markdown-link-check README.md

# 预览 Markdown
npx serve
```

---

## 授权协议

本项目采用 [CC0 1.0 Universal](LICENSE) 许可证，您可以自由使用、修改和分发本列表中的内容。

<div align="center">

---

**[⬆ 回到顶部](#awesome-agent-skills)**

**维护者**: [大熊掌门](https://github.com/MaesHughes) | **博客**: [五行代码](https://blog.wuxingcodes.com/)

</div>
