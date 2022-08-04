from re import S
import time
import os
import pyautogui # use this for making images look good 
import sys
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from PIL import Image


from selenium.webdriver.chrome.options import Options
#chrome_options = Options()#creates options
#chrome_options.add_argument("--headless")#chooses headless option


chromedriverPath = "C:\Program Files (x86)\chromedriver.exe" #for Windows



#driver = webdriver.Chrome(chromedriverPath, options=chrome_options)#headless version



def scrapper_Main():
    intendedsearch = input("What do you want to search?")
    search(intendedsearch)

def loadWebPage():
    global driver
    driver = webdriver.Chrome(chromedriverPath)
    driver.get("https://www.google.com/")
    driver.maximize_window()
    time.sleep(2)

def search(intendedsearch):
    loadWebPage()
    searchbar = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
                                            #/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input # this path is for search bar once somthing is already searced
    searchbar.send_keys(intendedsearch)
    searchbar.send_keys(Keys.RETURN)
    time.sleep(5)
    clickImage(intendedsearch)


def clickImage(intendedsearch):
    #only works if imageIcon is in 2nd spot 
    imageIcon = driver.find_element_by_xpath("/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a")# xpath won't work because the order will switch 
    imageIcon.click()
    #openImageInNewTab()
    scroll(intendedsearch)

def scroll(intendedsearch):
    #/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img -- First Image
    #/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[2]/a[1]/div[1]/img -- Second Image
    #/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[3]/a[1]/div[1]/img -- Third Image
    #Will keep scrolling down the webpage until it cannot scroll no more
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            time.sleep(2)
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height
    imageCollect(intendedsearch)
   

def imageCollect(intendedsearch):
    newpath = r'C:\Users\Jack Ryan\Desktop\Coding\Python\webScrapper\scrappedImages\\'+intendedsearch
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for i in range(1,10):    
        try:
            image = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div["+str(i)+"]/a[1]/div[1]/img")
            image.screenshot(r'C:\Users\Jack Ryan\Desktop\Coding\Python\webScrapper\scrappedImages\\'+intendedsearch+'\\'+intendedsearch+' (' +str(i)+ ').png')
            cropImages(intendedsearch, i)
        except:
            pass
    again()
    

def cropImages(intendedsearch, i): # no worky
        capturedImage = Image.open(r'C:\Users\Jack Ryan\Desktop\Coding\Python\webScrapper\scrappedImages\\'+intendedsearch+'\\'+intendedsearch+' (' +str(i)+ ').png')

        left = 50
        top = 50
        right = 150 
        bottom = 150
    
        parameters = (left,top,right,bottom)
        new_Image = capturedImage.crop(parameters)
        #new_Image.show()
        new_Image.save(r'C:\Users\Jack Ryan\Desktop\Coding\Python\webScrapper\scrappedImages\\'+intendedsearch+'\\'+intendedsearch+' (' +str(i)+ ').png')
        
def again(): 
    driver.close()
    answer = input("Would you like to collect more Images with a different search? (y/n)")

    if answer == "y":
        scrapper_Main()
    elif answer == "n":
        sys.exit("Thanks for running!!!")
    else:
        print("Please only enter 'y' or 'n' " )
        again()



print("done")