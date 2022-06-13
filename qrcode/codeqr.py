import qrcode
import cv2


def main():

    content = open('../encode/Document.pdf.encoded', 'r')
    j = 0
    # 2325
    for i in range(0, len(content.read()), 2325):
        # print(i)
        content = open('../encode/Document.pdf.encoded', 'r')
        qr = qrcode.QRCode()
        qr.add_data(content.read()[i:i+2325])
        # print("okay"+str(j))
        qr.make()
        img_qr = qr.make_image()
        img_qr.save("qr_"+str(j)+".png")
        j = j+1
    print(j)

    for i in range(0, j):
        filename = "qr_"+str(i)+".png"
        print(i)
        image = cv2.imread(filename)
        detector = cv2.QRCodeDetector()
        data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
        print(data)
        with open('qr.pdf.encoded', 'a') as fichier:
            fichier.write(data)


if __name__ == '__main__':
    main()
