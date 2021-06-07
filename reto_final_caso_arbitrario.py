import sys
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestRetoFinalCaso(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    #@unittest.skip("temp")
    def test_reto_final_caso_arbitrario1(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        elements_button = driver.find_element_by_xpath('//div[@class="header-text"]')
        elements_button.click() 
        textbox_button = driver.find_element_by_xpath("//span[contains(text(),'Text Box')]")
        textbox_button.click()
        dict_data = {'userName':'Milton','userEmail':'mespinozas@canvia.com',
                    'currentAddress':'San Jeronimo - Cusco','permanentAddress':'Santiago de Surco - Lima'}
        for keys in dict_data:
            field = driver.find_element_by_id(keys).send_keys(dict_data[keys])

        #driver.execute_script("document.getElementById('submit').click();")
        submit_button = driver.find_element_by_id('submit')
        try:
            submit_button.click()
        except:
            driver.execute_script('arguments[0].click();',submit_button)

        name_output = driver.find_element_by_id('name')
        email_output = driver.find_element_by_id('email')
        currentAddress_output = driver.find_element_by_id('currentAddress')
        permanentAddress_output = driver.find_element_by_id('permanentAddress')        
        self.assertRegex(name_output.text, 'Milton')
        self.assertRegex(email_output.text, 'mespinozas@canvia.com')
        self.assertRegex(currentAddress_output.get_attribute("value"), 'San Jeronimo - Cusco')
        self.assertRegex(permanentAddress_output.get_attribute("value"), 'Santiago de Surco - Lima')


    #@unittest.skip("temp")
    def test_reto_final_caso_arbitrario2(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        elements_menu = driver.find_element_by_xpath('//div[@class="header-text"]')
        elements_menu.click() 
        checkbox_menu = driver.find_element_by_xpath("//span[contains(text(),'Check Box')]")
        checkbox_menu.click()
        desliz_button = driver.find_element_by_xpath('//*[@class="rct-text"]/button')
        desliz_button.click()
        desktop_button = driver.find_elements_by_xpath('//*[@class="rct-checkbox"]')[1]
        desktop_button.click()        
        text_output = driver.find_element_by_id('result')
        self.assertRegex(text_output.text,'desktop')

    #@unittest.skip("temp")    
    def test_reto_final_caso_arbitrario3(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        elements_menu = driver.find_element_by_xpath('//div[@class="header-text"]')
        elements_menu.click() 
        radiobutton_menu = driver.find_element_by_xpath("//span[contains(text(),'Radio Button')]")
        try:
            radiobutton_menu.click()
        except:
            driver.execute_script('arguments[0].click();', radiobutton_menu)
        yes_radiobutton = driver.find_element_by_xpath("//div[@class='custom-control custom-radio custom-control-inline']")
        yes_radiobutton.click()
        text_output = driver.find_element_by_xpath('//*[@class="mt-3"]/span')
        self.assertEqual(text_output.text,'Yes')
    
    #@unittest.skip("temp")
    def test_reto_final_caso_arbitrario4(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        elements_menu = driver.find_element_by_xpath('//div[@class="header-text"]')
        elements_menu.click() 
     
        #driver.execute_script("document.getElementById('item-4').click();")
        buttons_menu = driver.find_element_by_id('item-4')
        try:
            buttons_menu.click()
        except:
            driver.execute_script('arguments[0].click();',buttons_menu)
     
        #clickme_button = driver.find_element_by_xpath('//button[contains(text(), "Click Me")]')
        clickme_button = driver.find_element_by_xpath('//button[text()="Click Me"]')
        clickme_button.click()

        text_output = driver.find_element_by_id('dynamicClickMessage')
        self.assertRegex(text_output.text, 'dynamic click')

    #@unittest.skip("temp")
    def test_reto_final_caso_arbitrario5(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        elements_menu = driver.find_element_by_xpath('//div[@class="header-text"]')
        elements_menu.click() 

        #driver.execute_script("document.getElementById('item-6').click();")
        broken_menu = driver.find_element_by_id('item-6')
        try:
            broken_menu.click()
        except:
            driver.execute_script('arguments[0].click();', broken_menu)

        broken_link = driver.find_element_by_xpath('//p[text()="Broken Link"]'+'//following-sibling::a')
        try:
            broken_menu.click()
        except:
            driver.execute_script('arguments[0].click();',broken_link)

        text_output = driver.find_element_by_class_name('example')
        self.assertRegex(text_output.text,'500 status code')

if __name__ == '__main__':
    unittest.main()
