import time
from selenium import webdriver


driver = webdriver.Chrome('C:\chromedriver.exe')  
driver.get('http://justnotepad.com/ru/');
time.sleep(5) 

#--------------------���� ������ � ����---------------------------------
div=driver.find_element_by_id("draft_form")
g=div.find_element_by_id("editable_text")
g.send_keys(".,/\-=+0123456789*~@#$%^&*()_{}[]abvgdzxcewqrtyuiopljkmn ")
#--------------�������� ������� ������ ��������------------------------------

div2=driver.find_element_by_id("header")
gk=div2.find_element_by_id("delete_draft")
gk.click()

div3=driver.find_element_by_id("confirm_lightbox")
cancel=div3.find_element_by_id("cancel")
cancel.click()
time.sleep(3)
#------------------------������� ��������----------------
div2=driver.find_element_by_id("header")
gk=div2.find_element_by_id("delete_draft")
gk.click()

div3=driver.find_element_by_id("confirm_lightbox")
ok=gk=div3.find_element_by_id("ok")
ok.click()

#-------------------������� ���������----------------------
g=div.find_element_by_id("editable_text")
g.send_keys(".,/\-=+0123456789*~@#$%^&*()_{}[]abvgdzxcewqrtyuiopljkmn  ")
time.sleep(5)
d=driver.find_element_by_id("drafts")
s=d.find_element_by_id("delete_all_drafts")
s.click()



div3=driver.find_element_by_id("confirm_lightbox")
ok=gk=div3.find_element_by_id("ok")
ok.click()

#--------------------� ������ ��� ������� ������---------------------
style=driver.find_element_by_id("style_mode")
style_ok=style.find_element_by_id("night_mode")
style_ok.click()
#---------------------------��������------------------------- 
time.sleep(1)
style_ok=style.find_element_by_id("day_mode")
style_ok.click()
time.sleep(2)
#---������ �� �������------------------------------------------


s2=driver.find_element_by_id("footer_menu")
s2.click()
time.sleep(1)
driver.get('http://justnotepad.com/ru/');
time.sleep(3)
driver.find_element_by_css_selector("a[href='faq/']").click()
driver.get('http://justnotepad.com/ru/');
time.sleep(3)
driver.find_element_by_css_selector("a[href='terms/']").click()
driver.get('http://justnotepad.com/ru/');
time.sleep(3)
driver.find_element_by_css_selector("a[href='feedback/']").click()
driver.get('http://justnotepad.com/ru/');
time.sleep(3)

#--------------������� �� ���� ������----------------------------------


s1=driver.find_element_by_id("footer_lang")
s1.click()
time.sleep(1)


#-----------------------������� �� ����� ����--------------------------
div2=driver.find_element_by_id("header")
new=div2.find_element_by_id("new_draft")
new.click()
#-------------------------------------



time.sleep(5) # �������� � �����
driver.quit()



