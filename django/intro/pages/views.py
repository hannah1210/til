from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def hola(request):
    return render(request, 'hola.html')

def dinner(request):
    menu = ['족발','치킨','피자','햄버거']
    pick = random.choice(menu)
    return render(request, 'dinner.html', {'pick':pick})

def hello(request, name):
    context={'name':name}
    return render(request, 'hello.html',context)

def introduce(request, name, age):
    context = {'name' : name, 'age': age}
    return render(request, 'introduce.html',context)

# 숫자를 2개 variable routing을 통해 받아 곱셈 결과를 출력
def times(request, num1, num2):
    result= num1 * num2
    context={'num1':num1,'num2':num2,'result':result}
    return render(request, 'times.html', context)

# 반지름(r)을 인자로 받아 원의 넓이를 구하세요.
def circle(request, r):
    cir=r**2 * 3.14
    context={'r':r, 'cir':cir}
    return render(request, 'circle.html',context)

def template_language(request):
    menus = ['짜장면','탕수육','짬뽕','양장피']
    my_sentence = 'Life is short, you need python'
    messages= ['apple','banana','cucumber','mango']
    empty_list=['Hanna','이한나']
    datetimenow = datetime.now()
    context={
        'menus':menus, 'my_sentence' :my_sentence,
        'message':messages, 'empty_list':empty_list,
        'datetimenow':datetimenow
    }
    return render(request, 'template_language.html',context)

def birthday(request):
    if datetime.now().month== 12:
        if datetime.now().day()==10:
            is_bday = True
        else:
            is_bday=False
    else:
        is_bday= False
    context = {
        'is_bday': is_bday
    }
    return render(request, 'birthday.html', context)

def throw(request):
    return render(request,'throw.html')

def catch(request):
    message=request.GET.get('message')
    message2 = request.GET.get('message2')
    context={'message':message, 'message2' : message2}
    return render(request,'catch.html', context)

# lotto /get
# get -> 1~45의 수 중에서 6개의 수를 뽑아 리스트로 만들어 넘긴다
# get -> 사용자로부터 이름을 입력받아 넘긴다
def lotto(request):
    return render(request, 'lotto.html')

def get(request):
    username=request.GET.get('username')
    numbers = range(1,46)
    lotto = random.sample(numbers, 6)

    context = {
        'username': username, 'lotto':sorted(lotto)
    }
    return render(request, 'get.html', context)