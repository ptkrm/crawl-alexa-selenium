#!/usr/bin/env python

from selenium import webdriver

driver = webdriver.Firefox()
top = []
f = open('AlexaTopCA.txt', 'w')

for i in range(0, 15):
	driver.get('http://www.alexa.com/topsites/countries;'+str(i)+'/CA')
	elem = driver.find_elements_by_class_name("desc-paragraph")
	for i in elem:
		top.append(i.text)

for i in top:
	f.write(str(i)+'\n')

f.close()

print("END")