#!/usr/bin/env python
# coding: utf-8

# ## 🐍COSADAMA SUMMER CAMP WEEK 4
# ### 실제 활용해보며 익히는 MySQL 기본 + 문법

# #### 1. Schema 정의   
# table을 두 개로 만든다. foreign key, primary key -> table 분리해서 사용   
# 랭킹 정보 저장, items에 가서 item 코드 가져오면 되는 구조

# In[ ]:


create table ranking (
    num int auto_increment not null primary key,
    main_category varchar(50) not null,# 변동 가능성 있음, 가변적 활용, 넉넉하게 잡아야
    sub_category varchar(50) not null,
    item_ranking tinyint unsigned not null, # 200위까지 저장하기 위함
    item_code varchar(20) not null,
    foreign key (item_code) references items(item_code) #item 코드를 가지고 참조할 수 있도록 함
);


# In[ ]:


create table items (
   item_code varchar(20) not null primary key,
    title varchar(200) not null,
    ori_price int not null,
    discount_price not null,
    discount_percent int not null,
    provider varchar(100) # 판매처
);


# create databse bestproducts   
# create table tablename(field definitions)
# 
# 한글 처리에 문제가 있을 경우 db, table에 default charset=utf8 collate=utf8_bin 옵션을 모두 추가해서 실행

# In[38]:


import pymysql
db= pymysql.connect(host='localhost', port=3306, user='root', passwd='Myloxyloto5!', db='bestproducts', charset='utf8')
cursor = db.cursor()

sql = '''
create table items (
    item_code varchar(20) not null primary key,
    title varchar(200) not null,
    ori_price int not null,
    discount_price int not null,
    discount_percent int not null,
    provider varchar(100)
);
'''

cursor.execute(sql)

sql = '''
create table ranking (
    num int auto_increment not null primary key,
    main_category varchar(50) not null,
    sub_category varchar(50) not null,
    item_ranking tinyint unsigned not null,
    item_code varchar(20) not null,
    foreign key (item_code) references items(item_code)
);
'''

cursor.execute(sql)

db.commit()
db.close()


# #### 2. Crawling

# #### main/sub category info + product info + product code + seller

# In[52]:


import requests
from bs4 import BeautifulSoup
import pymysql
db= pymysql.connect(host='localhost', port=3306, user='root', passwd='Myloxyloto5!', db='bestproducts', charset='utf8')
cursor = db.cursor()

res = requests.get('http://corners.gmarket.co.kr/Bestsellers')
soup = BeautifulSoup(res.content, 'html.parser')

categories = soup.select('div.gbest-cate ul.by-group li a')
for category in categories:
    get_category('http://corners.gmarket.co.kr'+ category['href'], category.get_text())


# http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01

# In[3]:


def get_category(category_link, category_name):
    res =  requests.get(category_link)
    soup = BeautifulSoup(res.content, 'html.parser') #main category no sub
    
    get_items(soup, category_name, 'ALL')
    sub_categories = soup.select('div.navi.group ul li > a') #li 바로 밑에 것들만 올 수 있도록
    for sub_category in sub_categories: #sub
        res = requests.get('http://corners.gmarket.co.kr'+ sub_category['href'])
        soup = BeautifulSoup(res.content, 'html.parser')
        get_items(soup, category_name, sub_category.get_text())


# In[ ]:


#def get_items(html, category_name, sub_category_name):
    #items_result_list = list()
    #best_item = html.select('div.best-list')
    #for index, item in enumerate(best_item[1].select('li')): #product list
        title = item.select_one('a.itemname').get_text()
        ori_price = item.select_one('div.o-price').get_text()
        dis_price = item.select_one('div.s-price strong span').get_text()
        discount_percent = item.select_one('div.s-price em').get_text()


# 많은 페이지를 크롤링하다 보면 get_text 메서드에 대해 호출을 못하게 될 수도 있음. 해당 부분이 없는 경우.   
# 태그가 없는 경우, 태그는 있는데 데이터가 없는경우
# 위의 경우 할인 적용이 안되거나 등
# 
# string으로 오기 때문에 가격에서 '원' 글자와 쉼표도 빼줘야함

# In[49]:


import re


# In[51]:


def get_items(html, category_name, sub_category_name):
    items_result_list = list()
    best_item = html.select('div.best-list')
    for index, item in enumerate(best_item[1].select('li')): #product list
        data_dict = dict()
        
        ranking = index+1
        title = item.select_one('a.itemname')
        ori_price = item.select_one('div.o-price')
        dis_price = item.select_one('div.s-price strong span')
        discount_percent = item.select_one('div.s-price em')
        
        if ori_price == None or ori_price.get_text() == '': # 객체가 없으면 원래 가격을 discount price로 덮어쓰기
            ori_price = dis_price
        if dis_price == None:
            ori_price, dis_price = 0,0
        else: 
            ori_price = ori_price.get_text().replace(',', '').replace('원','')
            dis_price = dis_price.get_text().replace(',', '').replace('원', '')
        
        if discount_percent == None or discount_percent.get_text() == '':
            discount_percent = 0
        else:
            discount_percent = discount_percent.get_text().replace('%','')
        
        product_link = item.select_one('div.thumb > a')
        item_code = re.split("=|&",product_link.attrs['href'])[1]

        
        res = requests.get(product_link.attrs['href'])
        soup = BeautifulSoup(res.content, 'html.parser')
        provider = soup.select_one('div.item-topinfo_headline > p > a > strong')
        if provider == None:
            provider = ''
        else:
            provider = provider.get_text()
        data_dict['category_name'] = category_name
        data_dict['sub_category_name'] = sub_category_name
        data_dict['ranking'] = ranking
        data_dict['title'] = title.get_text()
        data_dict['ori_price'] = ori_price
        data_dict['dis_price'] = dis_price
        data_dict['discount_percent'] = discount_percent
        data_dict['item_code'] = item_code
        data_dict['provider'] = provider
        
        save_data(data_dict)
        #print(category_name, sub_category_name, ranking,item_code, provider, title.get_text(), ori_price, dis_price, discount_percent)


# `
# create table ranking (   
#     num int auto_increment not null primary key,   
#     main_category varchar(50) not null,# 변동 가능성 있음, 가변적 활용, 넉넉하게 잡아야   
#     sub_category varchar(50) not null,   
#     item_ranking tinyint unsigned not null, # 200위까지 저장하기 위함   
#     item_code varchar(20) not null,   
#     foreign key (item_code) references items(item_code) #item 코드를 가지고 참조할 수 있도록 함   
# );
# `

# In[45]:


item_info = {'category_name':'ALL', 'sub_category_name':'ALL', 'ranking':1, 'title':'투투22 투투 단하루 균일가+15+22%찬스 슬랙스/청바지 5XL','ori_price':49500,'dis_price':14900,'discount_percent':69,'item_code':'1368640307','provider':'투투22'}


# In[44]:


sql.replace('\n','')


# In[50]:


def save_data(item_info):
    sql = """select count(*) from items where item_code = '""" + item_info['item_code'] + """';"""
    cursor.execute(sql)
    result = cursor.fetchone()
    if result[0] == 0:
        sql = """insert into items values('""" + item_info['item_code'] + """',
        '""" + item_info['title'] + """',
        '""" + str(item_info['ori_price']) + """',
        '""" + str(item_info['dis_price']) + """',
        '""" + str(item_info['discount_percent']) + """',
        '""" + item_info['provider'] + """')"""
        print(sql)
        cursor.execute(sql)
        
    sql = """insert into ranking (main_category, sub_category, item_ranking, item_code) values('""" + item_info['category_name'] + """',
    '""" + item_info['sub_category_name'] + """',
    '""" + str(item_info['ranking']) + """',
    '""" + item_info['item_code'] + """')"""
    cursor.execute(sql)
    


# ### count sql
# - count : 검색 결과의 row 수를 가져올 수 있는 sql 문법
# - sql 예제 : select count(*) from items

# In[46]:


sql = """select count(*) from items where item_code = '""" + item_info['item_code'] + """';"""
cursor.execute(sql)
result = cursor.fetchone()
print(result[0])


# In[47]:


sql


# #### 목적   
# * 실제로 데이터 베이스를 사용하는 방법을 현업스타일로!
# * 현실 세계의 데이터를 어떻게 테이블로 정의할 것인가
# * 어떻게 데이터를 넣을 것인가
# * 저장된 데이터를 분석한다. SQL만 쓰는 경우 + 프로그래밍에서 데이터를 분석해서, 풀스택으로 서비스화함

# ### DELETE TABLE DATA

# In[ ]:


import pymysql
db= pymysql.connect(host='localhost', port=3306, user='root', passwd='Myloxyloto5!', db='bestproducts', charset='utf8')
cursor = db.cursor()

sql = 'delete from items'
cursor.execute(sql)

sql = 'delete from ranking'
cursor.execute(sql)

db.commit()
db.close()

