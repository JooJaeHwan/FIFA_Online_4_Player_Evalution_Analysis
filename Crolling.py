from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict
# 크롤링
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
df =  pd.read_csv('Player.csv', index_col=0)
reviews_dic = defaultdict(list)
for i in range(len(df)):
    for j in range(1, 100):
        url = 'https://fifaonline4.inven.co.kr/dataninfo/rate/index.php?pg={}|searchword={}|season={}'.format(j, df.iloc[i][1], df.iloc[i][2])
        driver.get(url)
        driver.implicitly_wait(5)
        html = driver.page_source 
        soup = BeautifulSoup(html, 'html.parser')
        temp = [i.text.strip() for i in soup.select('#fifaonline4Db > div.fifa4.db_board.board_style01.board_rate > div > table > tbody')]
        if temp[0] == '검색한 데이터가 존재하지 않습니다.':
            break
        data = temp[0].split("\n")
        for z in range(3,len(data),22):
            reviews_dic["name"].append(df.iloc[i][1])
            reviews_dic["class_id"].append(df.iloc[i][2])
            reviews_dic["rate"].append(data[z])
            reviews_dic["reviews"].append(data[z+2])
    print('{}명의 데이터를 수집했습니다'.format(i+1))
    result = pd.DataFrame(reviews_dic)
    result.to_csv("Reviews2.csv")
# webdriver 종료
driver.close()

print("최종 완료")
result.to_csv("Reviews2.csv")