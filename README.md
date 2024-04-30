# 👮개인 정보 마스커
<a href="./README_eng.md"><img src="./img/flags/us.png" height="20px"></img> READ ENGLISH VERSION</a>
## ⬇️ 리포지토리 내려받기
```
git clone https://github.com/youngdo1990/personal_info_masker.git
```
## 📄 한국인 이름 리스트 만드는 과정
전화번호, 이메일, 주소는 정규 표현식으로 추출할 수 있는데 사람 이름 겨우에는 쉽게 구현할 수 있는 정규 표현식이 없다. 그 때문에 이름, 성 리스트를 만들 수 밖에 없다.<br />
이름 리스트 만들기 위해서 웹 크롤링으로 이름과 성 리스트를 생성했다.<br /><br />
<b>이름 리스트 출처:</b> <br />
<a href="https://www.name-ranking.com/ranking#from=2008&to=2024&p=577">https://www.name-ranking.com/ranking#from=2008&to=2024&p=577</a></br>
<b>성 리스트 출처:</b> <br />
<a href="https://namu.wiki/w/%ED%95%9C%EA%B5%AD%EC%9D%98%20%EC%84%B1%EC%94%A8%EB%B3%84%20%EC%9D%B8%EA%B5%AC%20%EB%B6%84%ED%8F%AC">https://namu.wiki/w/%ED%95%9C%EA%B5%AD%EC%9D%98%20%EC%84%B1%EC%94%A8%EB%B3%84%20%EC%9D%B8%EA%B5%AC%20%EB%B6%84%ED%8F%AC</a>.
### 📋 이름, 성씨 리스트 및 정규 표현식 생성
한국 성씨와 이름 리스트를 만들기 위해서 <b>korean_name_crawler.py</b> 스크립트를 실행하면 된다.
```
cd utils
python korean_name_crawler.py
```
