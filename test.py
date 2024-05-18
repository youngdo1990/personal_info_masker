#################################################################################################### 
# AUTHOR: ALVARO ENRIQUE PERALTA GUTIERREZ (HWAN-HEE CHAE)                                         #
# PROJECT: INFO MASKER TESTER                                                                      #
####################################################################################################
import os
from personal_info_masker import *
from tqdm import tqdm


SAMPLE_FOLDER = os.path.join(".", "utils", "samples")
OUTPUT_FOLDER = os.path.join(".", "utils", "outputs")


def sample_list():
    files = os.listdir(SAMPLE_FOLDER)
    files = [os.path.join(SAMPLE_FOLDER, f) for f in files if f.startswith("sample")]
    return files


def mask_samples(keep_original=True):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    samples = sample_list()
    for sample in tqdm(samples):
        input_file = open(sample, "r", encoding="utf-8", errors="ignore")
        text = input_file.read()
        input_file.close()
        output_file_name = sample.split(os.path.sep)[-1]
        output_file_name = os.path.join(OUTPUT_FOLDER, output_file_name)
        masked_text = personal_info_masker(text)
        output_file = open(output_file_name, "w", encoding="utf-8", errors="encoding")
        if keep_original:
            output_file.write("="*8 + "원본" + "="*8 + "\n")
            output_file.write(text + "\n")
            output_file.write("="*20 + "\n")
        output_file.write("="*3 + "마스크된 택스트" + "="*3 + "\n")
        output_file.write(masked_text + "\n")
        output_file.write("="*20 + "\n")
        output_file.close()
        
    return


if __name__ == "__main__":
    mask_samples()
