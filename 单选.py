import requests
from bs4 import BeautifulSoup

# res = requests.get(url="https://ks.wjx.top/vm/QS6rVBa.aspx") # 网站输入自己需要爬取的网站

file_path = '/Users/cthanatos/Downloads/wjx1.html'  # 文件路径，根据实际情况修改
content = ''
with open(file_path, 'r') as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

subject = soup.findAll(attrs={"class": "field ui-field-contain"})
# field ui-field-contain
questions_list = []
for sub in subject:
    question = sub.find(attrs={"class": "field-label"}).text

    answer = sub.findAll(attrs={"class": "ui-radio", "ans": "1"})[0].findAll(attrs={"class": "label"})[0].text
    questions_list.append({"q": question, "a": answer})

res = "问题\r\n"
for item in questions_list:
    res += "\""
    res += item["q"]
    res += "\"\r\n\""
    res += item["a"]
    res += "\"\r\n"
print()