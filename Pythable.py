
def menu():
    print("------------------------\n Welcome to Pythable!\n Select an option below----------------------------------------------")
    print(" 1 - Division")
    print(" 2 - Multiplication")

menu()

while True:
    response = input()
    if response.strip() in "1234":
        break
  


if response.strip() == "1":   
       clr = input
n = input('Numerator: ')
d = input('Denominator: ') 
ans = int(n)/int(d)  
print(ans)

clr()



if response.strip() == "2":
        m1 = input('Multiplier: ')
m2 = input('Multiplier: ')
clr()
ans2 = int(m1)*int(m2)

print(ans2)