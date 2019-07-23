arr1=[1,2,3,4,5]

print(arr1)
#파일 실행시킬때는 run을 클릭한다.
#arr1=[1,2,3,4,5,,]의 경우 syntax error가 발생한다.

#------dic -> 딕셔너리

dic={'a':1,'b':2,'hello':'안녕'}

print(dic)
#arr1의 배열의 4번째 값 호출 // 모든 공간값은 0번부터 시작된다.
print(arr1[3])

#print(dic[1])의 경우 KeyError가 발생한다.

a='a'
b='b'
print(dic[a])
print(dic[b])
print(dic['a'])
print(dic['b'])
print(dic['hello'])

#조건문 - boolean

a=4
if(a!=3):
    #write code here
    #이렇게 탭 한칸 들여쓰기 한 구간내에서 if에 걸려 있는 조건문의 내용이 적용된다.
    print('is True')
else:
    print('is False')

