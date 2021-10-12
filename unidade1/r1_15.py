def check_is_diff(list):
    if len(set(list)) != len(list):
        return False
    else:
        return True
    
print(check_is_diff([1,2,3,4,5]))