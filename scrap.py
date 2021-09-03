from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome('C:\project128\chromedriver_win32\chromedriver.exe')
browser.get(start_url)
time.sleep(15)

def scrap():
    headers=["Proper name","Distance","Mass","Radius"]
    planet_data=[]

    for i in range(1,448):
        soup=BeautifulSoup(browser.page_source,'html.parser')
        for tr_tag in soup.find_all('tr',attrs={'class','exoplanet'}):
            td_tags=tr_tag.find_all('td')#li-td ul tr

            temp_list=[]

            for index,td_tags in enumerate(td_tags):
                if index==0:
                    temp_list.append(td_tags.find_all('a')[0].contents[0])

                else:
                    try:
                        temp_list.append(td_tags.contents[0])

                    except:
                        temp_list.append(' ')

            hyperlink_li_tag=li_tags[0]
            temp_list.append('https://en.wikipedia.org/wiki/List_of_brown_dwarfs'+hyperlink_li_tag.find_all('a',href=True)[0]['href'])

            planet_data.append(temp_list)

        #browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()


def scrap_more_data(hyperlink):
     try:
         page=requests.get(hyperlink)
         soap=BeautifulSoap(page.content,'html.parsel')
         temp_list=[]

         for tr_tag in soap.find_all('tr',attrs={'class':'fact_row'}):
             td_tags=tr_tag.find_all('td')

             for td_tag in td_tags:
                 try:
                     temp_list.append(td_tag.find_all('div',attrs={'class':'value'})[0].contents[0])
                 except:
                     temp_list.append(" ")

             new_planet_data.append(temp_list)
     except:
         time.sleep(1)
         scrap_more_data(hyperlink)#recursively calling the function

scrap()

for index,data in enumerate(planet_data):
    scrap_more_data(data[5])
    print(f'{index+1} page done')

for index,data in enumerate(planet_data):
    final_planet_data.append(data+final_planet_data[index])
    #new_planet_data_element=new_planet_data[index]



    with open('final.csv','w') as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(final_planet_data)

    




    

                
                

            

            



