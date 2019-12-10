

def getn(n, iterable):
    count = 0
    a = list()
    for x in iterable:
        a.append(x)
        count += 1
        if count == n:
            break
    return a
        
