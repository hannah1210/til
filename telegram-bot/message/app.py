from flask import Flask, render_template, request
import requests
import random
app = Flask(__name__)

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    token = "818657551:AAHNzRo7jswR-rD4YM-9OZ_SMys1lIJf3sE"
    api_url = f'https://api.telegram.org/bot{token}'
    chat_id = "596510462"  # 본인 telegram 계정 id
    # text='안녕하세요'
    # text= input('메시지를 입력하세요')
    #text = random.sample(range(1, 46), 6)
    text = request.args.get('message')
    requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')
    return '전송 완료'

if __name__=='__main__':
    app.run(debug=True)