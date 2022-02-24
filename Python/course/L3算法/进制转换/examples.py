# 进制转换的例题

def min_to_hour(mins):
    min = mins % 60
    hour = mins // 60
    print(hour,'小时', min,'分')

def day_to_week(days):
    day = days % 7
    week = days // 7
    
    print ('第',week,'周', '第', day,'天')



if __name__ =='__main__':
    for i in range(20):
        day_to_week(i)