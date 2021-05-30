import sys
import unittest
import time
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestReto1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()
        
    def test_reto1(self):
        df = pd.read_excel('challenge.xlsx').drop('Unnamed: 7',axis=1)
        df.columns = ['First Name', 'Last Name', 'Company Name', 'Role in Company','Address', 'Email', 'Phone Number']
        dict_data_list = []
        for index, row in df.iterrows():
            dict_ = {}
            for i in df.columns:
                dict_[i] = row[i]
            dict_data_list.append(dict_)

        driver = self.driver
        driver.get("http://www.rpachallenge.com/")
        button_start = driver.find_element_by_xpath("//button[contains(text(),'Start')]")
        button_start.click()   
        box = '//following-sibling::input'     
        
        for dict_data in dict_data_list:
            for keys in dict_data:
                field = driver.find_element_by_xpath(f'//label[text()="{keys}"]'+box).send_keys(dict_data[keys])
            button_submit = driver.find_element_by_xpath("//input[@class='btn uiColorButton']") #input[class="btn uiColorButton"]
            button_submit.click()
        text_input = driver.find_element_by_xpath('//div[@class="message2"]')
        score = int(re.search(r'(\d+)%',text_input.text).group(1))
        time.sleep(5)
        self.assertGreaterEqual(score,90)
    
if __name__ == '__main__':
    unittest.main()