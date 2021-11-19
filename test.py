import pytesseract
from pdf2image import convert_from_path
import os

os.chdir(os.getcwd())

# pytesseract.pytesseract.tesseract_cmd = '<path-to-tesseract-bin>'


def tess_ocr(fname, lang):
	dirname = fname.rsplit('.', 1)[0]
	if not os.path.exists(dirname):
		os.mkdir(dirname)
	images = convert_from_path(fname, fmt='png', output_folder=dirname)
	text = ''
	for img in images:
		text += pytesseract.image_to_string(img, lang=lang)

	with open('result.txt', 'w', encoding='utf-8') as f:
		f.write(text)
	return text

fname = '1.pdf'
text = tess_ocr(fname, lang='chi_sim')
