def sum_of_squares(n):
    squares=0
    for v in range(n):
        if v % 2>0:
            squares+=v**2
    return squares

    
print(sum_of_squares(10))