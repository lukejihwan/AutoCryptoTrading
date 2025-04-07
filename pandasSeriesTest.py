from pandas import Series

date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05']
xrp_close = [512, 508, 512, 507, 500]
s = Series(xrp_close, index=date)
# slicing 하는법 1번
print(s[['2018-08-02', '2018-08-04']])

# slicing 하는법 2번
print(s['2018-08-01': '2018-08-03'])

# Series에 값 추가하는 법
s['2018-08-06'] = 490

# Series에 값 삭제하는 법
print(s.drop('2018-08-01'))
print(s)

# Series에 사칙연산 적용하는 법
n = Series([100,200,300,400])
print(n/10)