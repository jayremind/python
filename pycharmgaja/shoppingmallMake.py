from flask import Flask, request, render_template, jsonify

#app이라는 구문으로 Flask할당
app=Flask(__name__)

articles=[]

#HTML넣기
@app.route('/')

def home():
    return 'This is ShoppingMall'

@app.route('/shoppingmallpage')
def shoppingpage():
    return render_template('w12_paircoding.html')

#본격적인 api넣기

@app.route('/post',methods=['POST'])
def post():
    global articles               #글로벌 변수 articles가 설정된다.

    #url_get = request.form['url_give']      #w12_paircoding.html로부터 url받기
    # comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분
    # url_name = request.form['name_give']
    user_address = request.form['address_receive']
    user_name = request.form['name_give']
    user_amount = request.form['amount_receive']
    phone_number = request.form['number_give']
    user_gender = request.form['gender_receive']

    #article={'url':url_get,'comment':comment_receive,'name':url_name, 'number':phone_number}  #위로부터 받은 url과 comment를 dictionary로 만들어주고
    #이름,수량,주소,전화번호
    article={'name':user_name,'amount':user_amount,'address':user_address,'phone':phone_number,'gender':user_gender}
    articles.append(article)

    return jsonify({'result': 'success'})

@app.route('/post', methods=['GET'])
def view():
    global articles            # 이 함수 안에서 나오는 articles 글로벌 변수를 가리킵니다.
    return jsonify({'result':'success', 'articles':articles})

if __name__=='__main__':
    app.run('0.0.0.0',port=5000,debug=True)

#지금까진 어떤 함수를 사용해도 끊는다는 메시지가 나왔지만 지금은 아니다. Flask라는 애는 한번 실행하면 우리가 직접 끄지 않는한 죽지 않는다.
