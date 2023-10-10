#!/usr/bin/env python
# coding: utf-8

# In[8]:


from importlib.resources import read_binary
from urllib import request
import re
import time
import random
import csv
from ua_info import ua_list

class MaoyanSpider(object): 
 
    def __init__(self):
        self.url = 'https://www.archdaily.com/search/projects/year/{}'
        

    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
      
        
        self.parse_html(html)
    
    
    def parse_html(self,html):
        
 
        re_bds = '<h3 class="search-header__title">(.*?)</h3>'
        
        pattern = re.compile(re_bds)
        
        r_list = pattern.findall(html)
 
        self.save_html(r_list)

    def save_html(self,r_list):
     
        with open('arch.csv','a',newline='',encoding="utf-8") as f:
          
            writer = csv.writer(f)
       
            for r in r_list:
                name = r[0].strip()
                
                L = [name,]
               
                writer.writerow(L)
                print(name,)

    def run(self):
 
        for offset in range(2017,2019,1):
            url = self.url.format(offset)
            
            self.get_html(url)
 
            time.sleep(random.uniform(1,2))

if __name__ == '__main__':
    
    try:
        spider = MaoyanSpider()
        spider.run()
    except Exception as e:
        print("错误:",e)
        
#Close the webpage
driver.quit()


# In[ ]:




