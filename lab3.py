#function_1
#4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes
#example
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(numbers)
print(prime_numbers)
#ans:[2, 3, 5, 7]
#5
def permutations(smth):
    n = len(smth)
    for i in range(n):
        for j in range(n):
            print(smth[(j-i)], end=" ")
        print()
k = str(input())
permutations(k)
#6
def reversing(s):
    rev=' '.join(reversed(s.split())) #split for every word
    return rev
s=input()
reversed_s=reversing(s)
print(reversed_s)
#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
s = input()
nums = list(map(int, s.split()))
print(has_33(nums))
#8
def order007(n):
    result = []
    for i in n:
        if i==0 or i==7:
            result.append(i)
    flag =  False
    for i in range(len(result)-2):
        if result[i]==result[i+1] and result[i]==0 and result[i+2]==7:
            flag = True
    if flag:
        print("True")
    else:
        print("False")
order007([1,2,4,0,0,5,7])
order007([1,0,2,4,0,5,7])
order007([1,7,2,0,4,5,0])
#9
def volume(r):
    V=(4*3.14*(r**3))/3
    return V
r=float(input())
print(volume(r))
#10
def unique(mylist):
    result = []
    for i in mylist:
        if mylist.count(i) == 1:#count is cheking repaets
            result.append(i)
    return result
n = int(input())
mylist = []
for i in range(n):
    number = int(input())
    mylist.append(number)
print(unique(mylist))
#11
def palindrom(s):
    if s==''.join(reversed(s)):
        print("yes")
    else:
        print("no")
s = input()
palindrom(s)
#12
def histogram(arr):
    for i in arr:
        print("*"*i)
n=input()
mylist=list(map(int,n.split()))
histogram(mylist)
#13
import random
from random import randint
def guessanumber():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = randint(1,20)
    sum = 0
    run = True
    while run:
        guess = int(input("Take a guess: "))
        sum+=1
        if guess == number:
            run = False
            print(f"Good job, {name}! You guessed my number in {sum} guesses!")
            break
        if guess>number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low")
guessanumber()
#classes
#5
class Bank():
    def __init__(self, account, money):
        self.money = money
        self.account = account
    def balance(self):
        return self.money
    def owner(self):
        return self.account   
    def deposit(self, money):
        self.money+=money
        return f"You are deposit {money} money"
    def withdraw(self, money):
        if self.money - money < 0:
            return "there is no money(you're beoke ;( )"
        else:
            self.money-=money
            return f"your balance:{self.money},and you take {money}"  
bank = Bank("marik", 1000000)
print(bank.balance())
print(bank.owner())
print(bank.deposit(1000000))
print(bank.withdraw(10000000))
print(bank.withdraw(150000))
#6
class pr:
    def __init__(self, numbers):
        self.numbers = numbers
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    def filterprimenumbers(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))
n = int(input())
mylist = []
for i in range(n):
    number = int(input())
    mylist.append(number)
prime_filter = pr(mylist)
print(prime_filter.filterprimenumbers())