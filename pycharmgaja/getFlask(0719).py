from flask import Flask, request, render_template, jsonify

#app이라는 구문으로 Flask할당
app=Flask(__name__)

#index.html페이지 넣어보기
#route라는 것은 해당 주소로 연결해주는 역할을 하는 통로이다
#@app.route
@app.route('/')

#home이라는 function을 하나 만들어준다.
def home():
    #return render_template('index.html')
    return ('<p>hello</p>')

#새로운 url연결해보기
@app.route('/get-test2',methods=['GET'])
def homeGet():

    print(request.query_string)
    print(request.args)

    name=request.args.get('name')

    print(name)
    return '0'

#if__name__==처럼 if와__name을 붙여서 기입하면 오류가 생긴다.
if __name__=='__main__':
    app.run('0.0.0.0',port=5000,debug=True)

#지금까진 어떤 함수를 사용해도 끊는다는 메시지가 나왔지만 지금은 아니다. Flask라는 애는 한번 실행하면 우리가 직접 끄지 않는한 죽지 않는다.
