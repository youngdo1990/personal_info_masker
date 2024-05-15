#################################################################################################### 
# AUTHOR: ALVARO ENRIQUE PERALTA GUTIERREZ (HWAN-HEE CHAE)                                         #
# PROJECT: SAMPLE MAKER FOR PERSONAL INFO MASKER                                                   #
####################################################################################################
import os


SAMPLES_FOLDER = "samples"
CHATGPT_INTRODUCTIONS_FILE = "chatgpt_generated_introduction.txt"


def divide_samples():
    text_samples = []
    with open(CHATGPT_INTRODUCTIONS_FILE, encoding="utf-8", errors="ignore") as file:
        for f in file:
            text_samples.append(f.strip())
    text_samples = [t for t in text_samples if t != "안녕하세요!" and t != "감사합니다." and len(t) > 3]
    count = 1
    if not os.path.exists(SAMPLES_FOLDER):
        os.makedirs(SAMPLES_FOLDER)
    for t in text_samples:
        file_name = os.path.join(SAMPLES_FOLDER, "sample" + str(count) + ".txt")
        with open(file_name, "w", encoding="utf-8", errors="ignore") as file:
            file.write(t)
        count += 1
    return


if __name__ == "__main__":
    divide_samples()