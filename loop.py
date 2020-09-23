# while 迴圈
# n = 1
# while n < 5:
#     print('變數n的資料是: ', n)
#     n +=1

# 1+2+3+4+5+6+7+8+9+10
# num = int(input('請輸入數字: '))
# n = 1
# sum = 0
# while n <= num:
#     print(n)
#     sum = sum + n
#     n += 1
# print('1加到%d的總和=' %num, sum)

# for 迴圈
# for x in [4, 1, 2]:
#     print(x)

# range
# sum = 0
# n = int(input('請輸入數字: '))
# for x in range(1, n + 1):
#     sum = sum + x
# print(sum)


# break
# n = 1
# while n < 5:
#     if n == 3:
#         break
#     n += 1
# print(n)

# continue
# n = 0
# for x in [1, 2, 3, 4]:
#     if x % 2 == 0:
#         continue
#     print(x)


# for - else 的點單範例
# sum = 0
# for n in range(1, 11):
#     sum += n
# else:
#     print(sum)

# 綜合範例:只找出整數平方根
# 輸入9，得到3
# 輸入11，得到沒有整數平方根
# n = input('輸入一個正整數: ')
# n = int(n) 
# for i in range(n):
#     if i * i == n:
#         print('整數平方根: ', i)
#         break
# else:
#     print('沒有整數平方根')

# 猜數字遊戲
# ans = 30
# guess = 0
# while guess != ans:
#     guess = int(input('猜猜0~100的數字: '))
#     if guess > ans:
#         print('請猜小一點')
#     elif guess < ans:
#         print('請猜大一點')
#     else:
#         print('恭喜答對')

# for 迴圈的進階應用
# for i in range(1, 10):
#     for j in range(1, 10):
#         if j <= i:
#             print('A', end ='') # end = '' 輸出完空一格，下次輸出不換行
#     print() # 換行輸出

# 99乘法表
# for i in range(1, 100):
#     for j in range(1, 100):
#         result = i * j
#         print('%d*%d= %-7d'%(i, j, result), end ='') # %-3d 表示每一個輸出預留3格，同時靠左輸出
#     print() 

# 99乘法表，用while迴圈
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        result = i * j
        print('%d*%d=%-3d'%(i, j, result), end = '')
        j += 1
    print()
    i += 1
