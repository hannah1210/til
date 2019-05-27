#String Interporation

a='123'
new_a = f'{a}'

#1. 옛날 방식
#'%s %s '% ('one', 'two')

#2. pyformat
#'{} {}'.format('one','two')
name = '홍길동'
eng_name= "Hong"
print("안녕하세요. {}입니다. My name is {}".format(name, eng_name))
#3. f-string
#a, b= "one","two"
#f'{a} {b}'
name="홍길동"
print(f'안녕하세요. {name}입니다.')