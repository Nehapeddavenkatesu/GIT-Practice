

from ProtoCommerce.Pages.ProtoCommerce_Pages import Locators
from ProtoCommerce.Scripts.Script import driver


class workflow(Locators):
    # labels :
    driver.find_element_by_xpath(Locators.label_name)
    driver.find_element_by_xpath(Locators.label_email)
    driver.find_element_by_xpath(Locators.label_password)
    driver.find_element_by_xpath(Locators.checkbox)
    driver.find_element_by_xpath(Locators.label_gender)
    driver.find_element_by_xpath(Locators.label_employee_status)
    driver.find_elements_by_id(Locators.radiobutton1)
    
    driver.find_elements_by_id(Locators.radiobutton2)
    driver.find_elements_by_id(Locators.radiobutton3)
    driver.find_element_by_xpath(Locators.label_dob)
    driver.find_element_by_xpath(Locators.label_data_binding)
    
    # Fields
    
    driver.find_element_by_xpath(Locators.name).send_keys("neha")
    driver.find_element_by_xpath(Locators.email).send_keys("nehagrriet@gmail.com")
    driver.find_element_by_xpath(Locators.password).send_keys("testtest")
    checkbox_select=driver.find_element_by_xpath(Locators.checkbox)
    print(checkbox_select.is_selected())
    checkbox_select.click()
    driver.find_element_by_xpath(Locators.gender_list)
    radiobutton1_enabled = driver.find_element_by_id(Locators.radiobutton1)
    print(radiobutton1_enabled.is_enabled())
    radiobutton1_enabled.click()
    radiobutton2_enabled=driver.find_element_by_id(Locators.radiobutton2)
    print(radiobutton2_enabled.is_enabled())
   # radiobutton2_enabled.click()
    radiobutton3_enabled=driver.find_element_by_id(Locators.radiobutton3)
    print(radiobutton3_enabled.is_enabled())
    driver.find_element_by_xpath(Locators.name1).send_keys("texttest")
    driver.find_element_by_xpath(Locators.submit_button).click()
    success_meaasge = driver.find_element_by_xpath("//div/a")
    print(success_meaasge.text)
    
    

  










