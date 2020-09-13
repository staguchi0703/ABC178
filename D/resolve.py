def resolve():
    '''
    code here
    '''
    S = int(input())
    res = 0
    if S <3:
        res = 0
    else:
        remain = S % 3
        case = S //3

        res = 0
        num = 3
        while case >=1:
            if case == 1:
                res += 1
            else:
                if remain == 0:
                    res += 1
                else:
                    res += 2
                    res += remain -1
                
            case -= 1
            remain += num
            
            res %= (10**9 +7)
    
    print(res%(10**9 +7))



if __name__ == "__main__":
    resolve()
