import requests
from bs4 import BeautifulSoup
import pymysql
import re

def get_category(category_link, category_name):
    res = requests.get(category_link)
    soup = BeautifulSoup(res.content, 'html.parser')  # main category no sub

    get_items(soup, category_name, 'ALL')
    sub_categories = soup.select('div.navi.group ul li > a')  # li 바로 밑에 것들만 올 수 있도록
    for sub_category in sub_categories:  # sub
        res = requests.get('http://corners.gmarket.co.kr' + sub_category['href'])
        soup = BeautifulSoup(res.content, 'html.parser')
        get_items(soup, category_name, sub_category.get_text())

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

def get_items(html, category_name, sub_category_name):
    items_result_list = list()
    best_item = html.select('div.best-list')
    for index, item in enumerate(best_item[1].select('li')):  # product list
        data_dict = dict()

        ranking = index + 1
        title = item.select_one('a.itemname')
        ori_price = item.select_one('div.o-price')
        dis_price = item.select_one('div.s-price strong span')
        discount_percent = item.select_one('div.s-price em')

        if ori_price == None or ori_price.get_text() == '':  # 객체가 없으면 원래 가격을 discount price로 덮어쓰기
            ori_price = dis_price
        if dis_price == None:
            ori_price, dis_price = 0, 0
        else:
            ori_price = ori_price.get_text().replace(',', '').replace('원', '')
            dis_price = dis_price.get_text().replace(',', '').replace('원', '')

        if discount_percent == None or discount_percent.get_text() == '':
            discount_percent = 0
        else:
            discount_percent = discount_percent.get_text().replace('%', '')

        product_link = item.select_one('div.thumb > a')
        item_code = re.split("=|&", product_link.attrs['href'])[1]

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



    sql = """insert into ranking (main_category, sub_category, item_ranking, item_code) values('""" + item_info[
        'category_name'] + """',
    '""" + item_info['sub_category_name'] + """',
    '""" + str(item_info['ranking']) + """',
    '""" + item_info['item_code'] + """')"""
    cursor.execute(sql)

db= pymysql.connect(host='localhost', port=3306, user='root', passwd='Myloxyloto5!', db='bestproducts', charset='utf8')
cursor = db.cursor()

res = requests.get('http://corners.gmarket.co.kr/Bestsellers')
soup = BeautifulSoup(res.content, 'html.parser')

categories = soup.select('div.gbest-cate ul.by-group li a')
for category in categories:
    get_category('http://corners.gmarket.co.kr'+ category['href'], category.get_text())