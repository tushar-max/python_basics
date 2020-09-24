from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

print(type(browser))

browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

# Clicking in one element:

linkElem = browser.find_element_by_link_text('Read Online for Free')

print(type(linkElem))

linkElem.click() # follows the "Read Online for Free" link

# Filling out or submitting forms

browser.get('https://login.metafilter.com')

userElem = browser.find_element_by_id('user_name')
userElem.send_keys('your_real_username_here')
passwordElem = browser.find_element_by_id('user_pass')
passwordElem.send_keys('your_real_password_here')
passwordElem.submit()