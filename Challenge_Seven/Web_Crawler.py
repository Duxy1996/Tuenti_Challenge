from selenium import webdriver
browser = webdriver.Chrome('./chromedriver.exe') 
browser.get("http://52.49.91.111:8036/word-soup-challenge")
cases = []
for i in range(0,5):
 	for j in range(0,5):
  		cases.append(str(i)+"-"+str(j))

print cases
browser.find_element_by_id('0-0').click()
copied_text = browser.find_by_id('results')[0].text
print copied_text

  