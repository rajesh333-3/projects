import requests
from bs4 import BeautifulSoup as bs
import os
import pandas as pd

def scrape_data(url):
    site=requests.get(url).text
    soup=bs(site,'lxml')
    #s=soup.prettify()
    table=soup.find('div',class_='table-responsive').find('table',class_='table table-hover table-condensed')
    headers = []
    for i in table.find_all('th'):
        title = i.text
        headers.append(title)
    row_data=[]   
    for j in table.find_all('tr'):  
        row_temp=[]
        for k in j.find_all('td'):
            row_temp.append(k.text)
        row_data.append(row_temp)
            
    df = pd.DataFrame(columns = headers,data=row_data)
    df.to_csv(os.path.join('population.csv'))
    print(df.shape)
      
url="https://www.worldometers.info/world-population/world-population-projections/"      
scrape_data(url)
        
# from requests import Session
# from bs4 import BeautifulSoup as bs
 
# with Session() as s:
#     site = s.get("http://quotes.toscrape.com/login")
#     bs_content = bs(site.content, "html.parser")
#     #print(bs_content)
#     token = bs_content.find("input", {"name":"csrf_token"})["value"]
#     login_data = {"username":"admin","password":"12345", "csrf_token":token}
#     s.post("http://quotes.toscrape.com/login",login_data)
#     home_page = s.get("http://quotes.toscrape.com")
#     print((home_page.content))

# import csv
# import requests
# from bs4 import BeautifulSoup


# def scrape_data(url):

#     response = requests.get(url, timeout=10)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     table = soup.find_all('table')[1]

#     rows = table.select('tbody > tr')

#     header = [th.text.rstrip() for th in rows[0].find_all('th')]

#     with open('output.csv', 'w') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(header)
#         for row in rows[1:]:
#             data = [th.text.rstrip() for th in row.find_all('td')]
#             print(data)
#             #writer.writerow(data)


# # if __name__=="__main__":
# url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
# scrape_data(url)

