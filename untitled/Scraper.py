from selenium import webdriver

#this function grabs a value from the specified website(needs to be a graph from
# 'Tradingview.com' because the driver needs the specified path to follow in
# order to grab the currency value
def scrapperValue(url):
    #initialize the driver with the headless option
    #in order to not open a window every time we grab
    #the values from the site
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(r'C:\Users\Shiffy46\webdrivers\chromedriver.exe',chrome_options=options)

    #possibly running into timing problems, loading webpage too late
    driver.implicitly_wait(20)

    #get the webpage information from the driver and grab the values for
    #the currency price and the name of the currency
    driver.get(url)
    result = driver.find_element_by_class_name("dl-header-price")
    price = result.text

    #close the window after the the values are pulled from it
    driver.close()

    return price

#This function is similar to scrapperValue but instead grabs the name of the currency
def scrapperName(url):
    #initialize the driver with the headless option
    #in order to not open a window every time we grab
    #the values from the site
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(r'C:\Users\Shiffy46\webdrivers\chromedriver.exe',chrome_options=options)

    #possibly running into timing problems, loading webpage too late
    driver.implicitly_wait(20)

    #get the webpage information from the driver and grab the values for
    #the currency price and the name of the currency
    driver.get(url)
    currencyName = driver.find_element_by_class_name("dl-header-symbol-desc")
    Name = currencyName.text

    #close the window after the the values are pulled from it
    driver.close()

    return Name


#testing scripts to run and see if it is working
price = scrapperValue("https://www.tradingview.com/chart/?symbol=TVC:DXY")
name = scrapperName("https://www.tradingview.com/chart/?symbol=TVC:DXY")
print(price)
print(name)