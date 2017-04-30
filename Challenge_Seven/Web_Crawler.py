from selenium import webdriver
import time

browser = webdriver.Chrome('./chromedriver.exe') 
browser.get("http://52.49.91.111:8036/word-soup-challenge")
cases = []
for i in range(0,6):
 	for j in range(0,6):
  		cases.append(str(i)+"-"+str(j))

time.sleep(1)

minl = 4

words = browser.find_elements_by_css_selector('#words > div')
initials = []
words.pop()
words.pop()
try:
	for w in words:
		if w.text[0] not in initials:
			print(w.text[0])
			initials.append(w.text[0])

	print(initials)

	for c in cases:
		if browser.find_element_by_id(c).text in initials:
			for d in cases:
				dif = abs(int(c[0])-int(d[0])) >= minl-1
				dif2 = abs(int(c[2])-int(d[2])) >= minl-1
				diag = abs(int(d[0])-int(c[0])) == abs(int(d[2])-int(c[2]))
				if (c[0]==d[0] and dif2) or (c[2]==d[2] and dif) or (diag and dif and dif2):
					browser.find_element_by_id(c).click()
					time.sleep(0.07)
					browser.find_element_by_id(d).click()
					time.sleep(0.07)
except Exception, e:
	print("exc")

time.sleep(3)
cases = []
for i in range(0,20):
 	for j in range(0,20):
  		cases.append(str(i)+"-"+str(j))

browser.find_element_by_id('btn-level-2').click()

time.sleep(1)

minl = 9

words = browser.find_elements_by_css_selector('#words > div')
initials = []
words.pop()
words.pop()

for w in words:
	if w.text[0] not in initials:
		print(w.text[0])
		initials.append(w.text[0])

print(initials)

for c in cases:
	if browser.find_element_by_id(c).text in initials:
		for d in cases:
				splited_c = c.split("-") 
				splited_d = d.split("-") 
				dif = abs(int(splited_c[0])-int(splited_d[0])) >= minl-1
				dif2 = abs(int(splited_c[1])-int(splited_d[1])) >= minl-1
				diag = abs(int(splited_d[0])-int(splited_c[0])) == abs(int(splited_d[1])-int(splited_c[1]))
				if (splited_c[0]==splited_d[0] and dif2) or (splited_c[1]==splited_d[1] and dif) or (diag and dif and dif2):
					browser.find_element_by_id(c).click()
					time.sleep(0.07)
					browser.find_element_by_id(d).click()
					time.sleep(0.07)
