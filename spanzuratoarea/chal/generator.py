import copy
import random
import string
from z3 import BitVec, Solver, ULT, ULE, LShR, sat, unsat, Or


flag = "ITEC{tr41m_4l4tur1_d3_34_p4n4_mur1m_474rna71_d3_34}"
L = len(flag)
print(flag)  # ITEC{tr41m_4l4tur1_d3_34_p4n4_mur1m_474rna71_d3_34}

op_6_cnt = 0;
op_5_cnt = 0;
op_4_cnt = 0;
op_3_cnt = 0;
op_2_cnt = 0;
op_1_cnt = 0;

flag = list(flag.encode())

consts = ""
f = [BitVec(f"flag_{i}", 16) for i in range(L)]
s = Solver()
for i in range(L):
    s.add(ULT(f[i], 256))
    s.add(ULE(0, f[i]))

while True:
    op = random.randint(0, 7)
    i = random.randint(0, L - 1)
    j = random.randint(0, L - 1)
    while i == j:
        j = random.randint(0, L - 1)
    if op == 0:
        # (flag[{i}] >> {k}) * (flag[{j}] << {l}) == {ans}\n
        k = random.randint(1, 3)
        l = random.randint(1, 3)
        ans = (flag[i] >> k) * (flag[j] << l)
        cond = (LShR(f[i], k)) * (f[j] << l) == ans
        consts += f"""
        tmp1 = ord(cuvant[{i}]) \n
        tmp2 = ord(cuvant[{j}]) \n
        assert ((tmp1 >> {k}) * (tmp2 << {l})) == {ans} \n\n
        """
    elif op == 1:
        # (flag[{i}] ^ {k}) ^ flag[{j}] == {ans}\n
        if op_1_cnt >= 10:
            continue
        k = random.randint(1, 255)
        ans = ((flag[i] ^ k) ^ flag[j])
        cond = ((flag[i] ^ k) ^ flag[j]) == ans
        consts += f"""
        tmp1 = ord(cuvant[{i}]) \n
        tmp2 = ord(cuvant[{j}]) \n
        assert (tmp1 ^ {k}) ^ tmp2 == {ans} \n\n
        """
        op_1_cnt += 1 
    elif op == 2:
        # (flag[{i}] & {k}) == {ans}\n
        if op_2_cnt >= 10 :
            continue
        k = random.randint(1, 255)
        ans = (flag[i] & k)        
        cond = (flag[i] & k) == ans
        consts += f"""
        tmp1 = ord(cuvant[{i}]) \n
        assert (tmp1 & {k}) == {ans} \n\n
        """
        op_2_cnt += 1
    elif op == 3:
        # (flag[{i}] + flag[{j}]) == {ans}\n
        if op_3_cnt >= 10 :
            continue
        ans = (flag[i] + flag[j])        
        cond = flag[i] + flag[j] == ans
        consts += f"""
        tmp1 = ord(cuvant[{i}]) \n
        tmp2 = ord(cuvant[{j}]) \n
        assert (tmp1 + tmp2) == {ans} \n\n
        """
        op_3_cnt += 1
    elif op == 4:
        # (flag[{i}] - flag[{j}]) == {ans}\n
        if op_4_cnt >= 10 :
            continue
        ans = (flag[i] - flag[j])        
        cond = flag[i] - flag[j] == ans
        consts += f"""
        tmp1 = ord(cuvant[{i}]) \n
        tmp2 = ord(cuvant[{j}]) \n
        assert (tmp1 - tmp2) == {ans} \n\n
        """
        op_4_cnt += 1
    elif op == 5:
        # (flag[{i}] * flag[{j}]) == {ans}\n
        if op_5_cnt >= 10 :
            continue
        ans = (flag[i] * flag[j])        
        cond = flag[i] * flag[j] == ans
        consts += f"""
        tmp1 = ord(cuvant[{i}]) \n
        tmp2 = ord(cuvant[{j}]) \n
        assert (tmp1 * tmp2) == {ans} \n\n
        """
        op_5_cnt += 1
    elif op == 6:
        # (flag[{i}] & flag[{j}]) == {ans}\n
        if op_6_cnt >= 10 :
            continue
        ans = (flag[i] & flag[j])        
        cond = flag[i] & flag[j] == ans
        consts += f"""
        tmp1 = ord(cuvant[{i}]) \n
        tmp2 = ord(cuvant[{j}]) \n
        assert (tmp1 & tmp2) == {ans} \n\n        
        """
        op_6_cnt += 1
    else:
        # (flag[{i}] >> {k}) & {l} == {ans}\n
        k = random.randint(1, 7)
        l = random.randint(0, 255)
        ans = (flag[i] >> k) & l 
        cond = (LShR(f[i], k)) & l == ans
        consts += f"""
        tmp1 = ord(cuvant[{i}]) \n
        assert ((tmp1 >> {k}) & {l}) == {ans} \n\n 
        """
    s.add(cond)
    assert s.check() == sat
    m = s.model()
    print('!!!!!',m)
    flag_rec = [m[f[i]].as_long() for i in range(L)]
    s_tmp = copy.deepcopy(s)
    s_tmp.add(Or([f[i] != flag_rec[i] for i in range(L)]))
    if s_tmp.check() == unsat:
        break
print(consts)