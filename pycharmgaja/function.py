#글로벌 변수 선언
global arr
arr=[1,2,3,4,5]



def arrTest2():
    #다른 함수에 있는 변수는 가져다 쓰지 못함
    print(arr)

    return

arrTest2()


