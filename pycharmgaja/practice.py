text=['1','2','a','b','c']

def funcTest(x):
    for i in text:
        print(i)
        if (i == 'a'):
            return x


v=funcTest('a')

#text변수를 for문으로 돌리기

