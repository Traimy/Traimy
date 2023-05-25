import requests
from bs4 import BeautifulSoup

# 设置请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# 设置目标url
url = 'http://www.rcsb.org/pdb/explore/literature.do?structureId=B5DFG1'
# 发送请求，获取html页面
response = requests.get(url, headers=headers)
html = response.text
# 使用BeautifulSoup解析html
soup = BeautifulSoup(html, 'html.parser')
# 查找目标标签
tags = soup.find_all('a', {'class': 'bodytext'})  # 这里找到所有class为'bodytext'的超链接标签，即配体相关信息所在的标签
# 遍历标签，提取配体相关信息
for tag in tags:
    if 'Ligand Summary' in tag.text:  # 找到'Ligand Summary'字符串
        ligand_url = 'http://www.rcsb.org' + tag.get('href')  # 获取配体信息的url
        ligand_response = requests.get(ligand_url, headers=headers)  # 发送请求，获取配体信息html页面
        ligand_html = ligand_response.text
        # 解析html页面，提取配体信息
        ligand_soup = BeautifulSoup(ligand_html, 'html.parser')
        ligand_table = ligand_soup.find('table', {'class': 'information_table'})  # 找到包含配体信息的table标签
        # 遍历table标签中的所有<tr>标签，提取配体基本信息
        for tr in ligand_table.find_all('tr'):
            tds = tr.find_all('td')
            if len(tds) == 2:
                key = tds[0].text.strip()
                value = tds[1].text.strip()
                print(key + ': ' + value)
