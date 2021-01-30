#1020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기

num = list(input("주민등록 번호를 입력해 주세요 : "))

for i in num:
    if i == "-":
        print(i)
print(num)
