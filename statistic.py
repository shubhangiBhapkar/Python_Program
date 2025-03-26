import numpy as np
temp=np.array([[10,20,30],[50,60,70]])

#mean
mean_temp=np.mean(temp)
print(mean_temp)

#median
median_temp=np.median(temp)
print(f"{median_temp:.2f}")

#standard deviation
std_temp=np.std(temp)
print(std_temp)

#min percentile
per_temp_0=np.percentile(temp,0)
print(per_temp_0)

#100 percentile
per_temp_100=np.percentile(temp,100)
print(per_temp_100)

#25 percentile
per_temp_25=np.percentile(temp,25)
print(per_temp_25)

#75
per_temp_75=np.percentile(temp,75)
print(per_temp_75)
