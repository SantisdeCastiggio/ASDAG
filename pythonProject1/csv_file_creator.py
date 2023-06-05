import csv
with open('case1.csv','a',newline='', encoding="utf-8") as f:
   w = csv.writer(f)
   w.writerow(['Кейс', 'название О файла', 'количество строк','ОБПО','загружен'])
