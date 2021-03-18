from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import *
from zillow_finder import zillow_finder

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSeSkO-bPILp_GXIhzl_5ulXY3NOmxmA38UyyNFyhKiDyrG34A/viewform?usp=sf_link"


class sheet_filler():
    def __init__(self):
        chrome_driver_path = "C:/Users/Maciek/PycharmProjects/chromedriver_win32/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.pages_to_scrape = 3

    def fill_sheet(self, zillow_output):
        self.driver.get(GOOGLE_FORM)

        for apartment in range(len(zillow_output[0])):
            sleep(3)
            address_box = self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
            address_box.send_keys(zillow_output[2][apartment])

            sleep(2)
            price_box = self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
            price_box.send_keys(zillow_output[1][apartment])

            sleep(2)
            link_box = self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
            link_box.send_keys(zillow_output[0][apartment])

            sleep(1)
            submit_button = self.driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div")
            submit_button.click()

            sleep(3)
            another_response_button = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            another_response_button.click()
