def is_multiple(n,m):
    try:
        if n % m == 0:
            return True
        else:
            return False
    except Exception:
        raise Exception(f"{n} is not multiple of {m}")
        
print(is_multiple(22,3))