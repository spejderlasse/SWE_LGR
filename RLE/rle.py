import sys
import time

def rle(mess):
    
    if not mess: #hvis ikke der er noget indholde, altså mess ikke har en værdi 
        return "no input"
        exit()
    str(mess)
        
    old = mess[0]
    count = 1
    res = []
    for c in mess[1:]:
        if c== old:
            count+=1
        else:
            res.append(f'{count}{old}')
            count = 1
            old = c
    res.append(f'{count}{old}')
    return ''.join(res)

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


if __name__ == '__main__':
    time.sleep(1)#hvis programmet afvikles for hurtigt vil dette opfattes som en fejl ifm fuzzing
    argv = sys.argv
    if argv[1] == "-d":
        print (rld(argv[2]))
    if argv[1] == "-e":
        with open(argv[2],'r') as f:
            print(rle(f.read())) 
#    print(argv)