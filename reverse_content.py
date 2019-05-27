with open ('mulcam.txt', 'r') as f:
    lines = f.readlines()

with open('mulcam.txt', 'w') as f:
    print(len(lines))
    for i in range(len(lines)-1, -1,-1):
        print(lines[i], i)
        f.write(lines[i])

# 2. reverse
# lines.reverse()
# 3. write file
# with open('mulcam.txt','w') as f:
#     f.writelines(lines)