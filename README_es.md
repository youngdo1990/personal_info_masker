# 🪪 Enmascarador de Información Personal
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
Después de crear una lista de apellidos y nombres coreanos, se debe generar una expresión regular en Python. Para la generación de la expresión regular de nombres coreanos, fue necesario combinar y convertir los apellidos y nombres coreanos obtenidos mediante web scraping en una expresión regular. Para crear la expresión regular de nombres coreanos extraídos, simplemente ejecuta el script korean_name_regex_generator.py.
```
python korean_name_regex_generator.py
```
Al ejecutar el script se creará el archivo <b>korname_regex.txt</b>. El script <b>personal_info_masker.py</b> utilizará el archivo <b>korname_regex.txt</b> como una expresión regular para encontrar los nombres coreanos.<br /><br />
<img src="./img/korname_regex_file.png"></img><br />
## ⚗️ Testing
Para probar el enmascarador de información personal, generé con ChatGPT 50 ejemplos de presentaciones personales en coreano. Como no tengo la API Key de OpenAI, simplemente pedí a ChatGPT que generara los 50 ejemplos con información personal falsa. Luego, copié y guardé los ejemplos en el archivo <b>chatgpt_generated_introduction.txt</b>, que se ve como se muestra en la imagen a continuación.<br /><br />
<img src="./img/chatgpt_samples.png"></img><br />
Como solo se necesita el contenido de la presentacion personal, se eliminan los token innecesarios como '안녕하세요!', '감사합니다' y la firma. Para realizar este proceso se debe correr el script <b>./utils/sample_maker.py</b>.<br />
```
cd utils
python sample_maker.py
```
Al correr el script se generan los archivos desde sample1.txt hasta sample50.txt. La imagen a continuación es un ejemplo de un archivo de ejemplo.<br /><br />
<img src="./img/sample_file.png"></img><br />
마지막으로 마스킹 테스팅하기 위해서 "test.py" 스크립트를 실행한다.<br /><br />
```
python test.py
```
"test.py" 스크립트는 샘플 파일 텍스트 적재하고 마스크를 한 다음에 <b>./utils/output</b> 폴더에 마스크된 텍스트를 저장한다. 마스크 된 파일 예시는 <b>./utils/outputs/sample47.txt</b>이고, 다음과 보인다.<br /><br />
<img src="./img/output_file.png"><br />
