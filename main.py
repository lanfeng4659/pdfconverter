# /mnt/e/projects/pdf_parse/test_datas/2005.10513.pdf
import os
import pdfplumber
def _makedirs(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
def _assert_dir_of_path(path):
    dir_name = os.path.dirname(path)
    _makedirs(dir_name)
    return path

RESULT_DIRS = './output'
pdf_file = '/mnt/e/projects/pdf_parse/test_datas/2005.10513.pdf'
pdf = pdfplumber.open(pdf_file)

for idx, page in enumerate(pdf.pages):
    # if idx != 3:
    #     continue
    im = page.to_image(resolution=72*4)
    # words = page.extract_words(
    #         x_tolerance=10,
    #         y_tolerance=1.2,
    #         ignore_blank_chars=True,
    #     )
    words = page.extract_text_lines()
    texts = [t['text'] for t in words]
  
    print(''.join(texts))
    # print(page.extract_text())
    im.draw_rects(words)
    # im.draw_rects(
    #     page.extract_text_lines(
    #     )
    # )
    # print(words)
    print('Save Done!')
    im.save(
        _assert_dir_of_path(os.path.join(RESULT_DIRS, f'page_{idx}.png'))
        )
