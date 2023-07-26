import requests
from bs4 import BeautifulSoup

# res = requests.get(url="https://ks.wjx.top/vm/QS6rVBa.aspx") # 网站输入自己需要爬取的网站

file_path = '/Users/cthanatos/Downloads/案例.html'  # 文件路径，根据实际情况修改
content = ''
with open(file_path, 'r') as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

subject = soup.findAll(attrs={"class": "field ui-field-contain"})
# field ui-field-contain
questions_list = []
for sub in subject:
    question = sub.find(attrs={"class": "field-label"}).text

    answer = sub.findAll(attrs={"class": "ui-checkbox", "ans": "1"})
    answers = []
    for item in answer:
        v = item.find(attrs={"class": "label"}).text
        answers.append(v)
    questions_list.append({"q": question, "a": answers})

res = "问题\r\n"
for item in questions_list:
    res += "\""
    res += item["q"]
    res += "\"\r\n\""
    cnt = 0
    lens = len(item['a'])
    for v in item["a"]:
        cnt += 1
        res += v
        if cnt == lens:
            res += "\"\r\n"
        else:
            res += "\r\n"

print()