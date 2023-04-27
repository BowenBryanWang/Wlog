# 读取index.html文件
import bs4
from bs4 import BeautifulSoup
import os

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.prettify())
    svg: bs4.element.ResultSet = soup.find_all("svg")
    for i in svg:
        if "style" in i.attrs.keys() and "xmlns" in i.attrs.keys() and i.attrs["xmlns"] == "http://www.w3.org/2000/svg":
            print(i)
            print(i.attrs)
            i.attrs["style"] = i.attrs["style"]+"display: inline;"
            print(i.attrs)
    # print(soup.prettify())
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(str(soup))

