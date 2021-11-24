# <카카오톡 메시지 전송 프로그램>
# (순서) 사전 설정 → 전송할 내용 입력 → 카운트다운 설정 → 필터링 → 메시지 전송
# 필터링 방식 : 친구 아이콘 누르기 → Ctrl + F → 키워드 검색(키워드가 없을 시 esc)
# 추가로 요구 : 실제 카카오톡 환경에서의 테스트가 요구됨.
# -----------------------------------------------------------------
from time import sleep as s                                         # '카운트다운'에 사용됨
import pyperclip                                                    # '사용자 정의 메시지 복사'에 사용됨
import pyautogui                                                    # '키보드 입력 동작'에 사용됨
import random                                                       # '봇 차단 회피 기능'에 사용됨
import sys                                                          # '프로그램 강제 종료'에 사용됨
import mouse                                                        # '마우스 클릭 인식'에 사용됨
# -----------------------------------------------------------------
def initialize() : 
    global message                                                  # 전송할 메시지
    global filter_starting                                          # '전송 대상이 위에서 몇 번째부터인가?'
    global person_number                                            # 메시지 전송 대상의 명 수
    global keyword                                                  # 검색 키워드

    message = input('\n[system] 전송할 메시지 : ')
    filter_starting = int(input('\n[system] 필터링 대상 시작 지점(숫자) : '))
    person_number = int(input('\n[system] 전송 대상 명 수(숫자) : '))
    keyword = input('\n[system] 검색 키워드(없을 시 Enter로 넘어가기) : ')

    time = int(input('\n[system] 전송 카운트다운을 몇 초로 설정하시겠습니까? '))
    print('\n')
    countdown(time)
    print('\n[system] 카운트다운이 종료되었으므로 메시지를 전송합니다.')


def filtering() : 
    pyautogui.click(x, y)
    pyautogui.hotkey('Ctrl', 'f')
    if keyword == '' : 
        pyautogui.keyDown('esc')
    else : 
        pyperclip.copy(keyword)
        pyautogui.hotkey('Ctrl', 'v')
    for i in range(filter_starting - 1) : 
        pyautogui.keyDown('down')


def send_message() : 
    for i in range(person_number) : 
        latency = random.uniform(1, 3)                              # 카톡 측에서 프로그램을 돌리는 중인지 알 수 없도록 랜덤한 시간 차 발생(1초 ~ 3초)
        s(latency)
        pyautogui.keyDown('enter')
        pyperclip.copy(message)                                     # 사용자가 입력하고자 하는 message를 클립보드에 복사
        pyautogui.hotkey('Ctrl', 'v')
        pyautogui.keyDown('enter')
        pyautogui.keyDown('esc')
        pyautogui.keyDown('down')
    print('\n[system] 전송이 완료되었습니다.')


def pre_configuration() : 
    print('='*30)
    print('\n   <메시지 전송 프로그램>\n')
    print('='*30)
    '''
    print('USER\'S Monitor information : ', pyautogui.size())       # 없어도 되는 부분임
    '''
    s(1.5)
    print('\n[system] 사전 환경설정을 시작합니다.')
    s(1.5)
    print('\n[system] 카카오톡에서 \'친구 아이콘\'을 클릭해주세요.')
    while True : 
        if mouse.is_pressed('left') : 
            global x
            global y
            x, y = pyautogui.position()
            break
    print('\n[system] 사전 환경설정이 완료되었습니다.')


def countdown(t) :
    try : 
        while t :                                                   # 0초가 아니면
            mins = t // 60                                          # 분 = 초 ÷ 60
            secs = t % 60                                           # 초 = 초를 60으로 나누고 나머지
            print('[system] %02d:%02d' %(mins, secs), end = '\r')
            s(1)
            t = t - 1           # 1초 지날 때 마다 1씩 감소
        print('[system] 00:00')
        return

    except KeyboardInterrupt :                                      # 고의적으로 오류를 발생시켜 카운트다운 종료
        print('\n\n[system] 메시지 전송을 취소했습니다.')
        sys.exit()
# -----------------------------------------------------------------
# configuration
pyautogui.PAUSE = 0.5                                               # 모든 키보드 입력 동작 0.5초 딜레이
# -----------------------------------------------------------------
if __name__ == "__main__" : 
    pre_configuration()
    initialize()
    filtering()
    send_message()