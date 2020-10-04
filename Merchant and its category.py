#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium


# In[2]:


from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://giftpass.sodexomerchant.com/merchant')


# In[ ]:


content = browser.find_element_by_class_name('content')
container = content.find_element_by_class_name('container')
print(container)


# In[ ]:


header3 = container.find_element_by_tag_name('h3')
category = header3.text
print(type(category))


# In[ ]:


getLink_merch_name = container.find_element_by_tag_name("a")
link_merch_name = getLink_merch_name.get_attribute('href')
print(link_merch_name)


# In[ ]:


list_a = getLink_merch_name.find_elements_by_xpath('//a[@href]')

for a in list_a:
    href = a.get_attribute('href')
    print(href)

get_href = container.find_element_by_tag_name("a")
#     link_merch_name = get_href.get_attribute('href')
#     print(link_merch_name)


# In[ ]:


container = content.find_elements_by_xpath('/html/body/section/div[1]/div[1]')
print(container)


# In[ ]:


import json
list_link = []
merchant_per_category = []

for i in range(10):
    i = i + 1 
    print(i)
    xpath = '/html/body/section/div[1]/div'
    bracket1 = '['
    str_i = str(i)
    bracket2 = ']'
    xpath_container = xpath+bracket1+str_i+bracket2
    container = content.find_elements_by_xpath(xpath_container)
    container_0 = container[0]
    header3 = container_0.find_element_by_tag_name('h3')
    category = header3.text
#     print(category)
    list_a = container_0.find_elements_by_xpath('//a[@href]')
    for cont in list_a:
        hr = container_0.find_element_by_tag_name('<hr>')
        if hr == '' :
            href = cont.get_attribute('href')
        else:
            break
#         print(href)
        list_link.append(href)
    merchant_per_category.append([category,list_link])


# In[ ]:


merchant_per_category[1]


# In[ ]:


container = content.find_elements_by_xpath('/html/body/section/div[1]/div[2]')
print(container)
container[0]


# In[ ]:


hr = container_0.find_element_by_tag_name('hr')


# ## BeatifulSoup

# In[2]:


from bs4 import BeautifulSoup
import requests

url = 'https://giftpass.sodexomerchant.com/merchant'
html_doc = requests.get(url).content
soup = BeautifulSoup(html_doc, 'html.parser')


# In[3]:


mrc_slide = soup.find("div", {"class": "mrc-slides"})
print(mrc_slide)


# In[10]:


category_container = mrc_slide.find("div", {"class": "container"})
category_name = category_container.find('h3').get_text().strip()
merchant_name = category_container.find('span').get_text().strip()
print(category_name)
print(merchant_name)


# In[11]:



merchants_name = [x.get_text().strip()
               for x in category_container.find_all('span')]
print(merchants_name)


# In[46]:


merchants_itsCategory = []
for category_container_i in mrc_slide.find_all("div", {"class": "container"}):
    category_names = category_container_i.find('h3').get_text().strip()
    merchants_name = [x.get_text().strip()
               for x in category_container_i.find_all('span')]
    merchants_itsCategory.append([category_names, merchants_name])


# In[45]:


# print(merchants_itsCategory)
print(merchants_itsCategory[0])


# In[48]:


#Cleansing
for i in range(len(merchants_itsCategory)):
#     print(merchants_itsCategory[i])
    for j in merchants_itsCategory[i][1]:
        if j == 'Detail Information':
          merchants_itsCategory[i][1].remove(j)  
        else:
            continue


# In[ ]:




