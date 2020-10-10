import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
print(r.status_code)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
print(soup.title)
tag = soup.a
print(tag.name)
print(tag.parent.name)
print(tag.parent.parent.name)
print(tag.attrs)
print(soup.head)
print(soup.head.contents)
print(soup.body.contents)
print(len(soup.body.contents))
print(soup.title.parent)
print(soup.prettify())
