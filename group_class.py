#This is the amount of students each class have
class1 = 32
class2 = 45
class3 = 51

#This calculate how many groups can be made
group1 = class1//5
group2 = class2//7
group3 = class3//6

#This calculate how many leftover students each class
left1 = class1%5
left2 = class2%7
left3 = class3%6

#Shows the output
print('Number of students in each group:')
print('Class 1=',group1)
print('Class 2=',group2)
print('Class 3=',group3)
print('\n')
print('Number of students leftover:')
print('Class 1=',left1)
print('Class 2=',left2)
print('Class 3=',left3)
