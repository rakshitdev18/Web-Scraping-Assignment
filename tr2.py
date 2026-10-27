import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://realpython.github.io/fake-jobs/"
r=requests.get(url)
soup=BeautifulSoup(r.content, 'html.parser')

job_title_list=[]
job_title=soup.find_all("h2","title is-5")
for i in job_title:
    job_title_list.append(i.text.strip())

company_name_list=[]
company_name=soup.find_all("h3","subtitle is-6 company")
for i in company_name:
    company_name_list.append(i.text.strip())

location_list=[]
location=soup.find_all("p","location")
for i in location:
    location_list.append(i.text.strip())

job_url_list=[]
job_url=soup.find_all("a",attrs={"href":True})
for i in job_url:
    if i.get_text(strip=True) == "Apply":
        job_url_list.append(i["href"].strip())

# print(len(job_title_list))
# print(len(company_name_list))
# print(len(location_list))
# print(len(job_url_list))

df=pd.DataFrame({"Job Title":job_title_list,"Company Name":company_name_list,"Location":location_list,"Job detail page URL":job_url_list})
df.index=range(1,len(df)+1)
df.to_csv("Job Postings.csv")