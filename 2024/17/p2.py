import z3

prog = [2, 4, 1, 3, 7, 5, 1, 5, 0, 3, 4, 3, 5, 5, 3, 0]

s = z3.Solver()
A = z3.BitVec("A", 3 * 17 - 2)
for i in range(16):
    cur_A = A >> (3 * i)
    B = cur_A & 0b111
    B ^= 3
    C = cur_A >> B
    B ^= 5
    B ^= C
    s.add(B & 0b111 == prog[i])

if s.check() == z3.sat:
    print(s.model()[A])
else:
    print("unsat")
