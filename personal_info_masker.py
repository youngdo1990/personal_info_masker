#################################################################################################### 
# AUTHOR: ALVARO ENRIQUE PERALTA GUTIERREZ (HWAN-HEE CHAE)                                         #
# PROJECT: PERSONAL INFO MASKER                                                                    #
####################################################################################################
import re
import os
import sys
import argparse
from datetime import datetime
from tqdm import tqdm


# 한국어 교착어이어서 개인 정보는 이다 동사와 붙여 있을 수도 있다.
# 이러한 문제 다루기 위해서 이다 동사 변경 정규 표현식을 만들 필요가 있다.
# Korean language is an agglutinative language, so personal information can appear in from of 이다(Koren To Be Verb).
# In order to face this problem is neccesary to make a pattern for 이다 verb in its different forms.
# 이다 정규 표현식
# 한국 전화번호 정규 표현식
KOREAN_TO_BE_PATTERN = r"(이다[\W]?|입니다[\W]?|이에요[\W]?|예요[\W]?|야[\W]?|이야[\W]?|이고[\W]?|인데[\W]?|이잖아[\W]?|이잖아요[\W]?|이라고[\W]?)"
# Korean phone number regular expression
PHONE_PATTERN = r"\d{2,3}[-|\s]\d{3,4}[-|\s]\d{4}"
# 이메일 주소 정규 표현식
# Email address regular expression
EMAIL_PATTERN = r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}"
# 주민동록 번호 정규 표현식
# Korean id number regular expression
ID_PATTERN = r'\d{6}-\d{7}'
# URL 정규 표현식
# URL regular expression
URL_PATTERN = r'\b(https?|ftp|file)://\S+'
# 신용 카드 정규 표현식
# Credit card regular expressions
VISA_PATTERN = r'4[0-9]{12}(?:[0-9]{3})?'
MASTERCARD_PATTERN = r'5[1-5][0-9]{14}'
AMERICAN_PATTERN = r'3[47][0-9]{13}'
DINERSCLUB_PATTERN = r'3(?:0[0-5]|[68][0-9])[0-9]{11}'
DISCOVER_PATTERN = r'6(?:011|5[0-9]{2})[0-9]{12}'
JCB_PATTERN = r'(?:2131|1800|35\d{3})\d{11}'


# 이다 문제점 다루기 위해서 이다 동사 나오는 곳으로 텍스트를 나누기
# To face 이다(Korean To Be) Verb problem the text is divided when 이다 appears
def split_ida(text):
    text = re.split(KOREAN_TO_BE_PATTERN, text)
    text = ' '.join(text)
    return text


# 텍스트의 원래 형태를 복구(추가된 띄어쓰기 제거하기)
# Recover original text form(Eliminate incorpored spaces)
def join_ida(text):
    text = re.split(KOREAN_TO_BE_PATTERN, text)
    text = [t[:-1] if t[-1] == " " else t for t in text]
    text = ''.join(text)
    return text


def complex_mask(text, info_type):
    if info_type == "phone":
        pattern = PHONE_PATTERN
        separator = "-"
    elif info_type == "email":
        pattern = EMAIL_PATTERN
        separator = "@"
    substrings = re.findall(pattern, text)
    return text


def mask_korean_name(text):
    with open(os.path.join("utils", "korname_regex.txt"), "r", encoding="utf-8", errors="ignore") as file:
        name_regex = file.read()
    text = re.sub(eval(name_regex), "***", text)
    return text


def credit_card_masker(text):
    text = re.sub(VISA_PATTERN, "****-****-****-****", text)
    text = re.sub(MASTERCARD_PATTERN, "****-****-****-****", text)
    text = re.sub(AMERICAN_PATTERN, "****-****-****-****", text)
    text = re.sub(DISCOVER_PATTERN, "****-****-****-****", text)
    text = re.sub(JCB_PATTERN, "****-****-****-****", text)
    return text


def personal_info_masker(text):
    text = split_ida(text)
    text = mask_korean_name(text)
    text = re.sub(PHONE_PATTERN, '***-****-****', text)
    text = re.sub(EMAIL_PATTERN, '**********@**********', text)
    text = re.sub(ID_PATTERN, '******-*******', text)
    text = re.sub(URL_PATTERN, '<URL>', text)
    text = credit_card_masker(text)
    text = join_ida(text)
    return text


def mask_text(text):
    new_text = personal_info_masker(text)
    return new_text


def mask_single_file(file):
    if not os.path.exists(file):
        print("지정된 파일이 존재하지 않습니다.")
        sys.exit()
    with open(file, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    new_text = mask_text(text)
    return new_text



def mask_multiple_files(folder, output_folder=None):
    if not os.path.exists(folder):
        print("지정된 폴더가 존재하지 않습니다.")
        sys.exit()
    files = os.listdir(folder)
    files = [f for f in files if f.endswith(".txt")]
    if output_folder is None:
        output_folder = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for file in files:
        new_text = mask_single_file(os.path.join(folder, file))
        output_file = os.path.join(output_folder, file)
        with open(output_file, "w", encoding="utf-8", errors="ignore") as f:
            f.write(new_text)
    return


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--text', help='마스크를 하고 싶은 텍스트')
    group.add_argument('--file', help='마스크를 하고 싶은 텍스트 파일')
    group.add_argument('--folder', help='마스킹하고 싶은 텍스트 파일이 담긴 폴더')
    parser.add_argument('--output_folder', help='마스킹된 텍스트 파일이 담긴 폴더')
    args = parser.parse_args()
    if args.text is None and args.file is None and args.folder is None:
        print("--text나 --file나 --folder 파라미터를 지정하면 됩니다.")
    if args.text is not None:
        new_text = mask_text(args.text)
        print(new_text)
    elif args.file is not None:
        new_text = mask_single_file(args.file)
        if args.output_folder is not None:
            if not os.path.exists(args.output_folder):
                os.makedirs(args.output_folder)
            print(args.output_folder)
            file_name = datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + "_output.txt"
            output_file_name = os.path.join(args.output_folder, file_name)
            with open(output_file_name, "w", encoding="utf-8", errors="ignore") as file:
                file.write(new_text)
        else:
            print(new_text)
    else:
        mask_multiple_files(args.folder, args.output_folder)
    return


if __name__ == "__main__":
    main()