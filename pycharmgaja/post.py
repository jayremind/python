from flask import Flask, render_template,request, jsonify

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post-test', methods=['POST'])
def post():
    name = request.form['name']

    return jsonify({'name':name})

@app.route('/post-card',methods=['POST'])
def post2():
    url = request.form['url']

    com= request.form['com']

    dic={'url':url,'com':com}

    return jsonify(dic)


@app.route('/link')
def link():
    return render_template('w1d2_paircoding.html')


if __name__=='__main__':
    #app.웹주소,호텔 방 5000번,debug메시지
    app.run('0.0.0.0',port=5000,debug=True)



