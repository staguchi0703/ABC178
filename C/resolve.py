def resolve():
    '''
    code here
    '''
    N = int(input())

    res = 0
    if N < 3:
        if N <= 1:
            res = 0
        elif N == 2:
            res = 2
    else:
        res = ((10**(N-2)) % (10**9+7))
        res *= N*(N-1)
        res -= N*2*(N-1)
    
    print(res%((10**9+7)))

if __name__ == "__main__":
    resolve()
