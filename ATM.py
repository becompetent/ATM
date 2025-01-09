# 기본금액 : balance(변수명)
# 기본 금액 변수에 3000원을 넣어주세요 --> 값을 넣어주세요
# while문을 이용해서 입금, 출금, 영수증 보기, 종료라는 기능이 종료라는 버튼을 누르기 전까지 계속해서 노출되도록 만들어주세요
# 종료를 누르면 서비스를 종료한다는 메세지를 출력하고 현재 잔액을 보여주세요

# 입금한 금액을 받는 변수 : deposit_amount
# 입금된 금액은 balance 변수에 추가되도록 코드를 작성해주세요
# 영수증에 다음 순서로 값이 들어가도록 코드를 만들어 주세요 -> "입금", 입금요청액, 총액 순으로 데이터 넣어주세요
#단, 영수증에 내역은 변경되지 않아야 하며 입금 또는 출금이 진행될때마다 이력이 기록됩니다.
#영수증 변수는 : receipts

# 출금한 금액을 받는 변수 : withdraw_amount
# 출금된 금액은 balance 변수에서 뺀 결과가 되도록 코드를 작성해주세요
# 영수증에 다음 순서로 값이 들어가도록 코드를 만들어 주세요 -> "출금", 출금요청액, 총액 순으로 데이터 넣어주세요
# 가지고 있는 금액보다 출금을 원하는 금액이 클때 가지고 있는 금액만 출금되도록 코드를  작성해주세요
# 단, 영수증에 내역은 변경되지 않아야 하며 입금 또는 출금이 진행될때마다 이력이 기록됩니다.
# 영수증 변수는 : receipts

# 입력 검증 및 에러 처리 추가
# 잘못된 입력 값(숫자가 아닌 값, 음수 값 등)을 처리하도록 기능을 추가해주세요
# 유효하지 않은 메뉴 선택시 경고 메세지 또는 사용방법 재안내를 해주세요 elif 로 구조화 하면 대처하기 쉬움

receipts = [ ] #[ ] 대괄호: list / {} 중괄호 : dict / () :tuple 
balance = 3000  #현재 잔액을 보여주세요
while True:
    num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료)")
    if num == '4':
        break
    if num=="1":
       deposit_amount = int(input("입금할 금액을 입력해주세요 : ")) #내장함수: input()/ int() input()>문자로인식
       if deposit_amount.isdigit() and int(deposit_amount) > 0: #1000 -> True  천원 -> False #Flase 조건을 and 앞에 해주면 코딩속도가 빨라짐
         balance += int(deposit_amount) #산술할당 연산자
       receipts.append(("입금", deposit_amount, balance))
       print(f"입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.")
    else:
        print("입금한 금액을 숫자 형태와 음수형태가 아닌 겂을 입력해주세요")

    if num=="2":
       withdraw_amount = int(input("출금할 금액을 입력해주세요 : ")) 
       withdraw_amount = min(balance, withdraw_amount)
       balance -= withdraw_amount 
       receipts.append(("출금", withdraw_amount, balance))
       print(f"출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.")       

print(f"서비스를 종료합니다. 현재 잔액은 {balance}원 입니다. ")




