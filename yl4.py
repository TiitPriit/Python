num1=int(input("Esimene number:"))
num2=int(input("Teine number: "))
if(num1<num2):
    print("{} On väiksem".format(num1))
elif(num2<num1):
    print("{} On väiksem".format(num2))
else:
    print("{} ja {} on võrdsed".format(num1,num2))