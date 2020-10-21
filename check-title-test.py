from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.dcode.fr/factorial")

if (browser.title == "Factorial Calculator - n! Notation - Online Software Tool"):
    print("Success: Factorial Calculator launched successfully")
else:
    print("Failure: Factorial page Title is incorrect")

browser.quit()