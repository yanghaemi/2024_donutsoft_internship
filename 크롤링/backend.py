import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pymysql
# pymysql 임포트
import time
import re

# 전역 변수 선언부
conn = None
cur = None


def create_db_table():

    # 메인코드
    conn = pymysql.connect(host='127.0.0.1', user = 'root', password='4021', db='pythondb', charset='utf8')
    # 접속정보
    cur = conn.cursor()
    # 커서 생성

    sql1 = "CREATE TABLE IF NOT EXISTS albamonCB (id int, location VARCHAR(255), title VARCHAR(255), company VARCHAR(255), salary VARCHAR(255), chip VARCHAR(255), workingTime VARCHAR(255), uploadTime VARCHAR(255));"
    # 실행할 sql문
    sql2 = "CREATE TABLE IF NOT EXISTS albamonmega (id int, location VARCHAR(255), title VARCHAR(255), company VARCHAR(255), salary VARCHAR(255), chip VARCHAR(255), workingTime VARCHAR(255), uploadTime VARCHAR(255));"

    cur.execute(sql1) # 커서로 sql문 실행
    cur.execute(sql2)

    conn.commit() # 저장

    conn.close() # 종료

def clear_db():
    conn = pymysql.connect(host='127.0.0.1', user = 'root', password='4021', db='pythondb', charset='utf8')
    # 접속정보
    cur = conn.cursor()
    # 커서 생성
    
    sql_clear = "TRUNCATE TABLE albamoncb;"
    
    sql_clear2 = "TRUNCATE TABLE albamonmega"

    cur.execute(sql_clear)
    cur.execute(sql_clear2)

    conn.commit()
    conn.close()

size = 50

def extract_id(url):
    # 정규식을 이용하여 id 추출
    match = re.search(r'detail/(\d+)\?', url)
    if match:
        return match.group(1)
    else:
        print('실패실패')
        return None

def cb_job_posts_page(page):
    url_mon = f'https://www.albamon.com/jobs/area?page={page}&condition=%7B%22pagination%22%3A%7B%22page%22%3A{page}%2C%22size%22%3A{size}%7D%2C%22recruitListType%22%3A%22AREA%22%2C%22extensionCondition%22%3A%7B%22area%22%3A%7B%7D%2C%22brand%22%3A%7B%7D%2C%22franchise%22%3A%7B%7D%2C%22franchiseStore%22%3A%7B%7D%2C%22callCenter%22%3A%7B%7D%2C%22guerrilla%22%3A%7B%22guerrillaBoothTabNo%22%3A0%7D%2C%22map%22%3A%7B%22radius%22%3A120%2C%22zoom%22%3A0%7D%2C%22miniJob%22%3A%7B%7D%2C%22ongoing%22%3A%7B%7D%2C%22part%22%3A%7B%7D%2C%22pay%22%3A%7B%7D%2C%22preference%22%3A%7B%7D%2C%22recent%22%3A%7B%7D%2C%22scrap%22%3A%7B%7D%2C%22search%22%3A%7B%22disableExceptedConditions%22%3A%5B%5D%2C%22suitBannerNo%22%3A0%7D%2C%22season%22%3A%7B%7D%2C%22senior%22%3A%7B%7D%2C%22shortTerm%22%3A%7B%7D%2C%22specUp%22%3A%7B%7D%2C%22subway%22%3A%7B%7D%2C%22suit%22%3A%7B%7D%2C%22teenager%22%3A%7B%7D%2C%22town%22%3A%7B%22similarDongJoin%22%3Afalse%7D%2C%22trust%22%3A%7B%7D%2C%22university%22%3A%7B%7D%2C%22welfare%22%3A%7B%7D%2C%22albamonZ%22%3A%7B%7D%2C%22albamonZAdditional%22%3A%7B%22recruitNo%22%3A0%7D%7D%2C%22sortTabCondition%22%3A%7B%22searchPeriodType%22%3A%22ALL%22%2C%22sortType%22%3A%22DEFAULT%22%2C%22recruitListViewType%22%3A%22LIST%22%2C%22latitude%22%3A0%2C%22longitude%22%3A0%2C%22albamonZSortType%22%3A%22RECOMMEND%22%7D%2C%22condition%22%3A%7B%22areas%22%3A%5B%7B%22si%22%3A%22P000%22%2C%22gu%22%3A%22%22%2C%22dong%22%3A%22%22%2C%22name%22%3A%22%EC%B6%A9%EB%B6%81+%EC%A0%84%EC%B2%B4%22%7D%5D%2C%22similarDongJoin%22%3Afalse%2C%22parts%22%3A%5B%5D%2C%22excludeBar%22%3Afalse%2C%22workPeriodTypes%22%3A%5B%5D%2C%22workWeekTypes%22%3A%5B%5D%2C%22workDayTypes%22%3A%5B%5D%2C%22workTimeTypes%22%3A%5B%5D%2C%22excludeNegoAge%22%3Afalse%2C%22employmentTypes%22%3A%5B%5D%2C%22excludeKeywords%22%3A%5B%5D%2C%22selectedArea%22%3A%7B%22si%22%3A%22%22%2C%22gu%22%3A%22%22%2C%22dong%22%3A%22%22%7D%7D%7D&areas=P000--&size=50'
    data = requests.get(url_mon)
    soup = BeautifulSoup(data.text, 'html.parser')
    ul = soup.select_one('ul.SimpleRecruitList_simple-recruit-list__ul__5KKhf')
    locations = ul.select('li > div> div> div.list-item-recruit__contents--keyword-area')
    titles = ul.select('li > div > div > a > div > span.typography-paid')
    companies = ul.select('li > div > div > a > span.ListItemRecruit_list-item-recruit__company-name__bbljH')
    salaries = ul.select('li > div > div > span.list-item-recruit__salary')
    chips = ul.select('li > div > div > span.Chip_chip__7EkHk')
    _ids = ul.select('li > div > div > a.list-item-recruitgoogle-analytics ')
    workingTimes = ul.select('li > div > div.list-item-recruit__contents--time')
    dates = ul.select('li > div > div.list-item-recruit__contents--date')
    hrefs = [a['href'] for a in _ids] 
    ids = []
    for href in hrefs:
        ids.append(extract_id(href))
    # 제목만 출력

    for i in range(size):
        # print(locations[i].get_text())
        # print(titles[i].get_text())
        # print(companies[i].get_text())
        # print(salaries[i].get_text())
        # print(chips[i].get_text())
        # print(ids[i])
        # print(workingTimes[i].get_text())
        # print(dates[i].get_text())
        # print(i)
        # print(len(ids))
        print(f"충북 {i}번째 정보")

        
        try: #예외 처리 시작
            conn = pymysql.connect(host='127.0.0.1', user = 'root', password='4021', db='pythondb', charset='utf8')
# 접속정보
            cur = conn.cursor()
# 커서 생성
            sql_upload = "INSERT INTO albamoncb VALUES('" + ids[i] + "','" + locations[i].get_text() + "','" + titles[i].get_text() + "','" + companies[i].get_text() + "','" + salaries[i].get_text() + "','" + chips[i].get_text() + "','" + workingTimes[i].get_text() + "','" + dates[i].get_text() + "')"
            cur.execute(sql_upload)
        except Exception as e: #에러 발생 시 작동
            print("에러발생 -----------------------")
            print(e)
            break
        else : #에러 없을 시 작동
            print("DB 업로드 완료 =========================")
        finally:
            conn.commit()
            conn.close()
            print("\n")
    return None

def mega_job_posts_page(page):
    url_mon_2someplace = f'https://www.albamon.com/jobs/brand/normal/1060015?condition=%7B%22pagination%22%3A%7B%22page%22%3A{page}%2C%22size%22%3A{size}%7D%2C%22recruitListType%22%3A%22PART_BRAND%22%2C%22extensionCondition%22%3A%7B%22area%22%3A%7B%7D%2C%22brand%22%3A%7B%22brandCode%22%3A%221060015%22%2C%22brandKeyword%22%3A%22%ED%88%AC%EC%8D%B8%ED%94%8C%EB%A0%88%EC%9D%B4%EC%8A%A4%22%7D%2C%22franchise%22%3A%7B%7D%2C%22franchiseStore%22%3A%7B%7D%2C%22callCenter%22%3A%7B%7D%2C%22guerrilla%22%3A%7B%22guerrillaBoothTabNo%22%3A0%7D%2C%22map%22%3A%7B%22radius%22%3A120%2C%22zoom%22%3A0%7D%2C%22miniJob%22%3A%7B%7D%2C%22ongoing%22%3A%7B%7D%2C%22part%22%3A%7B%7D%2C%22pay%22%3A%7B%7D%2C%22preference%22%3A%7B%7D%2C%22recent%22%3A%7B%7D%2C%22scrap%22%3A%7B%7D%2C%22search%22%3A%7B%22disableExceptedConditions%22%3A%5B%5D%2C%22suitBannerNo%22%3A0%7D%2C%22season%22%3A%7B%7D%2C%22senior%22%3A%7B%7D%2C%22shortTerm%22%3A%7B%7D%2C%22specUp%22%3A%7B%7D%2C%22subway%22%3A%7B%7D%2C%22suit%22%3A%7B%7D%2C%22teenager%22%3A%7B%7D%2C%22town%22%3A%7B%22similarDongJoin%22%3Afalse%7D%2C%22trust%22%3A%7B%7D%2C%22university%22%3A%7B%7D%2C%22welfare%22%3A%7B%7D%2C%22albamonZ%22%3A%7B%7D%2C%22albamonZAdditional%22%3A%7B%22recruitNo%22%3A0%7D%7D%2C%22sortTabCondition%22%3A%7B%22searchPeriodType%22%3A%22ALL%22%2C%22sortType%22%3A%22POSTED_DATE%22%2C%22recruitListViewType%22%3A%22LIST%22%2C%22latitude%22%3A0%2C%22longitude%22%3A0%2C%22albamonZSortType%22%3A%22RECOMMEND%22%7D%2C%22condition%22%3A%7B%22areas%22%3A%5B%5D%2C%22similarDongJoin%22%3Afalse%2C%22parts%22%3A%5B%5D%2C%22excludeBar%22%3Afalse%2C%22workPeriodTypes%22%3A%5B%5D%2C%22workWeekTypes%22%3A%5B%5D%2C%22workDayTypes%22%3A%5B%5D%2C%22workTimeTypes%22%3A%5B%5D%2C%22excludeNegoAge%22%3Afalse%2C%22employmentTypes%22%3A%5B%5D%2C%22excludeKeywords%22%3A%5B%5D%7D%7D&sortType=POSTED_DATE&searchPeriodType=&latitude=&longitude=&areas='
    # 투썸 플레이스의 채용공고 url (최신 등록순)
    data = requests.get(url_mon_2someplace)
    soup = BeautifulSoup(data.text, 'html.parser')
    ul = soup.select_one('ul.SimpleRecruitList_simple-recruit-list__ul__5KKhf')
    locations = ul.select('li > div> div> div.list-item-recruit__contents--keyword-area')
    titles = ul.select('li > div > div > a > div > span.typography-paid')
    companies = ul.select('li > div > div > a > span.ListItemRecruit_list-item-recruit__company-name__bbljH')
    salaries = ul.select('li > div > div > span.list-item-recruit__salary')
    chips = ul.select('li > div > div > span.Chip_chip__7EkHk')
    _ids = ul.select('li > div > div > a.list-item-recruitgoogle-analytics ')
    workingTimes = ul.select('li > div > div.list-item-recruit__contents--time')
    dates = ul.select('li > div > div.list-item-recruit__contents--date')
    hrefs = [a['href'] for a in _ids] 
    ids = []
    for href in hrefs:
        ids.append(extract_id(href))
    # 제목만 출력

    for i in range(size):
        # print(locations[i].get_text())
        # print(titles[i].get_text())
        # print(companies[i].get_text())
        # print(salaries[i].get_text())
        # print(chips[i].get_text())
        # print(ids[i])
        # print(workingTimes[i].get_text())
        # print(dates[i].get_text())
        # print(len(ids))
        print(f"메가 커피 {i}번째 정보")
        
        try: #예외 처리 시작
            conn = pymysql.connect(host='127.0.0.1', user = 'root', password='4021', db='pythondb', charset='utf8')
# 접속정보
            cur = conn.cursor()
# 커서 생성
            sql_upload = "INSERT INTO albamonmega VALUES('" + ids[i] + "','" + locations[i].get_text() + "','" + titles[i].get_text() + "','" + companies[i].get_text() + "','" + salaries[i].get_text() + "','" + chips[i].get_text() + "','" + workingTimes[i].get_text() + "','" + dates[i].get_text() + "')"
            cur.execute(sql_upload)
        except Exception as e: #에러 발생 시 작동
            print("에러발생 -----------------------")
            print(e)
            break
        else : #에러 없을 시 작동
            print("DB 업로드 완료 =========================")
        finally:
            conn.commit()
            conn.close()
            print("\n")
    return None




headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 브라우저가 크롬일 때 이렇게 작성




# 메인코드
while True:
    create_db_table()
    for i in range(1, 6):
        cb_job_posts_page(i)
        mega_job_posts_page(i)
        print(f"-----------------{i}page---------------------")
        
    time.sleep(5) # 5초마다 반복
    clear_db()
    
