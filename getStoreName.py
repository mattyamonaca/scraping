from selenium import webdriver
import chromedriver_binary #使用しているchromeのバージョンに合わせる
import time

driver = webdriver.Chrome()
driver.get("https://www.e-map.ne.jp/p/lawson/nmap.htm?&his=al1&lat=35.6863167&lon=139.6950472&srchnm=%C5%EC%B5%FE%C5%D4")

INTERVAL = 5 #emapの要素が展開されるまでに時間がかかるので、数秒待機させる


time.sleep(INTERVAL)

store_all = driver.find_element_by_class_name("nearest-result-left")
store_list = store_all.find_elements_by_xpath("//div[@role='button']")

info_list = ["address","phone","desc"]
result = {}
for store in store_list:
    result[store.find_element_by_class_name("name").text] = {}
    result[store.find_element_by_class_name("name").text]["name"] = store.find_element_by_class_name("name").text
    store_info = store.find_elements_by_tag_name("li")
    for num in range(0,len(store_info)):
        result[store.find_element_by_class_name("name").text][info_list[num]] = store_info[num].text

print(result)

driver.quit()
