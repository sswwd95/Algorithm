array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --------------------------------------------------

# key기준 기본 정렬 예제
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)
# [('바나나', 2), ('당근', 3), ('사과', 5)]