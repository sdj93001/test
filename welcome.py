arr = [1,2,3,4,4,6,7,8]
arr.remove(4)
print(arr)



'''
# 输出100以内的质数。

j = 2
while j <=100000:
    i = 2
    flag = True
    while i<= j ** 0.5  :

        if ( j % i == 0 ):
            flag = False
            break
        i +=1

    if flag : pass
        #print ( j )

    j += 1

#打印9*9口诀表
i = 1
while i < 10 :
    j = 1
    while j < i+1 :
        print( j,'*' , i ,'=' , i*j, end = '  ')
        j += 1
    print()
    i += 1   


# 打印倒三角形
i = 0
while i <5 :
    j = 0
    while j < 5-i:
        print('*', end='')
        j += 1
    print()    
    i += 1

# 获取用户输入的任意数，判断其是否是质数。
num =int( input ( '请输入一个大于1的整数：'))
i = 2
count = 0
while ( i< num ):
    if num % i == 0:
        count += 1        
    i += 1

if count >0 :
    print ('输入的不是质数。')
else:
    print ('输入的是质数。')
    


def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print(list_sum([1,3,5,7,9]))


def fac(n):
    if n<=1 and n>=0:
        return 1
    elif n>1:
        return n*fac(n-1)
    else:
        print('n必须大于0')
        return 

print(fac(-5))

'''




    
    
