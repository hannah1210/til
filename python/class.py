class Person:
    name='사람의 고유한 속성'
    age ='출생 이후부터 삶을 마감할 때까지의 기간'

    def greeting(self):
        print(f'{self.name}이 인사입니다. 안녕하세요.')

    def eating(self):
        print(f'{self.name}은 밥을 먹고 있습니다.')

    def aging(self):
        print(f'{self.name}은 현재 {self.age}살이고, 현재 나이를 먹어가는 중입니다.')


hannah=Person()
print(hannah.name)
print(hannah.age)
hannah.name = 'hannah'
hannah.age = 19
print(hannah.name)
print(hannah.age)
hannah.greeting()
hannah.eating()
hannah.aging()