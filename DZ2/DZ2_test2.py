mystr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
mystr[1] = ''.join(['"',"%02d" % int(mystr[1]),'"'])
mystr[3] = ''.join(['"',"%02d" % int(mystr[3]),'"'])
mystr[8] = ''.join(['"','+',"%02d" % int(mystr[8]),'"'])
result = ' '.join(mystr)
print(result)
