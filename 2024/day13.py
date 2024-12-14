from sympy import symbols, Eq, solve

file = open("input.txt", "r")
lines = file.readlines()

score = 0
score2 = 0

for index in range(0, len(lines), 4):
    a, b = symbols('a,b')

    A = lines[index].strip()
    B = lines[index+1].strip()
    prize = lines[index+2].strip()

    A_blob = A.split(": ")[1]
    A_blob2 = A_blob.split(", ")
    Ax, Ay = int(A_blob2[0].split("+")[1]), int(A_blob2[1].split("+")[1])

    B_blob = B.split(": ")[1]
    B_blob2 = B_blob.split(", ")
    Bx, By = int(B_blob2[0].split("+")[1]), int(B_blob2[1].split("+")[1])

    P_blob = prize.split(": ")[1]
    P_blob2 = P_blob.split(", ")
    Px, Py = int(P_blob2[0].split("=")[1]), int(P_blob2[1].split("=")[1])

    eq1 = Eq((Ax*a + Bx*b), Px)
    eq2 = Eq((Ay*a + By*b), Py)

    eq3 = Eq((Ax*a + Bx*b), Px+10000000000000)
    eq4 = Eq((Ay*a + By*b), Py+10000000000000)

    r = (solve((eq1, eq2), (a, b)))
    res1, res2 = str(r[a]), str(r[b])
    if not ("/" in res1 or "/" in res2):
        score += (r[a]*3 + (r[b]))

    r = (solve((eq3, eq4), (a, b)))
    res1, res2 = str(r[a]), str(r[b])
    if not ("/" in res1 or "/" in res2):
        score2 += (r[a]*3 + (r[b]))

print(f"Part 1: {score}")
print(f"Part 2: {score2}")