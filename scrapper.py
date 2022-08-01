import time
import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from PIL import Image


from selenium.webdriver.chrome.options import Options
#chrome_options = Options()#creates options
#chrome_options.add_argument("--headless")#chooses headless option


chromedriverPath = "C:\Program Files (x86)\chromedriver.exe" #for Windows

intendedsearch = input("What do you want to search?")

#driver = webdriver.Chrome(chromedriverPath, options=chrome_options)#headless version
driver = webdriver.Chrome(chromedriverPath)
action = ActionChains(driver)
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(2)


def search(intendedsearch):
    searchbar = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
                                            #/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input # this path is for search bar once somthing is already searced
    searchbar.send_keys(intendedsearch)
    searchbar.send_keys(Keys.RETURN)
    time.sleep(5)
    clickImage(intendedsearch)

def ssecondearch(intendedsearch):
    searchbar = driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input")
    #//*[@id="hdtb-msb"]/div[1]/div/div[4]/a
    searchbar.send_keys(Keys.CONTROL, intendedsearch)#hilights text
    searchbar.send_keys(Keys.BACKSPACE)#deletes text
    searchbar.send_keys("harro")#new text 
    searchbar.send_keys(Keys.RETURN)
    

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
   

def openImageInNewTab(): #did not get this to work because selenium is web based and context menu is os based
    image = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div[2]/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img")
    #image.click()
    time.sleep(2)
    action.context_click(image).perform()
    pyautogui.moveTo(120, 130, duration=1)# the locations for the mouse are wrong and need to be change try not to make it jsut stand alone numbers or else it will not                            
    pyautogui.leftClick()               # change for every single picture
    time.sleep(1)
    pyautogui.moveTo(300,40)
    pyautogui.leftClick()
        
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
    

def cropImages(intendedsearch, i): # no worky
        capturedImage = Image.open(r'C:\Users\Jack Ryan\Desktop\Coding\Python\webScrapper\scrappedImages\\'+intendedsearch+'\\'+intendedsearch+' (' +str(i)+ ').png')
        #pixel = capturedImage.load()
        #x,y = capturedImage.size()
        '''print(" ")
        print(" ")
        print("x: " + x)
        print("y: " + y)'''

        left = 50
        top = 50
        right = 150 
        bottom = 150
        '''if x and y == 100:
            pass
        else: 
            if x != 100:
                difference = x - 100
                if difference % 2 == 0:
                    print("even x")
                    left = difference / 2 
                    right = x - left
                else:
                    print("odd x")
                    left = difference / 2
                    left = left - .5
                    right = difference / 2
                    right = right + .5
            elif y != 100:
                difference = y - 100
                if difference % 2 == 0:
                    print("even y")
                    top = difference / 2 
                    bottom = x - top
                else:
                    print("odd y")
                    top = difference / 2
                    top = top - .5
                    bottom = difference / 2
                    bottom = bottom + .5'''
        print(left)
        print(top)
        print(right)
        print(bottom)
        parameters = (left,top,right,bottom)
        new_Image = capturedImage.crop(parameters)
        
   
        new_Image.show()
        new_Image.save()
        


        
search(intendedsearch)
print("done")