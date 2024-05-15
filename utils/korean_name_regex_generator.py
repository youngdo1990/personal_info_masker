#################################################################################################### 
# AUTHOR: ALVARO ENRIQUE PERALTA GUTIERREZ (HWAN-HEE CHAE)                                         #
# PROJECT: KOREAN NAMES REGEX GENERATOR                                                            #
####################################################################################################

NAMES_FILE = "korean_names.txt"
LAST_NAMES_FILE = "korean_last_names.txt"


def generate_korname_regex():
    # 성 섭 정규 펴햔식 생성
    # Generate sub regular expression for last names
    korname_regex = "r\'\\b("
    last_names = open(LAST_NAMES_FILE, "r", encoding="utf-8", errors="ignore")
    names = open(NAMES_FILE, "r", encoding="utf-8", errors="ignore")
    names_list = []
    for name in names:
        names_list.append(name.strip())
    for last_name in last_names:
        for name in names_list:
            korname_regex += last_name.strip() + name + "|"
    # 마지막 '|' 지우기
    # Eliminate last '|'
    korname_regex = korname_regex[:-1] + ")\\b\'"
    last_names.close()
    names.close()
    with open("korname_regex.txt", "w", encoding="utf-8", errors="ignore") as file:
        file.write(korname_regex)
    return


if __name__ == "__main__":
    print("KOREAN REGEX GENERATOR")
    generate_korname_regex()