# set_dinner라는 이름의 집합을 만든다 그리고 set_dinner집합에서 또다른 집합인 set([food])을빼서 차집합을 만든다

set_dinner = set(["된장찌개", "피자", "제육볶음", "짜장면"])
food = "짜장면"
set_dinner = set_dinner - set([food])
print(set_dinner)