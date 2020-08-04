import requests
from bs4 import BeautifulSoup

# 네이버 영화 -> 상영작 -> 제목(title)과 번호(num) 출력하기
base_URL = 'https://movie.naver.com/movie/running/current.nhn'

# 네이버 무비에 리퀘스트를 요청해서 naver_moves 에 객체 저장
naver_movies = requests.get(base_URL)
# naver_movies에 text 파일을 불러오는데, html로 불러온다(?????)
soup = BeautifulSoup(naver_movies.text, 'html.parser')
naver_a = soup.select(
    "div[id=wrap] > div[id=container] > div[id=content] > div[class=article] > div[class=obj_section] > div[class=lst_wrap] > ul[class=lst_detail_t1] > li")


# print(len(naver_a))

movie_data = {
    "title" : "",
    "code" : ""
}
for movie in naver_a:
    movie_data['title'] = movie.select_one('dl > dt > a').text
    movie_data['code'] = movie.select_one('dl > dt > a')['href'].split("code=")[-1]

    print(movie_data, '\n')