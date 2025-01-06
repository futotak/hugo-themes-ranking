#!/usr/bin/python3

import re
import requests
from funcs import extract_github_stars

# HTMLファイルのパス
file_path = './view-source_https___themes.gohugo.io.html'

url = "https://themes.gohugo.io/"
response = requests.get(url)
html_content = response.text

# # HTMLファイルを開いて内容を読み込む
# with open(file_path, 'r', encoding='utf-8') as file:
#     html_content = file.read()

# 正規表現パターンを定義
pattern = r'https://themes\.gohugo\.io/themes/[^/]+/'

# 抽出したURLを格納するリスト
theme_urls = []
# パターンにマッチする全てのURLを抽出
theme_urls = re.findall(pattern, html_content)

# URLの重複を削除
unique_urls = list(set(theme_urls))

# {URL -> GitHub Stars} のディクショナリを作成. 初期値は0にしておく
urls_stars = {url: 0 for url in unique_urls}

for url in urls_stars:
    try:
        print(url)
        stars = extract_github_stars(url)
        print(stars)
        urls_stars[url] = stars
    except Exception as e:
        print(f"例外です {url}: \n {e}")
        break

    pass

print("Success!! ########################################################")

sorted_urls_stars = sorted(urls_stars.items(), key=lambda item: item[1])
print(sorted_urls_stars)