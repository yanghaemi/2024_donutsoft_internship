import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pymysql
# pymysql 임포트

# 전역 변수 선언부
conn = None
cur = None

sql = ""

# 메인코드
conn = pymysql.connect()



headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 브라우저가 크롬일 때 이렇게 작성
url_mon = 'https://www.albamon.com/'
url_mon_2someplace = 'https://www.albamon.com/jobs/brand/normal/1060015'
# 투썸 플레이스의 채용공고 url

data = requests.get(url_mon_2someplace)

soup = BeautifulSoup(data.text, 'html.parser')
ul = soup.select_one('ul.SimpleRecruitList_simple-recruit-list__ul__5KKhf')
titles = ul.select('li > div > div > a')
# 제목만 출력

driver = webdriver.Chrome()
url= 'https://www.google.com'
driver.get(url)

# 이 이후로 필요한 부분 추출
for title in titles:
    print(title.get_text())

