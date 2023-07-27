

def checkGame(lst: list):
    lst.append([lst[0][0], lst[1][0], lst[2][0] ])
    lst.append([lst[0][1], lst[1][1], lst[2][1] ])
    lst.append([lst[0][2], lst[1][2], lst[2][2] ])
    lst.append([lst[0][0], lst[1][1], lst[2][2] ])
    lst.append([lst[0][2], lst[1][1], lst[2][0] ])
    starCount = 0
    for item in lst:
        starCount += item.count("*")
        if item.count("o") == 3:
            return "o"
        if item.count("x") == 3:
            return "x"
        
    if( starCount == 0 ):
        return "d"
    
    return "n"
