import argparse
import io
import sys
from subprocess import check_output

import cv2
import pytesseract
import requests
from PIL import Image


def resolve(path: str) -> str:
    # print("Resampling the Image")
    # check_output(['convert', path, '-resample', '600', path])
    response = requests.get(path)
    content = io.BytesIO(response.content)
    img = Image.open(content)

    # image = cv2.imread(img)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image = cv2.medianBlur(image, 3)
    # image = cv2.imread(img)

    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # gray = cv2.medianBlur(gray, 3)
    # filename = {}.png.format(temp)
    # cv2.imwrite(filename, gray)

    # img = Image.open(gray)
    solved_capctha = pytesseract.image_to_string(img)
    print(solved_capctha, "solved")
    return solved_capctha


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-i", "--image", required=True, help="path to input image to be OCR'd"
    )
    args = vars(argparser.parse_args())
    path = args["image"]
    print("-- Resolving")
    captcha_text = resolve(path)
    print("-- Result: {}".format(captcha_text))
