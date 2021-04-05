import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import select

driver = webdriver.Chrome("C:\\Neha P\\Selenium\\chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(10)
driver.maximize_window()
print("driver title is : ", driver.title)
print("driver current url is :", driver.current_url)
print("driver name is ", driver.name)
list = driver.find_elements_by_xpath("//legend[text()]")
for legend in list:
    print(legend.text)

# radio button example :
radio_buttons = driver.find_elements_by_xpath("//input[@name='radioButton']")
print("Radio buttons are : ")
for radio_button in radio_buttons:
    print(radio_button.is_enabled())
    radio_button.click()
    print(radio_button.is_enabled())

# Checkbox Example
checkbox_buttons = driver.find_elements_by_xpath("//input[@type='checkbox']")
print("check boxes are : ")
for checkbox_button in checkbox_buttons:
    print(checkbox_button.is_selected())
    if checkbox_button.is_selected() == False:
        checkbox_button.click()
    print(checkbox_button.is_selected())

# dropdown example : static drop down
dropdown = driver.find_element_by_xpath("//select[@id='dropdown-class-example']")
print("visible options are : ")
dropdown.click()
options = driver.find_elements_by_xpath("//option[@value]")
for option in options:
    print(option.text)
    print(option.is_displayed())
    print(option.is_selected())
    option.click()
    dropdown.click()
    print(option.is_selected())

# suggestion class example
dynamic_dropdown = driver.find_element_by_xpath("//input[@id='autocomplete']")
dynamic_dropdown.click()
print("Enter the country: ")
#input_text = input()
input_text="ind"
text = "India"

dynamic_dropdown.send_keys(input_text)
dynamic_dropdown_list = driver.find_elements_by_xpath("//li/div[text()]")
for list in dynamic_dropdown_list:
    print(list.text)
    print(type(list.text))
    
    if list.text == text:
        list.click()
        print("list value is clicked")
        break
    
    else:
        print("list not found")
        
#switch window exmaple

open_window=driver.find_element_by_id("openwindow")
open_window.click()
window_handle=driver.window_handles
print("window handles are : ",len(window_handle))
child_window=driver.switch_to.window(window_handle[1])
driver.maximize_window()
print("control is in child window now")
driver.close()
#print("child window is closed")
driver.switch_to.window(window_handle[0])

#switch to tab
switch_tab=driver.find_element_by_id("opentab")
switch_tab.click()
open_tabs=driver.window_handles
print("window handles are : ",len(window_handle))
child_tab=driver.switch_to.window(open_tabs[1])
print("tab url is ",driver.current_url)

driver.close()
driver.switch_to.window(window_handle[0])
print(driver.current_url)



#switch to alert

alert_text=driver.find_element_by_id("name")
alert=driver.find_element_by_id("alertbtn")
alert_cancel=driver.find_element_by_id("confirmbtn")
alert_text.send_keys("neha")
alert.click()
alert_message1=driver.switch_to.alert.text
print("alert message is ",alert_message1)
assert "knowledge" in alert_message1
driver.switch_to.alert.accept()
print("alert has been accpeted")

alert_text.send_keys("neha")
alert_cancel.click()
assert_message=driver.switch_to.alert.text
print("alert text message cancel",assert_message)

assert "Hello" in driver.switch_to.alert.text
driver.switch_to.alert.dismiss()
print("alert message has been dismissed")

alert_text.send_keys("neha")
alert_cancel.click()
driver.switch_to.alert.accept()
print("cancel - alert message has been accpeted")

#hide and show
hide_textbox=driver.find_element_by_id("hide-textbox")
show_textbox=driver.find_element_by_id("show-textbox")
displayed_text=driver.find_element_by_id("displayed-text")

hide_textbox.click()
print("displayed test is visible ? :",displayed_text.is_displayed())

show_textbox.click()
print("displayed test is visible ? :",displayed_text.is_displayed())

#mouse hover

mouse_hover=driver.find_element_by_id("mousehover")
action=ActionChains(driver)
action.move_to_element(mouse_hover).perform()
print("mouse hover happened")
childMenu=action.move_to_element(driver.find_element_by_link_text("Top")).click().perform()
action.move_to_element(mouse_hover).perform()
action.move_to_element(driver.find_element_by_link_text("Reload")).click().perform()

#iframe
print("switch to Iframe")
driver.switch_to.frame("courses-iframe")
print("in iframe")
driver.switch_to.default_content()
print(driver.title)



driver.quit()






