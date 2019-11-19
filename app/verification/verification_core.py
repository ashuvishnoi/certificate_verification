import cv2
import pytesseract
from configuration import maxx, minn
import logging
import base64


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(filename)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    logging.info('text extraction done')
    return text


def get_structures(image):
    res = []
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU, img)
    cv2.bitwise_not(img, img)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, rect_kernel)
    im, contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            roi = image[y:y + h, x:x + w]
            if minn < h < maxx:
                string = base64.b64encode(cv2.imencode('.jpg', roi)[1]).decode()
                data = {'image': string}
                res.append(data)

    logging.info('logo extraction done')
    return res

