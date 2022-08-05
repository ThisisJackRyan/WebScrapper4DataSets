import csv
import os 
from PIL import Image



def pixel_Conversion_Main():
    parentFolder = os.listdir(r"C:\Users\Jack Ryan\Desktop\Coding\Python\webScrapper\scrappedImages") #list

    with open("RGB_Values.csv", 'w', newline = "") as f:
        for i in parentFolder:
            folder = os.listdir(r"C:\Users\Jack Ryan\Desktop\Coding\Python\webScrapper\scrappedImages\\"+i) # i is name of folder
            print("Parent Folder: " + i)
        
            for j in folder:
                image = Image.open(r"C:\Users\Jack Ryan\Desktop\Coding\Python\webScrapper\scrappedImages\\"+i +"\\" + j) # j is name of image
        
                pixel_values = image.getdata() # tuple
                folder_Name = j.removesuffix(".png") #removes .png 
                writer = csv.writer(f)
                writer.writerow(folder_Name)
                writer.writerow("")
                writer.writerow(pixel_values)
                writer.writerow("")
                writer.writerow("")
                writer.writerow("")
         
            





        