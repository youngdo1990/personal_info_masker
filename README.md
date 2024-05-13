# 🪪개인 정보 마스커
<a href="./README_eng.md"><img src="./img/flags/us.png" height="20px"></img> READ ENGLISH VERSION</a>
## ⬇️ 리포지토리 내려받기
```
git clone https://github.com/youngdo1990/personal_info_masker.git
```
## 🏞️ 가상 환경 설정
```
mkvirtualenv info_masker
cd personal_info_masker
pip install -r requirements.txt
```
## 📄 한국인 이름 리스트 만드는 과정
전화번호, 이메일, 주소는 정규 표현식으로 추출할 수 있는데 사람 이름 겨우에는 쉽게 구현할 수 있는 정규 표현식이 없다. 그 때문에 이름, 성 리스트를 만들 수 밖에 없다.<br />
이름 리스트 만들기 위해서 웹 크롤링으로 이름과 성 리스트를 생성했다.<br /><br />
<b>이름 리스트 출처:</b> <br />
<a href="https://www.name-ranking.com/ranking#from=2008&to=2024&p=577">https://www.name-ranking.com/ranking#from=2008&to=2024&p=577</a></br>
<b>성 리스트 출처:</b> <br />
<a href="https://namu.wiki/w/%ED%95%9C%EA%B5%AD%EC%9D%98%20%EC%84%B1%EC%94%A8%EB%B3%84%20%EC%9D%B8%EA%B5%AC%20%EB%B6%84%ED%8F%AC">https://namu.wiki/w/%ED%95%9C%EA%B5%AD%EC%9D%98%20%EC%84%B1%EC%94%A8%EB%B3%84%20%EC%9D%B8%EA%B5%AC%20%EB%B6%84%ED%8F%AC</a>.
### 📋 이름, 성씨 리스트 생성
한국 성씨와 이름 리스트를 만들기 위해서 <b>korean_name_crawler.py</b> 스크립트를 실행하면 된다.
```
cd utils
python korean_name_crawler.py
```
### 🔣 한국 이름 정규 푤현식 생성
한국 성씨와 이름 리스트를 만든 후 파이썬 정규 표현식을 생성해야 한다. 한국 이름 정규 표현삭울 먼둘가 위해서 크롤링된 한국 성 씨와 이름을 조합하고 정규 표현식으로 바꿔야 했다. 추출한 한국 이름 정규 표현식을 만들기 위해서 <b>korean_name_regex_generator.py</b> 스크립트를 실행하면 된다.
```
python korean_name_regex_generator.py
```
스크립트를 실행하면 <b>korname_regex.txt</b> 파일 생성한다. <b>personal_info_masker.py</b> 스크립은 <b>korname_regex.txt</b> 파일을 적재하고 한국 이름을 추출할 수 있는 정규 표현식으로 이용한다. <b>korname_regex.txt</b> 파일은 다음과 보인다.
