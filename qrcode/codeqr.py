import qrcode
from PIL import Image
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader



def main():
    # code pour transformer le fichier en png
    images = convert_from_path('test_2.pdf')
    for image in images:
        image.save('out.png','PNG')

    content = open('test_2.pdf', 'rb')
    PDF_read = PdfFileReader(content)
    page_1 = PDF_read.getPage(0)
    print(page_1.extractText())
    qr = qrcode.QRCode(box_size=4)
    qr.add_data(page_1.extractText())
    qr.make()
    img_qr = qr.make_image()
    img_qr.save("qr_1.png")


if __name__ == '__main__':
    main()
