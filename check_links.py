#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
链接验证脚本 - 批量检查 README.md 中的链接
"""
import re
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from urllib.parse import urlparse
import time
import sys
import io

# 设置标准输出为UTF-8编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 读取README文件
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 提取所有链接
link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
matches = re.findall(link_pattern, content)

# 去重并过滤
links = list(set([match[1] for match in matches]))
print(f"找到 {len(links)} 个唯一链接")

# 忽略的链接模式
ignore_patterns = [
    r'^https://github\.com/daxiong-zhangmen/awesome-agent-skills',
    r'^http://localhost',
    r'^https://creativecommons\.org',
    r'^https://awesome\.re',
    r'^https://i\.creativecommons\.org',
    r'^https://api\.star-history\.com',
]

def should_ignore(url):
    """检查是否应该忽略此链接"""
    for pattern in ignore_patterns:
        if re.match(pattern, url):
            return True
    return False

# 过滤需要检查的链接
links_to_check = [link for link in links if not should_ignore(link)]
print(f"需要检查 {len(links_to_check)} 个链接")

# 结果存储
results = {
    'total': len(links_to_check),
    'checked': 0,
    'valid': [],
    'invalid': [],
    'errors': []
}

def check_link(url):
    """检查单个链接"""
    try:
        start_time = time.time()
        response = requests.head(url, allow_redirects=True, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        elapsed = time.time() - start_time

        status_code = response.status_code
        is_valid = 200 <= status_code < 400

        return {
            'url': url,
            'status': status_code,
            'valid': is_valid,
            'time': round(elapsed, 2)
        }
    except Exception as e:
        return {
            'url': url,
            'status': 0,
            'valid': False,
            'error': str(e)
        }

# 使用多线程检查链接
print("开始检查链接...")
with ThreadPoolExecutor(max_workers=10) as executor:
    future_to_url = {executor.submit(check_link, url): url for url in links_to_check}

    for future in as_completed(future_to_url):
        result = future.result()
        results['checked'] += 1

        if result['valid']:
            results['valid'].append(result)
            print(f"[OK] [{results['checked']}/{results['total']}] {result['url']} ({result['status']})")
        else:
            results['invalid'].append(result)
            if 'error' in result:
                print(f"[FAIL] [{results['checked']}/{results['total']}] {result['url']} - ERROR: {result['error']}")
            else:
                print(f"[FAIL] [{results['checked']}/{results['total']}] {result['url']} ({result['status']})")

# 保存结果
with open('link_check_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

# 打印总结
print("\n" + "="*50)
print("链接检查完成!")
print(f"总计: {results['total']} 个链接")
print(f"已检查: {results['checked']} 个链接")
print(f"有效: {len(results['valid'])} 个")
print(f"无效: {len(results['invalid'])} 个")
print("="*50)

# 打印无效链接详情
if results['invalid']:
    print("\n无效链接列表:")
    for item in results['invalid']:
        if 'error' in item:
            print(f"  [X] {item['url']} - ERROR: {item['error']}")
        else:
            print(f"  [X] {item['url']} (Status: {item['status']})")
