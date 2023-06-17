# 방법 1
print("나는 %d살입니다." % 20)  # 'd'는 정수값만
print("나는 %s을 좋아해요." % "파이썬")  # 's'는 문자열
print("나는 %s살입니다." % 20)  # 's'는 정수값도 가능
print("Apple은 %c로 시작해요." % "A")  # 'c'는 캐릭터하서 한 글자만 받음

print("나는 %s색과 %s색을 좋아해요." % ("빨간", "파란"))  # 괄호를 통해 두 개의 값도 가능


# 방법 2
print("나는 {}살 입니다." .format(24))
print("나는 {}색과 {}색을 좋아해요." .format("빨간", "파란"))
print("나는 {1}색과 {0}색을 좋아해요." .format("빨간", "파란"))  # {}안에 순서 지정가능


# 방법 3
print("나는 {age}살이고 {color}색을 좋아해요." .format(age=24, color="빨간"))  # 변수로 가능

# 방법 4
age = 24
color = "빨간"
print(f"나는 {age}살이고 {color}색을 좋아해요.")
