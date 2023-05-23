import csv
import json
from PIL import Image
# 텍스트 파일 읽고 쓰기
# w 써넣고
# r 읽어들이기
# a 추가 써넣기
with open('message.txt', 'w', encoding='utf-8') as file:
    file.write('Hellow\n')
    file.write('Nice to meet you\n')

with open('message.txt', 'r', encoding='utf-8') as file:
    print(file.read())

# 많이 사용하는 형식의 파일을 읽고 쓴다
# open 함수의 키워드 인수 newline에 '' 빈 문자열을 지정한 것은 줄바꿈의 출력을 억제하는 효과가 있습니다.
# csv 모듈을 사용하는 경우 newline을 지정하지 않으면 줄바꿈이 여분으로 출력되어 각 행의 사이에 빈 행이 들어가 버리므로 아래와 같이 작성
# with ooen(파일명, 'w', encoding='utf-8', newline='') as file:
#   csv.writer(파일).writerows(이터러블)
# 변수 = csv.writer(파일)
# 변수.writerrow(이터러블)
catalog = [('hat', 2000), ('shirt', 1000), ('socks', 500)] # 리스트 안에 셋
with open('catalog.csv', 'w', encoding='utf-8', newline='') as file:
    csv.writer(file).writerows(catalog)

# csv 파일의 입력
with open('catalog.csv', encoding='utf-8') as file:
    for row in csv.reader(file):
        print(row)

# ㅊㄴㅍ 파일의 내용을 리스트로 저장
with open('catalog.csv', encoding='utf-8') as file:
    print([tuple(x) for x in csv.reader(file)])

# Json 파일 출력
# dump 함수는 열린 파일에 이터러블의 내용을 넣습니다
# indent를 지정하면 들여쓰기나 줄바꿈이 들어가서 가독성이 높아진다
catalog = [
    {'name': 'hat', 'price': 2000},
    {'name': 'shirt', 'price': 1000},
    {'name': 'socks', 'price': 500}]

with open('catalog.json', 'w', encoding='utf-8') as file:
    json.dump(catalog, file, indent=4)

# Json 파일의 입력
# Json 모듈의 load 함수를 이용한다
with open('catalog.json', encoding='utf-8') as file:
    print(json.load(file))

# 이미지 파일의 출력(Pillow)
# 신규로 이미지를 작성하려면 다음과 같은 new 함수
# new 함수는 image 클래스의 객체를 반환합니다
# 이미지 = Image.new(모드, (폭, 높이), 배경색)
# 이미지 = Image.new('RGB', (폭, 높이), (R 성분, G 성분, B 성분))
# 이미지.save(파일명)
image = Image.new('RGB', (640, 480), (255, 255, 0))
image.save('yellow.png')
W, H = 640, 480
image = Image.new('RGB', (W, H), (0, 0, 0))
for x in range(W):
    for y in range(H):
        r = int(x*255/W)
        g = int(y*255/H)
        b = int(((W+H)-(x+y))*255//(W+H))
        image.putpixel((x, y), (r, g, b))
image.save('gradatiom.png')

# 이미지 파일의 입력
image = Image.open('gradatiom.png')
print(image.format, image.width, image.height) # 형식을 문자열로 가져오기, 폭, 높이

# 다른형식으로 바꿔저장하기
image = Image.open('gradation.png')
image.save('gradation.jpg')