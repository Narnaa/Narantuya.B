#1
#lists = ['python','php','java']
#print(lists[0:3])

#2
#num = [2,5,6,7,311,431,74,230,1354,76]
#c = 0
#for i in num:
#    c = c + i
#    i = i + 1 
#print(c)

#3
#num = [4,34,13,56,95]
#def multiplier(x):
#    c = 1
#   for i in x:
#        c = c * i
#        i = i + 1
#    print(c)
#multiplier(num)

#4
# def multiply():
#    numbers = list(map(int, input('').split(',')))
#    multiplier = numbers[2]*numbers[-1]
#    print(multiplier)    
# multiply()

#5
#def func():
#    numbers = list(map(int, input('').split(',')))
#    x = max(numbers)
#    y = min(numbers)
#    print(x,y)

#6
#list = ['414','444','aba']
#def samedigits(list):
#  k = 0
#  for i in list:
#    if  i[0] == i[-1]:
#      k += 1
#  return k
#print(samedigits(list))


#7
#numbers = list(map(int, input('').split(',')))
#list2 = set(numbers)
#print(list(list2))

#8
# list = []
# def func(list):
#     if len(list) == 0:
#         print('List is empty')  
#     else:
#         print('List is not empty')
# func(list)

#9
# alist = [1,2,6,31,70,8,411,5,900,12]
# del alist[4], alist[6], alist[8]
# print(alist)

#10,11
# numbers = (1,2,3,5,6,7,8,9,10,11)
# y = list(numbers)
# y.append(input())
# numbers = tuple(y)
# print(numbers)

#12
# numbers = (1,2,3,5,6,7,8,9,10,11)
# print(numbers[1],numbers[-2])

# 13
# y = input()
# countries = ('Mongolia','Albania','Andorra',y)
# if y in countries:
#     print('Yes')


#14
# numbers = (1,2,3,5,6,7,8,9,10,11)
# k = 0
# for i in numbers:
#     print(i)
#     i += 1

#15 
# laugh = {'zuv','xaxa','tiin'}
# laugh2 = {'kk','za'}
# nlaugh = laugh.union(laugh2)
# print(nlaugh)

#16
# laugh = {'zuv','xaxa','tiin'}
# laugh2 = {'za','tiin', 'kk'}
# nlaugh = laugh.intersection(laugh2)
# print(nlaugh)

#17
# laugh = {'zuv','xaxa','tiin'}
# length = len(laugh)

#18
# x = input()
# laugh = {'zuv','xaxa',y,'tiin'}
# print(laugh)
# laugh.remove(y)
# print(laugh)

#19
# laugh = {'zuv','xaxa','tiin'}
# laugh.clear()


#20
#laugh = {'zuv','xaxa','tiin'}
#del laugh

#21
# from audioop import reverse
# import operator
# num = {2002: 205, 2022: 404, 2011: 808}
# print(sorted(num.items(),key=operator.itemgetter(1)))


#22
# num = {'2002': '205','2022': '404', '2011': '808'}
# if '2002' in num:
#     print('Yes')
# else:
#     print('No')

#23
# num = {'2002': '205','2022': '404', '2011': '808'}
# if '205' in num.values():
#     print('Yes')
# else:
#     print('No')

#24
# num = {'2002': '205','2022': '404', '2011': '808'}
# for i,k in num.items():
#     print(i,k)

#25
# num = {'2002': '205','2022': '404', '2011': '808'}
# names = {'key1':'Andorra','key2':'Mongolia'}
# num.update(names)
# for i,k in num.items():
#      print(i,k)

#26
# num = {'2002': '205','2022': '404', '2011': '808'}
# print(sum(num.values()))
