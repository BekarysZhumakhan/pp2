#1
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False
#2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") #ans:b is not greater than a
#3
print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15
print(bool(x))
print(bool(y)) #ans: All will show the same answer(True).
#4
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) #ans: All will show the same answer(False).In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None.
#5
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #ans: False. because it's return to 0
#6
def myFunction() :
  return True

print(myFunction()) #ans: True.
#7
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") #ans: YES!
#8
x = 200
print(isinstance(x, int)) #ans:True


