import csv
import os 
import scrappedImages



def pixel_Conversion_Main():
    print("Main() -- Worked!")
    #for pic in scrappedImages:
    #worried that having them seperated in folder will anger the coding gods

def pixelConversion(image):
    pixel_values = (image.getdata())
    with open('van_Camping_RGB_Values', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(pixel_values)

def find_intendedsearch():
    print("Still Working on")



        