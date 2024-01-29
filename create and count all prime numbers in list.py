'''you have been given a python list [10,501,23,37,100,999,87,351]
your task is to count all the prime numbers
and crate new python list which will contain all the prime numbers in it'''

list=[10,501,23,37,100,999,87,351]

prime=[]
for i in list:
    c=0
    for j in range(1,i):
        if i %j ==0:
            c+=1
    if c==1:
        prime.append(i)

'''Printing Prime numbers'''

print("Total prime numbers in given list:", len(prime))
print("Prime numbers are:", prime)

