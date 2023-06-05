import csv
with open('case1.csv','w',newline='', encoding="utf-8") as f:
   w = csv.writer(f)
   w.writerow(['1',"filename", '' , "", ''])