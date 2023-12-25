from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=c%2B%2B&txtLocation=").text
soup = BeautifulSoup(html_text , 'lxml')
jobs = soup.find_all('li' , class_ = 'clearfix job-bx wht-shd-bx')
for j in jobs:
    published_date = j.find('span' , class_ = 'sim-posted').span.text
    skills = j.find('span' , class_ = 'srp-skills').text.replace(' ' , '')
    company_name = j.find('h3' , class_ = 'joblist-comp-name').text.replace(' ', '')
    more_info = j.header.h2.a['href']
    print(f"COMPANY_NAME : {company_name.strip()}")
    print(f"SKILLS REQUIRED : {skills.strip()}")
    print(f"MORE_INFO : {more_info}")
    print('')
    