import csv
import os 
from PIL import Image



def pixel_Conversion_Main():
    folderNames = os.listdir(r"C:\Users\Jack Ryan\Desktop\Coding\Python\webScrapper\scrappedImages")
    print(folderNames)
    for i in folderNames:
        parentFolder = os.listdir(r"C:\Users\Jack Ryan\Desktop\Coding\Python\webScrapper\scrappedImages\\"+i)
        print("Parent Folder: " + i)
        for j in parentFolder:
            image = Image.open(r"C:\Users\Jack Ryan\Desktop\Coding\Python\webScrapper\scrappedImages\\"+i +"\\" + j)
            pixelConversion(image)
        

def pixelConversion(image):
    pixel_values = (image.getdata())
    with open('van_Camping_RGB_Values', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(pixel_values)





        