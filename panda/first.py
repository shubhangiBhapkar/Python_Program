import pandas as pd
import numpy as np
temp=np.array([26,30,28,25,32,22,21])
day=["mon","tue","wed","thu","fri","sat","sun"]
temp_ser=pd.Series(temp,index=day)
print(temp_ser)

carbon_foot={"pune": 450.75,
              "mumbai":550.50,
              "nagpur":425.80,
              "sangamner":400.90
}
cfs=pd.Series(carbon_foot)
print(cfs)

print(temp_ser.head(3))
print(temp_ser.info())
print(temp_ser.describe())

