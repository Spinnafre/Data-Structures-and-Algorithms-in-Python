def sum_of_squares(data):
    return sum([v**2 for v in range(data) if data>0] )
print(sum_of_squares(10))