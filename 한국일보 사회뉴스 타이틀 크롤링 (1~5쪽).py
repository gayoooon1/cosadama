from urllib.request import urlopen 
from bs4 import BeautifulSoup
import openpyxl

excel_file = openpyxl.Workbook()
excel_file.remove(excel_file.active)
excel_sheet = excel_file.create_sheet('사회뉴스')  # sheet 이름 작성 
excel_sheet.column_dimensions['B'].width = 100   # 컬럼 크기 정하기 

excel_sheet.append(['번호','제목']) #sheet에 표제목 넣기 

titleli=[]
for pgnum in range(1,6):
    url = 'https://www.hankookilbo.com/News/Society/HC01?Page='
    page = urlopen(url+str(pgnum))
    soup = BeautifulSoup(page, "html.parser")

    titles = soup.find_all('p', class_='title')   # 각 타이틀에서 p 중 class가 title인 것 가져오기 
    for title in titles: 
            value=title.get_text()  # 타이틀 개수와 타이틀 내용 
            titleli.append(value)

for index in range(len(titleli)):
    excel_sheet.append([index+1, titleli[index]])
    
cell_A1 = excel_sheet['A1']
cell_A1.alignment = openpyxl.styles.Alignment(horizontal="center")  # A1 양식 center로!
cell_B1 = excel_sheet['B1']
cell_B1.alignment = openpyxl.styles.Alignment(horizontal="center")  # B1 양식 center로!

excel_file.save('한국일보 사회뉴스 타이틀 크롤링 (1~5쪽).xlsx')
excel_file.close()