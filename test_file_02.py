'''markers'''
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.softwaretestingmaterial.com/sample-webpage-to-automate/')
driver.maximize_window()
def test_amb():
    a = 10
    b = 22
    assert not a==b
#
#
def test_amb_01():
    x = 10
    y = 20
    assert x==y
#
#
def test_notification_00():
    A = driver.find_element(By.ID,"onesignal-slidedown-cancel-button")
    A.click()


def test_text_01():
    a = driver.find_element(By.NAME,"username")
    a.send_keys("Sanket")


def test_password_02():
    b = driver.find_element(By.NAME,"password")
    b.send_keys("pass@123")


def test_textarea_03():
    c = driver.find_element(By.NAME,"comments")
    c.send_keys("sanket shirode\nAurangabad\nMaharashtra")


def test_checkboxes_04():
    d = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/div/article/div/div[1]/form/p[3]/input[1]")
    d.click()
    e = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/div/article/div/div[1]/form/p[3]/input[2]")
    e.click()
    f = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/div/article/div/div[1]/form/p[3]/input[3]")
    f.click()


def test_radiobutton_05():
    g = driver.find_element(By.NAME,"radioselenium")
    g.click()
    h = driver.find_element(By.NAME,"radioqtp")
    h.click()
    i = driver.find_element(By.NAME,"radioloadrunner")
    i.click()
    time.sleep(2)
    driver.minimize_window()
    time.sleep(10)
