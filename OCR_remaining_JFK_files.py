# OCR the remaining JFK files

from pydoc import doc
from pdf2image import convert_from_path
import os, pickle, time
from utils.whoopsie import whoopsie
from utils.pickle_it import pickle_it

from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


with open("left_to_ocr.pkl", 'rb') as f:
    docs_remaining = pickle.load(f)


def extract_imgs (filename) :

    # The first 10 pages of each document will be plenty
    images = convert_from_path('docs2/' + filename)[:10]

    os.mkdir('batch2processing/img_dump/' + filename[:-4])

    for i, image in enumerate(images):
        fname = "batch2processing/img_dump/" + filename[:-4] + "/image" + str(i) + ".png"
        image.save(fname, "PNG")


def ocr_doc (basedir, dir) :
    doc = ''
    
    for img in os.listdir(basedir + dir):
        doc = doc + pytesseract.image_to_string(Image.open(basedir + dir + '/' + img))

    with open('batch2processing/txt_dump/' + dir + '.txt', 'w') as f:
        f.write(doc)

t0 = time.time()
t1 = t0
n = len(docs_remaining)
print(f"OCRing up to the first ten pages from each of {n} image PDFs.")
for i in range(0, n):
# for pdf in texts_not_dumped:
    doc = docs_remaining[i]
    try:
        extract_imgs(doc + ".pdf")
    except Exception as exc:
        whoopsie(str(exc))
    try:
        ocr_doc('batch2processing/img_dump/', doc)
    except Exception as exc:
        whoopsie(str(exc))
    if i % 100 == 0:
        t2 = time.time()
        print(f"{i} of {n} docs OCRed. {t2 - t1} s elapsed this cycle of 100 docs, {t2 - t0} s elapsed since processing began.")
        t1 = time.time()
    
print(f"Done OCRing {i} JFK docs.")