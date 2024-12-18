import z3

prog = [2, 4, 1, 3, 7, 5, 1, 5, 0, 3, 4, 3, 5, 5, 3, 0]
N = len(prog)

opt = z3.Optimize()
A = z3.BitVec("A", 3 * (N + 1))
for k in range(N):
    cur_A = A >> (3 * k)
    B = cur_A & 0b111
    B ^= 3
    C = cur_A >> B
    B ^= 5
    B ^= C
    opt.add(B & 0b111 == prog[k])
opt.add(B >> (3 * N) == 0)
opt.minimize(A)

if opt.check() == z3.sat:
    model = opt.model()
    print(model[A])
else:
    print("unsat")
