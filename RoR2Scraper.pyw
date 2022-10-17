#! c:\\Users\\corye\\AppData\\Local\\Programs\\Python\\Python38\\pythonw.exe

import requests
from bs4 import BeautifulSoup

f = open('C:/Users/corye/Documents/RoR2 Wiki Scraper/xml.txt', 'w')

response = requests.get(
    url="https://riskofrain2.fandom.com/wiki/",
)

soup = BeautifulSoup(response.content, 'html.parser')

numberOfSkills = len(soup.find_all("table", {"class": "article-table skill"}))
print(numberOfSkills)

#scrapes passive abilities
f.write("<string-array name=\"voidFiendPassive\">\n")
f.write("\t<item>" + str(len(soup.find("div", {"class": "skillbox"}).find_all("table", {"class": "article-table skill"}))) + "</item>\n")
for x in range(len(soup.find("div", {"class": "skillbox"}).find_all("table", {"class": "article-table skill"}))):
    if x == 0:
        f.write("\t<item>")
        f.write(soup.find("table", {"class": "article-table skill"}).find("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 1:
        f.write("\t<item>")
        f.write(soup.find("table", {"class": "article-table skill"}).find_next("table", {"class": "article-table skill"}).find("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 2:
        f.write("\t<item>")
        f.write(soup.find("table", {"class": "article-table skill"}).find_next("table", {"class": "article-table skill"}).find_next("table", {"class": "article-table skill"}).find("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 3:
        f.write("\t<item>")
        f.write(soup.find("table", {"class": "article-table skill"}).find_next("table", {"class": "article-table skill"}).find_next("table", {"class": "article-table skill"}).find_next("table", {"class": "article-table skill"}).find("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
f.write("</string-array>\n")
#scrapes primary abilities
f.write("<string-array name=\"voidFiendPrimary\">\n")
f.write("\t<item>" + str(len(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_all("table", {"class": "article-table skill"}))) + "</item>\n")
for x in range(len(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_all("table", {"class": "article-table skill"}))):
    if x == 0:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 1:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 2:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 3:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
f.write("</string-array>\n")
#scrapes secondary abilities
f.write("<string-array name=\"voidFiendSecondary\">\n")
f.write("\t<item>" + str(len(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_all("table", {"class": "article-table skill"}))) + "</item>\n")
for x in range(len(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_all("table", {"class": "article-table skill"}))):
    if x == 0:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 1:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 2:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 3:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
f.write("</string-array>\n")
#scrapes utility abilities
f.write("<string-array name=\"voidFiendUtility\">\n")
f.write("\t<item>" + str(len(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_all("table", {"class": "article-table skill"}))) + "</item>\n")
for x in range(len(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_all("table", {"class": "article-table skill"}))):
    if x == 0:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 1:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 2:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 3:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
f.write("</string-array>\n")
#scrapes special abilities
f.write("<string-array name=\"voidFiendSpecial\">\n")
f.write("\t<item>" + str(len(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_all("table", {"class": "article-table skill"}))) + "</item>\n")
for x in range(len(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_all("table", {"class": "article-table skill"}))):
    if x == 0:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 1:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 2:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
    if x == 3:
        f.write("\t<item>")
        f.write(soup.find("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find_next("div", {"class": "skillbox"}).find("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).find_next("span", {"class": "mw-headline"}).text)
        f.write("</item>\n")
f.write("</string-array>\n")