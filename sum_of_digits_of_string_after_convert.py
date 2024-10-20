def sum_of_digits(num):
    sum=0
    n=num
    while(n!=0):
        r=n%10
        n=n//10
        sum+=r
    num=sum
    return num
    
string=input("Enter your string: ")
str_transform=''
k=int(input("Enter your k: "))
for i in string:
    # print(i)
    d=ord(i)-96
    str_transform+=str(d)
print(str_transform)
int_str=int(str_transform)

for j in range(k):
    int_str=sum_of_digits(int_str)
    print(int_str)
    if(int_str<10):
        break
