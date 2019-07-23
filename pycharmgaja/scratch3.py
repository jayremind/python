#함수 설정하기
def func1(x):
    #탭으로 들여쓰기 된 이부분이 함수의 영역이다.
    x=x+1;
    print('is func')
    #위의 공식에 대한 결과를 표시해주는 것 ==return
    return x

func1(2)

res=func1(2)

print(res)