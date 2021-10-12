# def sum_of_squares(n):
#     squares=0
#     for v in range(n):
#         if v % 2>0:
#             squares+=v**2
#     return squares

def sum_of_squares(n):
    return sum([v**2 for v in range(n) if v%2>0])

    
print(sum_of_squares(20))