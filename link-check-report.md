# README.md 链接验证报告

**验证日期**: 2026-01-19
**验证文件**: README.md
**项目路径**: D:\indieHacker\AI\awesome-series\awesome-agent-skills

---

## 总体统计

| 指标 | 数量 | 百分比 |
|------|------|--------|
| 总链接数 | 150 | 100% |
| 有效链接 | 142 | 94.67% |
| 无效链接 | 8 | 5.33% |

---

## 无效链接详情

### 1. 需要修复的链接 (1个)

| 链接 | 状态码 | 位置 | 说明 |
|------|--------|------|------|
| ~~https://github.com/xxx/yyy~~ | 404 | README.md:302 | 提交指南中的示例链接 |

**修复状态**: ✅ 已修复
- 已将 `https://github.com/xxx/yyy` 改为 `https://github.com/username/repository`

### 2. 无需修复的相对路径和锚点链接 (7个)

这些链接在 Markdown 文档中是正常且有效的:

| 链接 | 类型 | 说明 |
|------|------|------|
| `LICENSE` | 相对路径 | 指向本地 LICENSE 文件 |
| `README.zh-CN.md` | 相对路径 | 指向中文版 README |
| `#community-independent-skills` | 页面锚点 | 跳转到"社区独立技能"章节 |
| `#supporting-tools` | 页面锚点 | 跳转到"支持工具"章节 |
| `#learning-resources` | 页面锚点 | 跳转到"学习资源"章节 |
| `#official-team-repositories` | 页面锚点 | 跳转到"官方团队仓库"章节 |
| `#awesome-agent-skills` | 页面锚点 | 跳转到页面顶部 |

---

## 有效链接抽样检查

所有外部 HTTP/HTTPS 链接均已验证,以下为部分示例:

### 官方文档链接 (全部有效)
- ✅ https://code.claude.com/docs/en/skills
- ✅ https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
- ✅ https://cursor.com/docs/context/skills
- ✅ https://docs.windsurf.com/windsurf/cascade/skills
- ✅ https://opencode.ai/docs/skills
- ✅ https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- ✅ https://agentskills.io
- ✅ https://agentskills.io/specification
- ✅ https://agentskills.io/what-are-skills

### GitHub 仓库链接 (全部有效)
- ✅ https://github.com/anthropics/skills
- ✅ https://github.com/vercel-labs/agent-skills
- ✅ https://github.com/openai/skills
- ✅ https://github.com/huggingface/skills
- ✅ https://github.com/alirezarezvani/claude-skills
- ✅ https://github.com/ingpoc/skills
- ✅ https://github.com/langgenius/dify
- ✅ https://github.com/kepano/obsidian-skills

### 社区技能仓库 (抽样验证,全部有效)
- ✅ https://github.com/smerchek/claude-epub-skill
- ✅ https://github.com/zxkane/aws-skills
- ✅ https://github.com/chrisvoncsefalvay/claude-d3js-skill
- ✅ https://github.com/lackeyjb/playwright-skill
- ✅ https://github.com/conorluddy/ios-simulator-skill
- ✅ https://github.com/bluzername/claude-code-terminal-title
- ✅ https://github.com/1NickPappas/move-code-quality-skill
- ✅ https://github.com/jthack/ffuf_claude_skill
- ✅ https://github.com/ibelick/ui-skills
- ✅ https://github.com/omkamal/pypict-claude-skill
- ✅ https://github.com/alinaqi/claude-bootstrap
- ✅ https://github.com/kylehughes/the-unofficial-swift-concurrency-migration-skill
- ✅ https://github.com/gapmiss/obsidian-plugin-skill
- ✅ https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill
- ✅ https://github.com/sanjay3290/ai-skills
- ✅ https://github.com/mhattingpete/claude-skills-marketplace
- ✅ https://github.com/obra/superpowers-lab
- ✅ https://github.com/wrsmith108/linear-claude-skill
- ✅ https://github.com/wshuyi/x-article-publisher-skill
- ✅ https://github.com/PleasePrompto/notebooklm-skill

### 支持工具链接 (全部有效)
- ✅ https://github.com/numman-ali/openskills
- ✅ https://github.com/yusufkaraaslan/Skill_Seekers
- ✅ https://github.com/zouyingcao/agentskills-mcp
- ✅ https://github.com/brucevanfdm/agent-skills-guard
- ✅ https://github.com/davidyangcool/agent-skill
- ✅ https://skild.sh

### 博客和文档链接 (全部有效)
- ✅ https://blog.wuxingcodes.com/
- ✅ https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- ✅ https://claude.com/blog/skills-explained
- ✅ https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers
- ✅ https://support.claude.com/en/articles/12512198-creating-custom-skills

---

## 验证方法

使用 Python 脚本进行批量验证:
- 并发检查: 10 个线程
- 超时设置: 10 秒/链接
- 验证方法: HEAD 请求 (检查响应状态码)
- 有效状态码范围: 200-399

完整验证结果已保存至: `link_check_results.json`

---

## 结论

README.md 的链接整体状态**良好**,有效链接占比达到 **94.67%**。

仅发现 1 个无效的外部链接(文档示例链接),现已修复完成。其余 7 个"无效"结果均为相对路径或页面锚点链接,属于正常现象。

**建议**: 定期运行链接检查以维护链接有效性,可使用项目中的 GitHub Actions 工作流自动进行验证。

---

**验证工具**: Python requests + concurrent.futures
**报告生成**: 自动生成
