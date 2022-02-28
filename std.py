import math 
import csv
with open("data.csv",newline='')as f:
    r = csv.reader(f)
    file_data = list(r)
data = file_data[0]


# finding mean
def mean(data):
    n = len(data)
    sum = 0
    for i in data:
        sum += int(i)
    mean = sum/n
    return mean

squaredList = []
for i in data:
    a = int(i)- mean(data)
    a = a**2
    squaredList.append(a)
    
sum = 0
for i in squaredList:
    sum += i
    
result = sum/ ( len(data) - 1 )
std = math.sqrt(result)
print(f"This is your required standard deviation: {std}")


d = [60,61,65,63,98,99,90,95,91,96]
import statistics 

#print( f"Derived std is : { statistics.stdev(d) }")