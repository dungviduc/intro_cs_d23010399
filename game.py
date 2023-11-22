from random import randint
def game1():
    a = 6
    while True :
        n = int(input("nhập vào 1 số :"))
        if n==a:
            print("chính xác")
        else:
            print("mời nhập lại")
            
def game2() :
    a=randint(1,10)
    while True :
        n= int(input("nhập 1 số từ 1 đến 10 :"))
        if n==a : print("chính xác")
        else : print("mời nhập lại")

def game3() :
    a=randint(1,10)
    while True :
        n=int(input("nhập số từ 1 đến 10:"))
        if n==a: 
            print("đúng")
        elif n>a : print("lớn hơn số bí mật")
        elif n<a : print("nhỏ hơn số bí mật")