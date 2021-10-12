def countVogals(string):
    vogalsInString={}
    vogals=['a','e','i','o','u']
    countVogals=[]
    for char in string:
        if char.lower() in vogals:
            countVogals.append(char.lower())

    for v in vogals:
       vogalsInString[v]=countVogals.count(v)
    
    return vogalsInString

print(countVogals('ONOMATOPEYA'))