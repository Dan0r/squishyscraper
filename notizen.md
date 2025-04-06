# Notizen
There are two methods for accessing shadow root:
* JavascriptExectuor
'''
cookie = driver.execute_script('return document.querySelector("#usercentrics-root").shadowRoot.querySelector("[data-testid=\'uc-deny-all-button\']")')
'''
* .getshadowroot method
'''
shadow_host = driver.find_element(By.CSS_SELECTOR, '#usercentrics-root')
shadow_root = shadow_host.shadow_root
shadow_content = shadow_root.find_element(By.CSS_SELECTOR, "[data-testid='uc-deny-all-button']")
shadow_content.click()
'''
[documentation](https://www.selenium.dev/documentation/webdriver/elements/finders/)

You can gradually improve the shadowroot method
1. Use hardcoded time.sleep(3)
2. Use EC for the parent to appear 
3. Use EC until the button in the parent is enabled with .isenabled()
    * WebDriverWait keeps calling a function and when this function turns from True to False it continues. But if its just one line, it just calls it once. Gets one False - and then immediately moves on. Thats why it needs a function to executed the whole time.
    * This however requires a function
