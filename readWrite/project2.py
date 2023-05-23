import glob
import shutil
import os
import sys
# glob 사용하면 저장한 디렉터리에 있는 파일의 목록을 가져온다
# glob.glob(경로)
# glob.glob(경로, recursive=True) 서브 디렉토리도 처리

for x in glob.glob('readWrite/data/*'):
    print(x)

total = 0  # 합계 0 
for x in glob.glob('readWrite/data/catalog.*'): # 파일 목록 가져오기
    with open(x, encoding='utf-8') as file:  # 각 파일을 열기
        s = file.read()  # 파일 읽어 들이기
        n = s.count('\n')+1 if len(s) else 0 # 행 수 계산기
        print(f'{x:15}{n:5}') # 행 수 표시
        total += n # 행 수 합계에 더하기

print('-'*20) # 경계선
print(f'{"Total":15}{total:5}')    # 합계

# 파일의 복사, 이름의 변경, 삭제
# shutil.copy(복사 원분, 복사 대상) 복사
# shutil.move(이동 원본, 이동 대상) 이동
# os.rename(이전 이름, 새로운 이름) 이름 변경
# os.remove(경로) 삭제
# os.chmod(경로, 모드) 모드의 설정
# os.mkdir(경로) 디렉터리 작성
# os.rmdir(경로) 기렉터리 삭제
# os.makedirs(경로) 재귀적으로 디렉터리 작성
# os.removedirs(경로) 재귀적으로 삭제

shutil.copy('readWrite/data/message.txt', 'message2.txt')
os.rename('message2.txt', 'message3.txt')
os.remove('message3.txt')

# 명령 행 인수 가져오기
# 프롬프느나 터미ㅓㄹ에서 명령어를 입력할 때 명령어에 대해서 주는 인수를 말한다.
# 명령어 인수 ....

# 파이썬의 프로그램명과 인수
# 프로그램명과 인수의 리스트를 가져오기
# sys.argv
# 지정한 위치의 프로그램명 혹은 인수를 가져오기
# sys.argv[인덱스]
# 프로그램명과 인수를 통합한 개수를 가져오기
print(sys.argv)