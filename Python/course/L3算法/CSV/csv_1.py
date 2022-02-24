import csv


"""读取csv文件"""
def readcsv():
    file = open("file.csv")     # 打开文件
    reader = csv.reader(file)   # 创建csv读取器

    for row in reader:      # 遍历每一行
        for cell in row:    # 遍历每一个单元格
            print(cell, end=' ')
        print()
    file.close()

"""写入单行csv文件"""
def writecsv():
    file = open("file.csv",'w')     # 打开文件
    writer = csv.writer(file)
    writer.writerow((2,"3,2",4))
    file.close()

"""写入多行csv"""
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
writecsv()

