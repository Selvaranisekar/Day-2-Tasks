'''you have been given a python list [10,501,23,37,100,999,87,351]
create two list which have all even numbers and another list which will have odd numbers in it'''

#List of numbers

List1=[10,501,23,37,100,999,87,351]

odd_List=[x for x in List1 if x%2==1]
even_List=[x for x in List1 if x%2==0]

#Printing List
print("orginal List:", List1)
print("odd List:", odd_List)
print("even List:", even_List)







