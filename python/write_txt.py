# Write File

# 1.open()
f=open('mulcam.txt','w')
for i in range (10):
    f.write(f"Hello, mulcam {i}\n")
f.close()

# 2. with open()
with open('mulcam.txt','w') as f:
    f.write('Hello,Mulcam!\n')

# with : Context Manager

# 2-1: writelines
with open('mulcam.txt','w') as f:
    f.writelines(['1\n','2\n','3\n'])

# \로 시작하는 문자 -> 이스케이프 시뭔스(문자)
# \n: 개행 문자
# \t : tab 문자
# \\ : 역슬래쉬 문자
# \' : 따음표 문자
# \" : 쌍따음표 문자


