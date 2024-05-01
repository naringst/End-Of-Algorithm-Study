s="1111111"
zeroCnt = 0

def solution(s):
    cnt = 0
    while True:
        s = binary(s)
        cnt+=1
        if s == "1":
            break
    return [cnt, zeroCnt]

def binary(s):
    global zeroCnt
    removeZero = 0
    old_len=len(s)
    s= s.replace("0", "")
    new_len=len(s)
    removeZero += old_len - new_len
    zeroCnt += removeZero
    new_num = ""
    s= new_len
    while True:
        if s==1:
            new_num+="1"
            break
        new_num+=str(s % 2)
        s=s//2
    return new_num[::-1]

print(solution(s))