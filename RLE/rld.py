def rld(mess):
    
    if not mess: #hvis ikke der er noget indholde, altså mess ikke har en værdi 
        return "no input"
        exit()
    
    res = ''
    count = 0
    for c in mess:
        if c.isdigit():
            count = count*10 + int(c)
        else:
            res += c*count
            count = 0
    return  res
