import random
print("Введите количество чисел в массиве A(целое число)")
n=int(input())
def a(nn):
    aa=[]
    nn=n
    for i in range(nn):
        x = random.randint(0, 25)
        aa.append(x)
    return aa
ans_a=a(n)
print("Массив А:",ans_a)
print()
print("Введите количество чисел в массиве B(целое число)")
h=int(input())
def b(hh):
    bb=[]
    hh=h
    for i in range(hh):
        x = random.randint(0, 25)
        bb.append(x)
    return bb
ans_b=b(h)
print("Массив В:",ans_b)
print()
ans=[]
for k in range(n):
    for g in range(h):
        if(ans_a[k]==ans_b[g]):
            ans.append(ans_a[k])
new=list(set(ans)) #удаление повторяющихся элементов
if(len(new)!=0):
    print("Решение:")
    print(new)
else:
    print("Нет одинаковыз элементов :(")

