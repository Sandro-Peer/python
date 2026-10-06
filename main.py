import random


def setup():
    numbs = []
    i = 1
    while i < 46:
        numbs.append(i)
        i += 1

    return numbs

def lottoziehung(zz):
    numbs = setup()
    n = 44
    pulls = zz
    DictCnts = {}
    for i in range(1, 46):
        DictCnts[i] = 0

    for x in range (pulls):
        if n > 0:
            index = random.randint(0, n)
            #x = numbs[index]
            #numbs.remove(x)
            #numbs.append(x)
            numbs[index], numbs[n] = numbs[n], numbs[index]

            stats(x, DictCnts)
            n = n-1
        else:
            break
    print(DictCnts)
    return numbs[44]

def statsZiehungen(zz):
    DictCnts = {}
    for i in range(1, 46):
        DictCnts[i] = 0

    for x in range(zz):
        y = lottoziehung(1)
        DictCnts[y] += 1

    print(DictCnts)


def stats(zahl, DictCnts):
    DictCnts[zahl] += 1


statsZiehungen(1000)