#!/usr/bin/env python3
"""查询 GitHub 仓库的 star 数"""

import requests
import json

# 所有需要检查的独立 skill 仓库
repositories = [
    # 文档处理
    "smerchek/claude-epub-skill",

    # 开发与代码工具
    "zxkane/aws-skills",
    "chrisvoncsefalvay/claude-d3js-skill",
    "lackeyjb/playwright-skill",
    "conorluddy/ios-simulator-skill",
    "bluzername/claude-code-terminal-title",
    "1NickPappas/move-code-quality-skill",
    "jthack/ffuf_claude_skill",
    "ibelick/ui-skills",
    "omkamal/pypict-claude-skill",
    "alinaqi/claude-bootstrap",
    "kylehughes/the-unofficial-swift-concurrency-migration-skill",
    "gapmiss/obsidian-plugin-skill",

    # 数据与分析
    "coffeefuelbump/csv-data-summarizer-claude-skill",
    "sanjay3290/ai-skills",

    # 协作与项目管理
    "mhattingpete/claude-skills-marketplace",
    "obra/superpowers-lab",
    "wrsmith108/linear-claude-skill",
    "wshuyi/x-article-publisher-skill",
    "PleasePrompto/notebooklm-skill",

    # 测试与开发
    "scarletkc/vexor",
    "fvadicamo/dev-agent-skills",
    "callstackincubator/agent-skills",
    "ZhangHanDong/makepad-skills",

    # 上下文工程
    "muratcankoylan/Agent-Skills-for-Context-Engineering",
    "NeoLabHQ/context-engineering-kit",

    # 专业领域
    "K-Dense-AI/claude-scientific-skills",
    "SHADOWPR0/security-bluebook-builder",
    "frmoretto/clarity-gate",
    "HeshamFS/materials-simulation-skills",
    "wrsmith108/varlock-claude-skill",
    "SHADOWPR0/beautiful_prose",

    # 安全与系统
    "dmmulroy/cloudflare-skill",

    # 写作与内容
    "emaynard/claude-family-history-research-skill",
    "michalparkola/tapestry-skills-for-claude-code",
    "ykdojo/claude-code-tips",
    "teng-lin/notebooklm-py",
    "JimLiu/baoyu-skills",
    "huangserva/skill-prompt-generator",
    "op7418/NanoBanana-PPT-Skills",

    # 企业工作流
    "langgenius/dify",
    "kepano/obsidian-skills",

    # 编程辅助
    "nextlevelbuilder/ui-ux-pro-max-skill",
    "OthmanAdi/planning-with-files",

    # 开发与测试工具
    "SawyerHood/dev-browser",
    "gotalab/skillport",
    "gmickel/sheets-cli",
    "benchflow-ai/SkillsBench",
    "jakedahn/pomodoro",
    "yzfly/Mind-Cloning-Engineering",

    # 自动化与集成
    "czlonkowski/n8n-skills",
    "haunchen/n8n-skills",

    # 配套工具
    "numman-ali/openskills",
    "yusufkaraaslan/Skill_Seekers",
    "zouyingcao/agentskills-mcp",
    "brucevanfdm/agent-skills-guard",
    "davidyangcool/agent-skill",
]

def get_stars(repo):
    """查询仓库的 star 数"""
    url = f"https://api.github.com/repos/{repo}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("stargazers_count", 0)
        else:
            print(f"  Error querying {repo}: HTTP {response.status_code}")
            return None
    except Exception as e:
        print(f"  Exception querying {repo}: {e}")
        return None

def main():
    """主函数"""
    import sys
    import io

    # 设置 UTF-8 编码输出
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("查询 GitHub 仓库 star 数...\n")

    results = []
    low_stars = []  # 低于 5 stars 的项目

    for repo in repositories:
        stars = get_stars(repo)
        if stars is not None:
            results.append((repo, stars))
            if stars < 5:
                low_stars.append((repo, stars))
            status = "[OK]" if stars >= 5 else "[LOW]"
            print(f"{status} {repo}: {stars} stars")

    # 打印总结
    print(f"\n总仓库数: {len(results)}")
    print(f"满足 5+ stars: {sum(1 for _, s in results if s >= 5)}")
    print(f"低于 5 stars: {len(low_stars)}")

    if low_stars:
        print("\n" + "="*60)
        print("需要删除的项目（低于 5 stars）：")
        print("="*60)
        for repo, stars in sorted(low_stars, key=lambda x: x[1]):
            print(f"  [DEL] {repo}: {stars} stars")

    # 保存结果到文件
    with open("star_check_results.json", "w", encoding="utf-8") as f:
        json.dump({
            "total": len(results),
            "qualified": sum(1 for _, s in results if s >= 5),
            "low_stars_count": len(low_stars),
            "results": [{"repo": r, "stars": s} for r, s in results],
            "low_stars": [{"repo": r, "stars": s} for r, s in low_stars]
        }, f, indent=2, ensure_ascii=False)

    print(f"\n结果已保存到 star_check_results.json")

if __name__ == "__main__":
    main()
