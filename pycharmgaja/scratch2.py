#반복문 적용

arr1=[100,'aaa',3,4,5,[1,2,3],{'a':1}]

dic={'arr':[1,2,3],'dic':{'hi':'bye'}}

#arr1에 있는 5개의 항목의 갯수만큼 숫자를 돌려준다.
for i in arr1:
    print(i)
    #arr1에 있는 값들을 출력하는데 3이 나올 경우 end라는 글자를 출력하면서 멈추기
    if(i==3):
        print('end')
        break

for k in dic:
    print(k)
