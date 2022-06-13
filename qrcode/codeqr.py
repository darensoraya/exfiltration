import qrcode
from PIL import Image
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader



def main():
    # code pour transformer le fichier en png
    # images = convert_from_path('../encode/Document.pdf.encoded')
    # for image in images:
        # image.save('out.png','PNG')
    # PDF_read = PdfFileReader(content)
    # page_1 = PDF_read.getPage(0)
    # print(page_1.extractText())

    content = open('../encode/Document.pdf.encoded', 'r')
    j = 0
    # 2325
    for i in range(0, len(content.read()), 2325):
        # print(i)
        content = open('../encode/Document.pdf.encoded', 'r')
        qr = qrcode.QRCode()
        qr.add_data(content.read()[i:i+2325])
        print("okay"+str(j))
        qr.make()
        img_qr = qr.make_image()
        img_qr.save("qr_"+str(j)+".png")
        j = j+1




if __name__ == '__main__':
    main()
