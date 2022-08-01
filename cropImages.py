import os
import time
from turtle import position, right
from PIL import Image
def loadImage():
    timesCropped = 0
    pathToPictures = os.listdir("scrappedImages")
    picNumber = 0
    for pic in pathToPictures:
        print(pic)
        image = Image.open(r"C:\Users\Jack Ryan\Desktop\Coding\Python\webScrapper\scrappedImages\\" + pic)
        pixel = image.load #loads
        x,y =image.size #finds hieght and width
        print("x: " + str(x))
        print("y: " + str(y))
        print(" ")
        time.sleep(2)
        rgbValues(x, y, image,timesCropped,picNumber)


def rgbValues(x, y, image, timesCropped, picNumber):
    #time.sleep(10)
    pixel_values = list(image.getdata())# gets pixel rgba values
    #print(pixel_values)
    counter = 0
    pixelIndex = 0 
    for i in pixel_values:
        #print(i)
        if i == (255, 255, 255, 255):
            counter +=1   
        elif i != (255, 255, 255, 255) and counter > 2:
            print("Counter is Now: " + str(counter))
            counter = 0
        #banna = pixelIndex+1% x#fix this 
        #print(banna)
        if pixelIndex % x == 0:
            print("END OF ROW")
            print("PixelIndex: "+ str(pixelIndex))
            print(" ")
            print(" ")
            if counter > 2 and pixelIndex+1 != counter:
                position = "right"
                print(pixelIndex)
                cropImage(image, position, counter, x, y, timesCropped, picNumber)
                print("CROPPPED")
        pixelIndex += 1

def cropImage(image, position, counter, x, y, timesCropped, picNumber):#no worky
    print("x: " + str(x))
    print("y: " + str(y))
    print(counter) # curently is 272 on first picture first row because it is the whole width of the picture so when it crops it crops the entire picture 
    left = 0                                        #/\
    top = 0                                        #/  \
    right = 0                                      #Fixed but crop no worky
    bottom = 0
    if position == "right":
        amount =  x - counter  #tried to see if my understanding was off on crop works but did not fix issue probabaly a bad syntax error -- probably delete this line and change counter back to amount because it is nicer.
        right = amount 
    elif position == "left":
        left = amount
    elif position == "top":
        top = amount
    elif position == "bottom":
        bottom = amount
    parameters = (left,top,right,bottom)
    new_Image = image.crop(parameters)#scorcce of issue I think
    timesCropped +=1
    picNumber +=1
    print(timesCropped)
    print(picNumber)
    print("test after crop")
    new_Image.save("scrapped (" + str(picNumber) + ")_cropped(" + str(timesCropped) + ").png" )
    print("test after save")
    new_Image.show()
    print("test after show")
    time.sleep(10)

            



    
loadImage()