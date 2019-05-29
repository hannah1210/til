from flask import Flask
from flask import render_template, request
import random
import requests
app = Flask(__name__)

@app.route('/send')
def send():

    return render_template('send.html')

@app.route('/receive')
def receive():
    # {name: 'hannah', 'message:': 'I'm here'}
    user=request.args.get('user')
    message=request.args.get('message')
    return render_template('receive.html', user=user, message=message)

#[실습] 랜덤 게임(신이 나를 만들 떄)
#1. 데이터와 함께 요청을 보내고,
#2. 데이터를 받아서
#3. 결과를 보여주는 페이지
@app.route('/test1')
def test1():
    return render_template('test1.html')

@app.route('/test2')
def test2():
    user = request.args.get('user')
    r_num=[1,2,3,4]
    num=random.choice(r_num)
    filename='신이{}.PNG'.format(num)
    print(filename)
    return render_template('test2.html', user=user, filename=filename)

@app.route('/lotto_check')
def lotto_check():

    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round= request.args.get('lotto_round')
    input_lotto = [int(request.args.get(f'lotto_num{n}')) for n in range(1, 7)]
    input_lotto.sort()
    url=f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response=requests.get(url)
    lotto=response.json()
    winner=[]   #list()
    # for n in range(1,7):
    #     winner.append(lotto[f'drwtNo{n}'])

    # list comprehension
    a = [lotto[f'drwtNo{n}'] for n in range(1,7)]
    b = lotto['bnusNo']

    # 같은 숫자 갯수
    matched = len(set(a) & set(input_lotto))

    # 같은 숫자 갯수에 따른 등수
    if matched ==6:
        result ="1등입니다."
    elif matched ==5:
        if b in input_lotto:
            result="2등입니다."
        else:
            result= "3등입니다."
    elif matched ==4:
        result="4등입니다."
    elif matched ==3:
        result="5등입니다."
    else :
        result= "꽝입니다."


    winner = f'{a} + {b}'
    return render_template('lotto_result.html', lotto=winner, lotto_round=lotto_round, result=result, my_numbers=input_lotto)


#[실습] 로또 당첨 여부 확인
#1. lotto_check에서 내가 산 로또 번호 입력
#2. lotto_result에서 값 가져와서 변수에 저장
#3. API를 통해서 가져온 특정 회차 로또 번호와 비교
#4. 당첨 결과 메세지를 html에 작성


if __name__ == '__main__':
    app.run(debug=True)