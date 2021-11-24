# <카카오톡 메시지 예약 전송 프로그램>
# (순서) 사전 설정 → 전송할 내용 입력 → 카운트다운 설정 → 필터링 → 메시지 전송
# 필터링 방식 : 친구 아이콘c누르기 → Ctrl + F → 키워드 검색(키워드가 없을 시 esc)
# 추가로 요구 : 최대 메시지 전송 가능 횟수 무제한-화의 김성근 감동님 사랑해 ㅖㅖㅖㅖㅖㅖ
# -----------------------------------------------------------------
from time import sleep as s                                         # '카운트다운'에 사용됨
import pyperclip                                                    # '사용자 정의 메시지 복사'에 사용됨
import pyautogui                                                    # '키보드 입력 동작'에 사용됨
import random                                                       # '봇 차단 회피 기능'에 사용됨
import sys                                                          # '프로그램 강제 종료'에 사용됨
import mouse                                                        # '마우스 클릭 인식'에 사용됨
# -----------------------------------------------------------------
def pre_configuration() : 
    print('='*30)
    print('\n   <메시지 전송 프로그램>\n')
    print('='*30)
    
    s(1.3)
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


def construct() : 
    global message                                                  # 전송할 메시지
    global filter_starting                                          # '전송 대상이 위에서 몇 번째부터인가?'
    global person_number                                            # 메시지 전송 대상의 명 수
    global keyword                                                  # 검색 키워드

    message = input('\n[system] 전송할 메시지 : ')
    filter_starting = int(input('\n         필터링 대상 시작 지점(숫자) : '))
    person_number = int(input('\n         전송 대상 명 수(숫자) : '))
    keyword = input('\n         검색 키워드(없을 시 Enter로 넘어가기) : ')


def more_construct() : 
    global more_playing_number
    more_playing_number = 0
    more_playing_number = int(input('\n[system] 추가 메시지를 몇 회 작성하시겠습니까?(숫자) ........ '))

    global more_message
    global more_filter_starting
    global more_person_number
    global more_keyword
    more_message = []
    more_filter_starting = []
    more_person_number = []
    more_keyword = []

    for i in range(more_playing_number) : 
        temporary_message = input('\n[system] 전송할 메시지 : ')
        temporary_filter_starting = int(input('\n         필터링 대상 시작 지점(숫자) : '))
        temporary_person_number = int(input('\n         전송 대상 명 수(숫자) : '))
        temporary_keyword = input('\n         검색 키워드(없을 시 Enter로 넘어가기) : ')

        more_message.append(temporary_message)
        more_filter_starting.append(temporary_filter_starting)
        more_person_number.append(temporary_person_number)
        more_keyword.append(temporary_keyword)


def filtering() : 
    pyautogui.click(x, y)
    pyautogui.hotkey('Ctrl', 'f')
    if keyword == '' : 
        pyautogui.press('esc')
    else : 
        pyperclip.copy(keyword)
        pyautogui.hotkey('Ctrl', 'v')
    for i in range(filter_starting - 1) : 
        pyautogui.press('down')


def more_filtering() : 
    pyautogui.click(x, y)
    pyautogui.hotkey('Shift', 'Home')
    pyautogui.press('Delete')
    if keyword == '' : 
        pyautogui.press('esc')
    else : 
        pyperclip.copy(more_keyword[more_playing_number - 1])
        pyautogui.hotkey('Ctrl', 'v')
    for i in range(more_filter_starting[more_playing_number - 1] - 1) : 
        pyautogui.press('down')
        

def send_message() : 
    for i in range(person_number) : 
        latency = random.uniform(1, 3)                              # 카톡 측에서 프로그램을 돌리는 중인지 알 수 없도록 랜덤한 시간 차 발생(1초 ~ 3초)
        s(latency)
        pyautogui.press('enter')
        pyperclip.copy(message)                                     # 사용자가 입력하고자 하는 message를 클립보드에 복사
        pyautogui.hotkey('Ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.press('esc')
        pyautogui.press('down')
    print('\n[system] 전송이 완료되었습니다.')


def more_send_message() : 
    for i in range(more_person_number[more_playing_number - 1]) : 
        latency = random.uniform(1, 3)                              # 카톡 측에서 프로그램을 돌리는 중인지 알 수 없도록 랜덤한 시간 차 발생(1초 ~ 3초)
        s(latency)
        pyautogui.press('enter')
        pyperclip.copy(more_message[more_playing_number - 1])                                     # 사용자가 입력하고자 하는 message를 클립보드에 복사
        pyautogui.hotkey('Ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.press('esc')
        pyautogui.press('down')
    print('\n[system] 전송이 완료되었습니다.')


def replay() : 
    while True : 
        more = int(input('\n[system] 추가 메시지를 작성하시겠습니까? ........ 1 - 추가 메시지를 작성한다 / 2 - 메시지 작성을 그만둔다 '))
        if more == 1 : 
            s(0.5)
            print('[system] 메시지를 추가로 작성합니다')
            more_construct()
            break

        elif more == 2 : 
            s(0.5)
            print('[system] 카운트다운 과정으로 넘어갑니다')
            break

        else : 
            s(0.5)
            print('<오류코드_518> 잘못된 입력입니다. 다시 입력해주세요')
            continue


def counting() : 
    time = int(input('\n[system] 전송 카운트다운을 몇 초로 설정하시겠습니까? ........ '))
    print('\n')
    countdown(time)
    print('\n[system] 카운트다운이 종료되었으므로 메시지를 전송합니다.')


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
    construct()
    replay()
    counting()
    filtering()
    send_message()
    for i in range(more_playing_number) : 
        more_filtering()
        more_send_message()