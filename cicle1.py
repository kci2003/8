n = 5  # int(input())
m = [[0 for i in range(n)] for j in range(n)]
n2 = n ** 2
c = n
row = 0 # начальная строка
col = 0 # начальная колонка
i = 1
e = True
step = 1
while i <= n2:
    p = 1
    #print('\n',)
    while p <= 4:#повороты лп\вн\пл\нв
         step = 1
         while step < c and e:
             print(i, end=' ')
             #if p == 1:
             m[row][step -1] = i
             i = i + 1
             if i > n2:
                 e = False
             step = step + 1
             #print('-', end=' ')
         p = p + 1
         print('-', end=' ')
         break
    c = c - 2
    if c == 1:
        print(i, end=' ')
        break
     #
     #
     #break
    #for j in range(n-1):
     #   m[row][j] = i

     # if i <= n:
     #     m[0][i - 1] = i
     # elif i < n * 2:
     #     m[i - n][n - 1] = i
     # elif i < n * 3 - 1:
     #     m[n-1][(n*2) - 2 - i] = i
         #print(i, end=' ')
#         for j in range(n):
#             if j < n:
#                 m[j].append(0)
#             else:
#                 m[j].append(i)
#     # print(i, end = ' ')
# print(m)
for r in range(n):
    for c in range(n):
        print(m[r][c], end=' ')
    print()

