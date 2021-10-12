def minmax(data):
    max=0
    min=data[0]
    for v in data:
        if v>max:
            max=v
        if v<min:
            min=v
               
    return (min,max)
print(minmax([0,2,5]))
