# print("Hello You")
# suiii="sam"
# print(suiii*5)   




# firstname=input("Enter your first name: ")
# print(firstname)
# lastname=input("Enter your last name: ")
# print(lastname)
# age=int(input("Enter your age: "))
# print(age)
# age1=int(input("Enter your age: "))
# print(type(age1))
# print(firstname,lastname,age+age1)



# pro1=int(input("pro1price: "))
# print(pro1)
# pro2=int(input("pro2price: "))
# print(pro2)
# pro3=int(input("pro3price: "))
# print(pro3)
# pro4=int(input("pro4price: "))
# print(pro4)
# totalpro=(pro1,pro2,pro3,pro4)
# avg=(len(totalpro))
# total=(pro1+pro2+pro3+pro4)
# finaltotal=(total/avg)
# print(finaltotal)


# name=input("Enter your name: ")
# print(name)
# startname=name.endswith("n")
# print(startname)

# age=18

# if age>=18:
#     print("you can vote")
# elif age<=18:    
#     print("you can't vote")    


#calculator
# a=int(input("enter the value: "))
# print(a)
# b=int(input("enter the value: "))
# print(b)
# sign=input("enter the sign: ")
# if sign=="+":
#     print(a+b)
# elif sign=="-":
#     print(a-b)
# elif sign=="/":
#     print(a/b)
# elif sign=="*":
#     print(a*b)
# elif sign=="%":
#     print(a%b)


# for i in range(1,20):
#     if i%2==1:
#         print(i)
# a=int(input("Enter the firstnumber: "))
# b=int(input("Enter the secondnumber: "))
# num=0
# for i in range(1,1000):
#     if i%a==0 and i%b==0:
#         print(i)
#         return


# rollnumber={101,104,105,107,105,103}
# print(len(rollnumber),rollnumber)

# idinput=int(input("Enter the id: "))
# employe=[
# (101,"alice",5000),
# (102,"charlie",5000),
# (103,"ronshean",5000)
# ]
# for id in employe:
#     employeid=id[0]
#     if employeid==idinput:
#         print("id found")
#         print("employe id: ",employe[0])
#         print("employe name: ",employe[1])
#         print("employe salary: ",employe[2])
#     found=True
#     return

# if not found:
#     print("id not found")


# from Math import factorial



# def eveorodd(num):
#     if num%2==0:
#         print("even")
#     elif num%2==1:
#         print("odd")

# eveorodd(12)


# vowels="AEIOUaeiou"

# def findvowels(str):
#     count=0
#     for v in (str):
#         if v in vowels:
#             count+=1
#     return count
# print(findvowels("hesarewego"))


def findprime(num):
    if num==1:
        print("num is not a prime number")

    readnum=int(num/2)
    for v in range(2,readnum):
        if num%v==0:
            print("num is not a prime number")
            return
        elif num%v!=0:
            print("num is a prime number")
            return
findprime(1)


