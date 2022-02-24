from easygui import *

name = enterbox("请输入名字","我的成绩单")
classes = enterbox("请输入班级","我的成绩单")
score = int(enterbox("请输入分数","我的成绩单"))

level = "E"

if score ==100:
    level = "S"
elif score >=95:
    level = "A+"
elif score >= 90:
    level = "A"
elif score >= 80:
    level = "B"
elif score >= 70:
    level = "C"
elif score >= 60:
    level = "D"
else:
    level = "E"



line1 = "|" + "-"*20 + "|\n"
line2 = "|" + " "*7+ "report" + ' '*7 + "|\n"
line3 = "|" + "-"*5 + "Hello Code" + '-'*5 + "|\n"
line4 = "|" +  " name : "
while len(name) < 12:
    name +=' '
line4 += name[0:11] +" |\n"

line5 = "|" + " class: "
while len(classes) < 12:
    classes += " "
line5 += classes[0:11] +" |\n"

line6 = "|" +  " score: "
score = str(score)
while len(score) < 12:
    score += " "
line6 += score[0:11] +" |\n"

line7 = "|" +  " level: "
while len(level) < 12:
      level += " "

line7 += level[0:11] +" |\n"

line8 = "|" + "_"*20 + "|\n"


line = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8

# 可以不使用文件
with open("file.txt","w") as file:
    file.write(line)
with open("file.txt") as file:
    print(file.read())
