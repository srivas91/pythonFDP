from PIL import Image,ImageFilter

def blackwhite():
    srcimg="C:\\Users\\admin\\Pictures\\clrdhoni.jpg"
    destimg="C:\\Users\\admin\\Pictures\\bwdhoni.jpg"
    image1=Image.open(srcimg)
    image1.convert(mode='L').save(destimg)

blackwhite()

def blurimage():
    srcimg2=""
    destimg2=""
    image2=Image.open(srcimg2)
    image2.filter(ImageFilter.GaussianBlur(20)).save(destimg2)

blurimage()

def imgrotate():
    srcimg3=""
    destimg3=""
    image3=Image.open(srcimg3)
    image3.rotate(-90).save(destimg3)  #clockwise=90degree

#imgrotate()