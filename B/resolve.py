def resolve():
    '''
    code here
    '''
    a, b, c, d = [int(item) for item in input().split()]

    print(max(a*c,a*d,b*c,b*d))


if __name__ == "__main__":
    resolve()
