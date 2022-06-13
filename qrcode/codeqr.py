import qrcode
from PIL import Image
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader



def main():
    # code pour transformer le fichier en png
    # images = convert_from_path('../encode/Document.pdf.encoded')
    # for image in images:
        # image.save('out.png','PNG')

    content = open('../encode/Document.pdf.encoded', 'r')
    # PDF_read = PdfFileReader(content)
    # page_1 = PDF_read.getPage(0)
    # print(page_1.extractText())
    print(len(content.read()))
    print(type(content.read()))
    text = content.read()
    print(text)
    j = 0
    for i in range(0, len(content.read()), 2325):
        qr = qrcode.QRCode()
        qr.add_data(i)
        qr.make()
        img_qr = qr.make_image()
        img_qr.save("qr_"+j+".png")
        j = +1




if __name__ == '__main__':
    main()
