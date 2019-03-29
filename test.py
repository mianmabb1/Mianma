#做了一个方案1
import re
f = open('Test')
data = f.read()
a = 1

#大写字母开头单词
# pattern = r'\b[A-Z]\S*\b'

#匹配数字
# pattern = r'-?\d+\.?/?\d*%?'

#日期替换
pattern = r'\d{4}\.\d{1,2}\.\d{1,2}'

regex = re.compile(pattern)
for i in regex.finditer(data):
    # print(i.group())
    s = i.group()
    date = re.sub(r'\.','-',s)
    data = re.sub(pattern,date,data)

f = open('Test','w')
f.write(data)
f.close()
