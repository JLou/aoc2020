with open('inputs/13.txt', 'r') as f:
    min_timestamp = int(f.readline())
    buses = f.readline().split(',')
    buses_id = [int(x) for x in buses if x != 'x']
    
wait = 0
found_bus = False
result = None
while not found_bus:
    res = [bus_id*wait for bus_id in buses_id if (wait + min_timestamp) % bus_id == 0]
    if res:
        found_bus = True
        result = res[0]
    else:
        wait += 1

print(result)

def inverse(a: int, n: int):
    """
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
    Find t such that a*t ≋ 1 (mod n)
    Examples:
    >>> inverse(3, 11)
    4
    which satisfies 3*4 ≋ 1 (mod 11)
    """

    t = 0
    newt = 1
    r = n
    newr = a

    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)

    if r > 1:
        raise Exception("a is not invertible")
    if t < 0:
        t += n

    return t

def crt(remainders:list, modulos:list):
    """
    Check-proofed against https://github.com/bsounak/Aoc2020/blob/45b233ac30121425675fda5763a4942ce55e8c1d/day13.py#L83
    Solve according to chinese remainder theorem
    Implementation follows this tutorial
    https://www.youtube.com/watch?v=zIFehsBHB8o
    Examples:
    >>> a = [0, 12, 55, 25, 12]
    >>> m = [7, 13, 59, 31, 19]
    >>> solve_crt(a, m)
    1068781
    >>> a = [2, 3, 2]
    >>> m = [3, 5, 7]
    >>> solve_crt(a, m)
    23
    """
    N = 1
    for n in modulos:
        N *= n
    ni = [N//n for n in modulos]
    xi = [inverse(x, n) for x,n in zip(ni, modulos)]
    
    s = sum([a*b*c for a,b,c in zip(remainders, ni, xi)])
    
    return int(s % N)

with open('inputs/13.txt', 'r') as f:
    data = f.readlines()
    remainders = [int(v) - idx for idx, v in enumerate(data[1].split(",")) if not v == "x"]
    modulos = [int(v) for v in data[1].split(",") if not v == "x"]

print(crt(remainders, modulos))