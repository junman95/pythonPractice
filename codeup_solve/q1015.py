x = float(input("실수를 입력해 주세요 : "))

print("-" * 70)
print("입력값 = " ,'%0.2f' %x ,"\n" + "입력 타입 = " , type(x)) 

'''
실수 소숫점 자리제한
'%0.nf' %실수
n은 제한하려는 자릿수
'''