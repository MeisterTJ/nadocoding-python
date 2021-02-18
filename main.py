kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

# [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(kor, eng)))  # 리스트 2개를 세로로 합쳐준다.

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

# [('사과', '바나나', '오렌지'), ('apple', 'banana', 'orange')]
print(list(zip(*mixed)))  # 첫번째, 두번째 것들끼리 분리해준다.

kor2, eng2 = zip(*mixed)
print(kor2)     # ('사과', '바나나', '오렌지')
print(eng2)     # ('apple', 'banana', 'orange')
