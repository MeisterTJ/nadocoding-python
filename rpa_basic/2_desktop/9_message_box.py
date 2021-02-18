# 메시지 박스
import pyautogui
# pyautogui.countdown(3)  # 카운트 다운을 한다. 3 2 1
# print("자동화 시작")

# pyautogui.alert("자동화 수행에 실패하였습니다.", "경고")       # 확인 버튼만 있는 팝업
result = pyautogui.confirm("계속 진행하시겠습니까?", "타이틀")   # 확인, 취소 버튼
print(result)       # OK, Cancel
result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력")        # 사용자 입력
print(result)
result = pyautogui.password("암호를 입력하세요")
print(result)