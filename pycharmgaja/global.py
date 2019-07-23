global arr
arr=[1,2,3,4]
#1.함수 arrTest() 선언하기
def arrTest():

    print(arr)
    return
    #현재 function에서는 받아서 사용하는 값은 없다.

def arrTest2():
    print(arr)
    return
arrTest2()

#다른 함수에 있는 변수는 가져다 쓰지 못한다.
#이럴때는 어디서든 가져다 쓸 수 있는 변수가 필요하다 ->global변수
#만약 func라는 변수 안에다가 a라는 function을 넣어주고 싶으면