def sum_of_squares(n):
    x=[v**2 for v in range(n)] if n>0 else False
    return sum(x)
print(sum_of_squares(20))