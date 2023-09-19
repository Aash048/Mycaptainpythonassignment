 
n = 13
series = [0,1]

while len(series) < n:
    series.append(series[-1] +series[-2])
    
print (series)


