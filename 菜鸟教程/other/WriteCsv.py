import csv

with open('C:\\users\\fang\\Desktop\\writecsv.csv', "w",encoding="utf-8",newline='') as f:
   dict_writer = csv.DictWriter(f, fieldnames=["id", "name", "age"])
   dict_writer.writeheader()
   dict_writer.writerow({"id": "1", "name": "qwe", "age": "14"})
   dict_writer.writerow({"id": "1", "name": "qwe", "age": "14"})
