# Facut De Antonio & Paul
n = int(input('Fie n indicele din scrierea Sn. n = '))

ord = int(input('ordin = '))

frecv = dict()

sol = [0 for _ in range(n + 1)]

c = 0

def nuestee(perm):
    for i in range(1, n + 1):
        if perm[i] != i:
            return True
    return False

def inmultire(t1, t2):
    global rep
    aux = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        aux[i] = t1[t2[i]]
    t1 = aux
    if nuestee(t1):
        rep += 1
        inmultire(t1, t2)

def GCEA():
    global rep
    rep = 1
    if nuestee(sol):
        rep = 2
        inmultire(sol, sol)
    if rep == ord:
        global c
        c += 1

def bkt(pos):
    if pos == n+1:
        GCEA()
    else:
        for i in range(1, n+1):
            try:
                if frecv[i] != 0:
                    continue
                else:
                    frecv[i] = 1
                    sol[pos] = i
                    bkt(pos + 1)
                    frecv[i] -= 1
            except KeyError:
                frecv[i] = 1
                sol[pos] = i
                bkt(pos + 1)
                frecv[i] -= 1

bkt(1)
print("Facut de Paul si Antonio :)")
print(c)