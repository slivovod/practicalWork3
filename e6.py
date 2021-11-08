num = int(input())
if(num < 0):
    print("error :(")
elif(num == 0):
    print("0")
else:
    ff = 1
    while num > 1:
        ff *= num
        num -= 1

print(ff)