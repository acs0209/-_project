# 반복문이 돌면서 계속해서 입력을 받는다 추가메뉴관련해서 입력을 하고 그거를 lunch리스트에 넣는다
lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
while True:
    item = input("음식을 추가 해주세요 : ")
    lunch.append(item)
    print(lunch)