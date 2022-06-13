from PIL import Image


def genData(data):
    newdata = []
    for i in data:
        newdata.append(format(ord(i), '08b'))
    return newdata


def modPixel(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):
        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]

        for j in range(0,8):
            if(datalist[i][j]=='0' and pix[j]% 2 !=0):
                pix[j] -=1
            elif(datalist[i][j]=='1' and pix[j]% 2 ==0):
                if(pix[j] !=0):
                    pix[j] -= 1
                else:
                    pix[j] += 1

        if (i == lendata - 1):
            if(pix[-1]% 2 == 0):
                if (pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[j] += 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
    for pixel in modPixel(newimg.getdata(), data):
        newimg.putpixel((x, y), pixel)
        if( x == w - 1 ):
            x = 0
            y += 1
        else:
            x += 1

def encode():
    image = Image.open('in.JPG', 'r')

    data = open('../encode/Document.pdf.encoded', 'r', encoding='utf8', errors='ignore')
    data = data.read()

    if(len(data) == 0):
        raise ValueError('Data is Empty')
    newimg = image.copy()
    encode_enc(newimg, data)

    new_img_name = 'hide.png'
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))


def decode():
    image = Image.open('hide.png', 'r')
    data = ''
    imgdata = iter(image.getdata())
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
								imgdata.__next__()[:3] +
								imgdata.__next__()[:3]]
        # string of binary data
        binstr = ''
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
        data += chr(int(binstr, 2))

        if (pixels[-1] % 2 != 0):
            datas = open('hide.pdf.encoded', 'w', encoding='utf8', errors='ignore')
            datas.write(data)
            return data

def main():
    encode()
    decode()


if __name__ == '__main__':
    main()
