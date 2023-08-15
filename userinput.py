"""#odds except divissables by 3
lis=[]
for n in range(1,21):
    if n % 2 == 0:
        continue
    elif n % 3 !=0:
        lis.append(n)
print(lis)"""

"""print('input password if it matches mine you win')
user_input = input("input password")
my_passwd = 'abrakadabra'

while user_input != my_passwd:
    test = 0
    if user_input == my_passwd:
        print("you win!")
    elif user_input!= my_passwd:
        test+=1
        print("incorrect, guess again")

    elif test == 3:
        print("out of guesses")
        break ???"""


"""i=0
while i<=10:
    if i ==5:
        i+=1
        break
    print(i)
    i +=1"""


"""list1=[1,2,3,4,5]
list2=[3,4,5,6,7]

result = []
for n in list1:
    if n in list2:
        result.append(n)
print(result)"""

"""def removeSpaces(string):
    list = []
    for i in range(len(string)):
        if string[i] != ' ':
            list.append(string[i])
    return string(list)
def string(List):
    return ''.join(List)
string = " and theyll tell you black is really" \
         " white the moon is just the sun at night" \
         " and when you walk the golden halls" \
         " youll get to keep the gold that falls "
print (removeSpaces(string))"""

"""fib = [0,1]
for i in range(2,11):
    next = fib[i-1]+fib[i-2]  
    fib.append(next)
print(fib)"""

"""for i in range (1,101):
    if i % 5 == 0:
        print(i)"""

"""num = 7
for i in range(1,11):
    print(num,"X",i,"=",num*i)"""

"""num = 5
fac = 1
i = 1
while i <= num:
    fac = fac * i
    i += 1
print(fac)"""

"""print("enter mark obtained: ")
mark=int(input())

if mark>=80:
    print("your grade is A")
elif mark<80 and mark>60:
    print("your grade is B")
elif mark < 60 and mark > 40:
    print(" your grade is C")
elif mark < 40:
    print("your grade is D")"""

"""print("input a,b,c and ill solve a quadratic equation for those numbers")
a = float(input("input a: "))
b = float(input("input b: "))
c = float(input("input c: "))

import math

dis = (b*b) - (4*a*c)
sqrt_val = math.sqrt(abs(dis))

if a == 0:
    print("a cant be 0")

elif dis>0:
    print((-b+sqrt_val)/(2*a))
    print((-b-sqrt_val) / (2 * a))

elif dis == 0:
    print(-b/(2*a))

else:
    print("doesnt have a real solution")"""


"""vcount = 0;
ccount = 0;
str = "Peter piper picked a pack of pickled peppers";

str = str.lower();
for i in range(0, len(str)):
    if str[i] in ('a', "e", "i", "o", "u"):
        vcount = vcount + 1;
    elif (str[i] >= 'a' and str[i] <= 'z'):
        ccount = ccount + 1;
print("Total number of vowel and consonant are");
print(vcount);
print(ccount);"""


"""def sieveoferatosthenes(num):
    prime = [True for i in range(num + 1)]
    n = 2
    while (n * n <= num):
        if (prime[n] == True):
            for i in range(n * n, num + 1,n):
                prime[i] = False
        n += 1
    for n in range(2, num + 1):
        if prime[n]:
            print(n)
num=100
sieveoferatosthenes(num)"""

"""squares = []
for i in range(1,11):
    res = (2**i)
    squares.append(res)
print(squares)"""

"""nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for i in range(1,11):
    res = (i**2)
    squares.append(res)

list1 = list(zip(nums, squares))
print(list1)"""
# arajin@ chisht dzev@ glxi ch@nka 