#from flask import Flask, render_template, jsonify

dic={'a':'b'}
arr=['a','b']

#배열 arr출력
print(arr)
#
print(dic)

print(arr[1])

#arr항목에 3이라는 숫자를 추가하고자 한다.
arr.append(3)

print(arr)

print(dic['a'])

#abc라는 변수 만들고  a라는 값 넣기
abc='a'

#변수로 dic만들기
dic={abc:'b'}

print('호출')
print(dic)

#print(key:value)
#어떤 변수를 가지고 있을때 arr.append라고 했고 append에 추가할 값을 넣었다. 이 .이라는 것은 ㅇㅇ가 가지고 있는 내장함수라는 의미이다.
#지우는 함수도 있고 수정하는 함수도 있다. arr이라는 특성에 append가 들어가 있다고 생각하면 된다. ex)1~10이라는 숫자를 돌리는 함수 이름을
#sum이라고 하면 sumb.b

#python 3.7 docs찾기
#language reference & library reference
#key값 가져오기
dic.keys()

#value값 가져오기

dic['b']='bbbb'

print(dic)
dic['b']='cccc'

print(dic)


#dic에 새로운 item3값 cccccc추가해주기
dic.update({'item3':'ccccccccc'})

print(dic)
dic.update({'ddddd':'fdasfdsaf'})

print(dic)



