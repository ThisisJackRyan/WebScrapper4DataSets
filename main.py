import scrapper 
import pixelConversion 



def choose_Direction():
    answer = input('Do you want to run the "Web Scrapper Script (w)" or "Pixel Conversion Script (p)"')
    if answer == "w":
        scrapper.scrapper_Main()
    elif answer == "p":
        pixelConversion.pixel_Conversion_Main()
    else:
        print('Please only enter "w" or "p" ')
        choose_Direction()

    
choose_Direction()