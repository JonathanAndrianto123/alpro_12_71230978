def sama_gak_yah(t):
    return len(set(t)) == 1

t1 = (90, 90, 90, 90)
t2 = (90, 90, 90, 80)
print(sama_gak_yah(t1))
print(sama_gak_yah(t2))