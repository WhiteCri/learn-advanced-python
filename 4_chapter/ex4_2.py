cafe = bytes('café', encoding='utf_8')
print(cafe)

print(cafe[0]) # since it's one byte, it's range is 0~255
print(cafe[:1]) # it's bytes even we slice it

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:]) #it's bytesarray even we slice it

## when we print byte, there's 3 ways of printing
# 1. 0 ~ ? 까지 출력 가능한 문자는 그대로 출력
# 2. 탭, 개행문자, 캐리지 리턴, 백슬래시는 이스케이프 시퀀스로 출력..\t, \n, \r. \\
# 3. 그 외의 값은 \x00등으로 출