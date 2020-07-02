 #encoding utf-8
old = [u'ا', u'ە', u'ب', u'پ', u'ت', u'ج', u'چ', u'خ', u'د', u'ر', u'ز', u'ژ', u'س', u'ش', u'ف', u'ڭ', u'ل',\
        u'م', u'ھ', u'و', u'ۇ', u'ۆ', u'ۈ', u'ۋ', u'ې', u'ى', u'ي', u'ق', u'ك', u'گ', u'ن', u'غ',u'؟']
new = [u'a', u'e',  u'b', u'p', u't', u'j', u'ch', u'x', u'd', u'r', u'z', u'j', u's', u'sh', u'f', u'ng', u'l',\
         u'm', u'h', u'o', u'u', u'ö', u'ü', u'w', u'é', u'i', u'y', u'q', u'k', u'g', u'n', u'gh',u'?']
print('ھۆججەتتىن ئوقۇمدۇ ياكى قولدا كىرگۈزەمسىز؟\n')
print(' ھۆججەتتىن ئوقۇماقچى بولسا 1 نى بىسىڭ \n قولدا كىگۈزسىڭىز 2 نى بىسىڭ')
xo = int(input())
xin = ""
if xo == 1:
    print('ھۆججەت ئورنىنى كىرگۈزۈڭ')
    file = str(input())
    #a = open('a.txt',mode='r')
    a = open(file,mode='r')
    a = a.read()
    b = list(a.lower())
elif xo ==2:
    print('قېنى يېزىق كىرگۈزۈڭ')
    dd = str(input())
    b = dd
else:
    exit()
tr=""
for i in range(0,len(b)):
    if b[i] == 'ئ':
        continue
    x = 0
    for j in range(0,len(old)):
        if b[i] == old[j]:
            tr += new[j]
            x=1
            break
    if x == 0:
        tr += b[i]
print(tr)
