# def divisible (a,b,c):
#     if a%b==0 and a%c==0:
#         print("true")
#     else:
#         print("false")
# divisible(-12,2,-6)
# divisible(-12,2,-5)
# divisible(45,1,6)
# divisible(45,5,15)
# divisible(4,1,4)
# divisible(15,-5,3)


a=1234
i=len(str(a))-1
while i>=0:
    rev=a//(10**i)
    sum=rev*(10**i)
    a%=(10**i)
    print(sum,'+',end="")
    i=i-1

