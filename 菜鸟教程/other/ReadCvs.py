import csv

with open('C:\\users\\fang\\Desktop\\demo.csv',encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
       # print(row)
         print(row.get("name"),end="-")
         print(row["age"])