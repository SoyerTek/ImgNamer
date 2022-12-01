from fileinput import filename
from PIL import Image
from pytesseract import pytesseract
import os

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

path_img_folder = r'images'

for img_name in os.listdir(path_img_folder):

    #Define path to image
    path_to_image = os.path.join(path_img_folder, img_name)

    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    #Open image with PIL
    img = Image.open(path_to_image)

    #Original image size
    width, height = img.size

    # Setting the points for cropped image
    left = 0
    top = 0
    right = width*0.8
    bottom = height / 2.5

    img = img.crop((left, top, right, bottom))

    #Extract text from image
    text = pytesseract.image_to_string(img)
    
    print(text)

    #text cleanup
    text = text.replace('$', 'S');
    text = text.replace("£", "E")
    text = text.split('|')[0];
    text = text.split();

    title = 'RaimondoF'
    for x in text:
        title += '_' + x

    title = title.replace(":", "");
    title = title.replace("/", "");
    print(title)
    #add extension to filename
    title += ".jpg";

    print(title)

    try:
        os.rename(path_to_image, os.path.join(path_img_folder, title))
    except:
        print("errore")