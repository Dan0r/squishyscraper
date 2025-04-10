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
2. WebDriver needs a function to call
3. WebDriver also needs a tuple, thats why we use ((By.ID, "picker-trigger"))).click(). Instead it gives you the error ""element_to_be_clickable() takes 1 positional argument but 2 were given"
2. Use EC for the parent to appear 
3. Use EC until the button in the parent is enabled with .isenabled()
    * WebDriverWait keeps calling a function and when this function turns from True to False it continues. But if its just one line, it just calls it once. Gets one False - and then immediately moves on. Thats why it needs a function to executed the whole time.
    * This however requires a function
3. Flexbox: It is always better to try and let selenium click the <button> element, rather than a sibling, like id=label-element. Buttons are always clickable
4. $0 shows the most recent selected DOM element, kind of like your cursor
5. Notice: 45 doesn't need '' like color did, because here we are selecting an integer
6. We also notice, when we select a shoe that is not in stock, a window instantly pops up.
if we click the out of stock number enough times, with the Developer-Tools open, we can see that values change. in particular: data-is-selected switches from =true to =false.
THis is a boolean value: The data is either there, or its not. Webdevelopers often blend in these boolean values, to open another feature or not. Als sie vielleicht extra für diesen Artikel abboniert haben ist das HTML-Element des Artikels von       "hasHeisePlusAccess": false auf       "hasHeisePlusAccess": true gesprungen.
Also im Prinzip haben sie mit der Bezahlung nur einen booleschen Wert umgelegt, der dann ein Dominoeffekt anstöst und diesen Artikel lud.
7. IF you declared a variable and print(variable) it will most of the time only return the selenium WebElement. To paste out what this WebElement contains, use .text method
8. use /ancestor to navigate up the DOM
