import random

num = random.randint(0, 100)

attempt = 4
msg = ''
while attempt > 0:
   
    user_input = int(input('Sisesta number: '))
    if user_input == num:
        msg = 'See on õige!'
        break
    elif user_input > num:
        print(f'{user_input} On Liiga Suur Paku Väiksem')
        

    elif user_input < num:
        print(f'{user_input} On Liiga Väike Paku Suurem')
        

    else:
        print('Midagi läks valesti!')
        break
    
print(msg)