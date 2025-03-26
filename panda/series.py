import pandas as pd
import numpy as np
a=pd.Series([10,20,30,40,50,60,70])
b=pd.Series([1,2,3,4,5,6,7,8,9])
c=pd.Series([10,20,30,40,50])
print(a)
print(b)
print(c)
print(a+b)

squared_ser=a.apply(lambda x: x**2)
print(squared_ser)

series_with_missing=(a+b)
print(a+b)

print(series_with_missing.fillna(series_with_missing.mean()))
#print(temp_ser([(temp_ser > 20)& (temp_ser < 10)])

print(a.iloc[2:5])