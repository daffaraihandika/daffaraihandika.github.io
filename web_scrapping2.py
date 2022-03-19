from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import json
from datetime import datetime
import urllib.request

PATH = "C:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
count = 1
page = 1
data = []
now = datetime.now()
createnote = open('title_list.txt', 'w',encoding='utf-8')
createJson = open('hasil_scrap.json', 'w',encoding='utf-8')
driver.get("https://www.novelupdates.com/series-ranking/")
while(count<100):
    for anime in driver.find_elements(by=By.CLASS_NAME,value='search_main_box_nu'):
        count_string = '#' + str(count)
        title = anime.find_element(by=By.CLASS_NAME,value='search_title')
        temp_title = title.text
        title = temp_title.replace(count_string,'')
        ratings = anime.find_element(by=By.CLASS_NAME,value='search_ratings').text
        origin,rating = ratings.split(' ')
        genre = anime.find_element(by=By.CLASS_NAME,value='search_genre').text
        link_cover = anime.find_element(by=By.TAG_NAME,value='img').get_attribute('src')
        for image in anime.find_elements_by_tag_name("img"):
            urllib.request.urlretrieve(image.get_attribute("src"), str(count)+".png")
            break
        print(str(count),'. ',title,ratings,genre,link_cover)
        createnote.write(title)
        createnote.write(" ")
        createnote.write(ratings)
        createnote.write('\n')
        data.append({"Judul": title,
                 "Genre": genre , 
                 "rating": rating,
                 "origin": origin,
                 "img_src" : image.get_attribute("src"),
                 "Waktu_scrapping": now.strftime("%d/%m/%Y %H:%M:%S")})
        if count>=100:
            break
        count+=1
    try:
        page+=1
        driver.find_element(by=By.CLASS_NAME,value="digg_pagination").find_element(by=By.PARTIAL_LINK_TEXT, value=str(page)).click()
    except NoSuchElementException as e:
        break;
createnote.close()
jdumps = json.dumps(data, indent=5)
createJson.writelines(jdumps)
createJson.close()
driver.quit()