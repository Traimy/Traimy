import requests
from bs4 import BeautifulSoup

url = 'https://www.rcsb.org/ligand/' + 'B5DFG1'  # 替换为你要查询的蛋白质的 UniProt ID
response = requests.get(url)

if response.status_code == 200:  # 如果请求成功，则开始解析请求内容
    soup = BeautifulSoup(response.content, 'html.parser')
    # 找到所有包含配体相关信息的 HTML 元素
    ligand_info = soup.find_all('div', class_='col-md-4')[1]
    # 打印配体信息
    print(ligand_info.text)
else:
    print('请求失败')
