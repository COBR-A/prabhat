def lst_find():
    lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
    f = lambda n: (max(n), min(n))
    maxv, minv = f(lst)
    print(f"Max: {maxv}, Min: {minv}")

def fibb(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

def sb(h):
    sb = sum(i**3 for i in range(1, h))
    return sb


