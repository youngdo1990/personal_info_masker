# 🪪개인 정보 마스커
<a href="./README_eng.md"><img src="./img/flags/us.png" height="20px"></img> READ ENGLISH VERSION</a>
&nbsp;
<a href="./README_eng.md"><img src="./img/flags/kr.png" height="20px"></img> 한국어 버전 보기</a><br /><br />
Este es un programa que utiliza expresiones regulares para proteger la información personal de las personas.
## ⬇️ Descarga del Repositorio
```
git clone https://github.com/youngdo1990/personal_info_masker.git
```
## 🏞️ Creación del Entorno Virtual
```
mkvirtualenv info_masker
cd personal_info_masker
pip install -r requirements.txt
```
## 📄 Creación de una Lista de Nombres y Apellidos Coreanos
Aunque se puede crear una expresión regular para los teléfonos, emails y direcciones, es muy difícil crear una para los nombres de las personas. Por ese motivo, es necesario crear una lista de nombres y apellidos.<br />
La creación de la lista de nombres y apellidos se realiza mediante web scraping.<br /><br />
<b>Fuente de los nombres:</b> <br />
<a href="https://www.name-ranking.com/ranking#from=2008&to=2024&p=577">https://www.name-ranking.com/ranking#from=2008&to=2024&p=577</a></br>
<b>Fuente de los Apellidos:</b> <br />
<a href="https://namu.wiki/w/%ED%95%9C%EA%B5%AD%EC%9D%98%20%EC%84%B1%EC%94%A8%EB%B3%84%20%EC%9D%B8%EA%B5%AC%20%EB%B6%84%ED%8F%AC">https://namu.wiki/w/%ED%95%9C%EA%B5%AD%EC%9D%98%20%EC%84%B1%EC%94%A8%EB%B3%84%20%EC%9D%B8%EA%B5%AC%20%EB%B6%84%ED%8F%AC</a>.
### 📋 Generación de una Lista de Nombres y Apellidos
Para generar una lista de nombres y apellidos se debe utilizar el script <b>korean_name_crawler.py</b>.
```
cd utils
python korean_name_crawler.py
```
### 🔣 Generación de una Expresión Regular para Nombres Coreanos
한국 성씨와 이름 리스트를 만든 후 파이썬 정규 표현식을 생성해야 한다. 한국 이름 정규 표현삭울 먼둘가 위해서 크롤링된 한국 성 씨와 이름을 조합하고 정규 표현식으로 바꿔야 했다. 추출한 한국 이름 정규 표현식을 만들기 위해서 <b>korean_name_regex_generator.py</b> 스크립트를 실행하면 된다.
```
python korean_name_regex_generator.py
```
스크립트를 실행하면 <b>korname_regex.txt</b> 파일 생성한다. <b>personal_info_masker.py</b> 스크립은 <b>korname_regex.txt</b> 파일을 적재하고 한국 이름을 추출할 수 있는 정규 표현식으로 이용한다. <b>korname_regex.txt</b> 파일은 다음과 보인다.<br /><br />
<img src="./img/korname_regex_file.png"></img><br />
## ⚗️ 테스팅
개인 정보 마스커를 테스팅하기 위해서 ChatGPT로 가짜 정보를 이용하는 자기소개 50개를 생성했다. OpenAI API Key 없어서 ChatGPT가 생성한 자기소개를 복사하고 텍스트 파일에 저장했다. 파일 이름은 <b>chatgpt_generated_introduction.txt</b>이며 다음과 보인다.<br /><br />
<img src="./img/chatgpt_samples.png"></img><br />
자기소개 내용만 필요해서 '안녕하세요!', 사인과 '감사합니다'를 담고 있는 라인을 제거하고 샘플 파일을 생성하기 위해서 <b>./utils/sample_maker.py</b> 스크립트를 실행한다.<br />
```
cd utils
python sample_maker.py
```
스크립트를 실행하면 sample1.txt부터 sample50.txt까지 담은 폴더를 생성한다. 샘플 파일은 다음과 보인다.<br /><br />
<img src="./img/sample_file.png"></img><br />
마지막으로 마스킹 테스팅하기 위해서 "test.py" 스크립트를 실행한다.<br /><br />
```
python test.py
```
"test.py" 스크립트는 샘플 파일 텍스트 적재하고 마스크를 한 다음에 <b>./utils/output</b> 폴더에 마스크된 텍스트를 저장한다. 마스크 된 파일 예시는 <b>./utils/outputs/sample47.txt</b>이고, 다음과 보인다.<br /><br />
<img src="./img/output_file.png"><br />
