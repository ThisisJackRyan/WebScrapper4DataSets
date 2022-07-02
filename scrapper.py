import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
#chrome_options = Options()#creates options
#chrome_options.add_argument("--headless")#chooses headless option


chromedriverPath = "C:\Program Files (x86)\chromedriver.exe" #for Windows

intendedsearch = input("What do you want to search?")

#driver = webdriver.Chrome(chromedriverPath, options=chrome_options)#headless version
driver = webdriver.Chrome(chromedriverPath)
driver.get("https://www.google.com/")
time.sleep(2)

def search(intendedsearch):
    searchbar = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
                                            #/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input # this path is for search bar once somthing is already searced
    searchbar.send_keys(intendedsearch)
    searchbar.send_keys(Keys.RETURN)
    time.sleep(5)
    clickImage()

def ssecondearch(intendedsearch):
    searchbar = driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input")
    #//*[@id="hdtb-msb"]/div[1]/div/div[4]/a
    searchbar.send_keys(Keys.CONTROL, intendedsearch)#hilights text
    searchbar.send_keys(Keys.BACKSPACE)#deletes text
    searchbar.send_keys("harro")#new text 
    searchbar.send_keys(Keys.RETURN)
    

def clickImage():
    #only works if in 2nd spot 
    imageIcon = driver.find_element_by_xpath("/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a")# xpath won't work because the order will switch 
    imageIcon.click()
    imageCollect()

def imageCollect():
    #/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img -- First Image
    #/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[2]/a[1]/div[1]/img -- Second Image
    #/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[3]/a[1]/div[1]/img -- Third Image
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #scrolls down till new images load
    time.sleep(2)
    #driver.execute_script("window.scrollTo(document.body.scrollHeight,0)") #returns to the top
    time.sleep(2)

    
    for i in range(1,40):    
        try:
            image = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div["+str(i)+"]/a[1]/div[1]/img")
            image.screenshot(r'C:\Users\Jack Ryan\Desktop\Coding\Python\webScrapper\scrappedImages\scrapped (' +str(i)+ ').png')
        except:
            pass
    

search(intendedsearch)
print("done")