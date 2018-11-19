# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re, copy, json


def read_file(filename):
    data = []
    for line in open(filename, 'r'):
        str = line.rstrip('\n')
        data.append(str)
    return data


def init():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # silent mode
    driver = webdriver.Chrome(executable_path= '/Users/claire/Documents/USC/Study/SecondTerm/KnowledgeGraph/project/git/KGKitchen/amazon/chromedriver',
                          chrome_options=options)
    return driver


def search_ingre(driver, data):
    all_info = []
    for dt in data:
        print(dt)
        driver.get('https://www.amazon.com/AmazonFresh/b?ie=UTF8&node=10329849011')

        input = driver.find_element_by_name('field-keywords')
        input.clear()
        input.send_keys(dt)
        driver.find_element_by_xpath("//input[@type='submit']").click()

        all_info.append({dt: ext_ingre(driver, dt)})
        driver.implicitly_wait(5)

    return all_info


def ext_ingre(driver, dt):
    try:
        driver.implicitly_wait(2)

        center_minus_xpath = "//div[@id='centerMinus']/div[@class='a-row s-result-list-parent-container']/ul/li"
        info = [{dt: ext_info(center_minus_xpath)}]

        center_below = "//div[@class='a-row s-padding-left-small s-padding-right-small']"
        center_below_length = len(driver.find_elements_by_xpath(center_below))
        for i in range(center_below_length):
            center_below_xpath = center_below +"/div[@id='fkmr-results" + str(i) + "\']/ul/li"
            center_below_keyword = ''
            for cbk in driver.find_elements_by_xpath(center_below +"/div[@id='fkmr-results" + str(i) + "\']/../preceding-sibling::div[1]//span/span"):
                center_below_keyword += (cbk.text + ' ')

            center_below_keyword = re.sub(r'[\W]', ' ', center_below_keyword).strip(' ')
            center_below_keyword = re.sub(r'[ ]+', ' ', center_below_keyword)
            info.append({center_below_keyword: ext_info(center_below_xpath)})
        return info
    except:
        print('ext_ingre wrong')
        pass


def ext_info(xpath):
    info = []
    count = 0
    try:
        for sec in driver.find_elements_by_xpath(xpath):
            ingre = {'name': '', 'price': '', 'unit_price': ''}
            sec_t = sec.text.split('\n')
            ingre['name'] = driver.find_elements_by_xpath(xpath + '//h2')[count].text.encode('utf-8')
            for st in sec_t:
                if st[0] == '$':
                    temp = st[2:].split(' ')
                    ingre['price'] = '$' + temp[0] + '.' + temp[1]
                    if len(temp) > 2:
                        if re.search('\(\$', temp[2]):
                            t = re.split('\)', temp[2])[0]
                            ingre['unit_price'] = t.lstrip('(')
                        else:
                            ingre['unit_price'] = ingre['price'] + '/default'
                    else:
                        ingre['unit_price'] = ingre['price'] + '/default'
            if ingre['name'] != '':
                info.append(copy.deepcopy(ingre))
            count += 1

            if len(driver.find_elements_by_xpath(xpath)) == 1 or driver.find_elements_by_xpath(xpath)[1].text == '':
                break
            elif len(driver.find_elements_by_xpath(xpath)) > 1:
                if count == 2:
                    break
    except:
        print('ext_info wrong')
        pass

    return info


def save_file(filename, info):
    with open(filename, 'w') as f:
        f.write(json.dumps(info, indent=4))


if __name__ == '__main__':
    data = read_file('5.txt')
    driver = init()
    info = search_ingre(driver, data)
    save_file('price_5.txt', info)

