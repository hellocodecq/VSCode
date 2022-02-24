import csv

def create_data():
    file = open("file.csv",'w',encoding='gbk')
    writer = csv.writer(file)
    rows = [['植物','生长情况'],
    ['A03',3],
    ['A07',7],
    ['A02',2],
    ['A04',4],
    ['A08',8]]
    writer.writerows(rows)
    file.close()

file = open('file.csv')
reader = csv.reader(file)

reader = list(reader)
for row in reader[1:]:
    if int(row[1]) >= 6:
        print(row)