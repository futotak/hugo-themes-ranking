#!/usr/bin/python3

import requests
import re
from bs4 import BeautifulSoup

def extract_github_stars(url):
    """
    url からGitHub Starsの右隣にある数字を抽出してリターンする関数
    整数値を返す
    """
    response = requests.get(url)

    # ステータスコードが200（成功）の場合
    if response.status_code == 200:
        # BeautifulSoupでHTMLを解析
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # "GitHub Stars:"を内容に持つ要素を探す
        gs_element = soup.find(string=re.compile("GitHub Stars:*"))
        gs_parent = gs_element.parent   #その親要素を取得
        
        stars_element = gs_parent.find_next()   # "GitHub Stars:" の親要素の次の要素が星の数を含んでいる 
        stars_text = stars_element.get_text()   # 星の数の文字列を取得
     
        return int(stars_text)  # 星の数の文字列を整数にキャストしてリターン

    # ステータスコードが200以外の場合    
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# extract_github_stars関数のテスト
if __name__ == '__main__':
    # テストケース
    print("extract_github_starsのテスト")
    url ="https://themes.gohugo.io/themes/blox-tailwind/"
    stars = extract_github_stars(url)
    print(f"stars = {stars}")
    assert(stars == 8451)
