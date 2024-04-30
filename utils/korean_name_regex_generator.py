#################################################################################################### 
# AUTHOR: ALVARO ENRIQUE PERALTA GUTIERREZ (HWAN-HEE CHAE)                                         #
# PROJECT: KOREAN NAMES REGEX GENERATOR                                                            #
####################################################################################################

NAMES_FILE = "korean_names.txt"
LAST_NAMES_FILE = "korean_last_names.txt"


def generate_korname_regex():
    # 성 섭 정규 펴햔식 생성
    # Generate sub regular expression for last names
    last_names_substring = "("
    with open(LAST_NAMES_FILE, "r", encoding="utf-8", errors="ignore") as file:
        for last_name in file:
            last_names_substring += last_name.strip() + "|"
        last_names_substring = last_names_substring[:-1]
    last_names_substring += ")"
    # 이름 섭 정규 펴햔식 생성
    # Generate sub regular expression for names
    names_substring = "("
    with open(NAMES_FILE, "r", encoding="utf-8", errors="ignore") as file:
        for name in file:
            names_substring += name.strip() + "|"
        names_substring = names_substring[:-1]
    names_substring += ")"
    korname_regex = "r\'\\b" + last_names_substring + names_substring + "\\b\'"
    with open("korname_regex.txt", "w", encoding="utf-8", errors="ignore") as file:
        file.write(korname_regex)
    return


if __name__ == "__main__":
    print("KOREAN REGEX GENERATOR")
    generate_korname_regex()