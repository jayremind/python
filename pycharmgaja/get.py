#http://_________________/promo?key=value&

from flask import Flask, render_template,request, jsonify

#app이라는 구문으로flask 할당

app=Flask(__name__)

#@은 꾸며주는 역할
#decorator
#route - 주소 이동하는 역할을 한다.
#@app.route('/promo')



#     return reder_template(" ")
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/link')
def link():
    return render_template('w1d2_paircoding.html')

@app.route('/get-card')
#card-list를 글로벌 변수로 만들어준다.
def get2():
    cardList={"card":"card1","card2":"card132","card3":"card4314"}

    return jsonify(cardList)
#json화를 안해주면 error생김


#get으로만 통신하는 함수
#get으로 queryString을 받아올 차례
@app.route('/get-test', methods=['GET'])
def get():
    print(request.query_string)
    print(request.args)

    name=request.args.get('name')
    print(name)

    #return에 아무것도 주지 않으면 내용이 뜨지 않는다.
    return jsonify({'name':name})

if __name__=='__main__':
    #app.웹주소,호텔 방 5000번,debug메시지
    app.run('0.0.0.0',port=5000,debug=True)
