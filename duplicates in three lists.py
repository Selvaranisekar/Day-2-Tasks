'''you have been given three lists , your task is to find the duplicates in the three lists .
Write a python program for the same'''


def find_common(list1,list2,list3):
    common=set()
    for ele in list1:
        if ele in list2 and ele in list3:
            common.add(ele)
    return common

list1=[20,30,40,50,60,70,80]
list2=[10,30,40,50,60,70,80]
list3=[90,30,40,50,60,70,80]

common=find_common(list1,list2,list3)
print(common)
