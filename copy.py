n = 7  # int(input())
m = [[0 for i in range(n)] for j in range(n)]
n2 = n ** 2
# a = []
for i in range(1, n2 + 1):
     if i <= n:
         m[0][i - 1] = i
     elif i < n * 2:
         m[i - n][n - 1] = i
     elif i < n * 3 - 1:
         m[n-1][(n*2) - 2 - i] = i
         #print(i, end=' ')
#         for j in range(n):
#             if j < n:
#                 m[j].append(0)
#             else:
#                 m[j].append(i)
#     # print(i, end = ' ')
print(m)
for r in range(n):
    for c in range(n):
        print(m[r][c], end=' ')
    print()

