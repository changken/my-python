from sys import stdin
BigMonth = ['1','3','5','7','8','10','12']
SmallMonth = ['2','4','6','9','11']
for row in stdin:
    ans = row.replace('\n','')
    if ans in BigMonth:
        print('>')
    elif ans in SmallMonth:
        print('<')
    else:
        print('!')
