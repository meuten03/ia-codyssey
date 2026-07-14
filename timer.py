import datetime
import time
import os
import sys

TARGET_HOURS = 80.0
MAX_DAILY_HOURS = 12.0

def parse_accumulated_time(input_str):
    """'25.5' 또는 '25:30' 형식의 누적 시간을 실수(float) 시간으로 변환합니다."""
    try:
        if ':' in input_str:
            h, m = map(int, input_str.split(':'))
            return h + (m / 60.0)
        else:
            return float(input_str)
    except ValueError:
        print("⚠️ 입력 형식이 잘못되었습니다. 기본값 0시간으로 시작합니다.")
        return 0.0

def parse_start_time(input_str):
    """'0930' 또는 '09:30' 형식의 시간을 오늘 날짜의 datetime으로 변환합니다."""
    now = datetime.datetime.now()
    if not input_str:
        return now
    try:
        if ':' in input_str:
            h, m = map(int, input_str.split(':'))
        else:
            h = int(input_str[:2])
            m = int(input_str[2:])
        return now.replace(hour=h, minute=m, second=0, microsecond=0)
    except Exception:
        print("⚠️ 입력 형식이 잘못되었습니다. 현재 시간으로 시작합니다.")
        return now

def format_timedelta(td_seconds):
    """초(seconds)를 HH:MM:SS 형식의 문자열로 변환합니다."""
    h = int(td_seconds // 3600)
    m = int((td_seconds % 3600) // 60)
    s = int(td_seconds % 60)
    return f"{h:02d}시간 {m:02d}분 {s:02d}초"

def calculate_fastest_route(remaining_hours):
    """일 최대 12시간 기준으로 가장 빠르게 채우는 플랜을 계산합니다."""
    if remaining_hours <= 0:
        return "🎉 축하합니다! 80시간을 모두 채웠습니다!"
    
    full_days = int(remaining_hours // MAX_DAILY_HOURS)
    leftover = remaining_hours % MAX_DAILY_HOURS
    
    route = ""
    if full_days > 0:
        route += f"하루 12시간씩 꽉 채워서 {full_days}일 출석"
    if leftover > 0:
        if full_days > 0:
            route += f"\n👉 그리고 마지막 날에 {leftover:.1f}시간 추가 출석"
        else:
            route += f"오늘 {leftover:.1f}시간 출석"
    return route

def main():
    print("=" * 45)
    print("  🚀 실시간 80시간 카운트다운 트래커  ")
    print("=" * 45)
    
    acc_input = input("\n1. 지금까지의 누적 시간을 입력하세요\n(예: 25.5 또는 25:30): ").strip()
    initial_accumulated_hours = parse_accumulated_time(acc_input)

    start_input = input("\n2. 오늘 출석을 시작한 시간을 입력하세요\n(예: 0930 또는 09:30 / 방금 시작했다면 그냥 엔터): ").strip()
    start_time = parse_start_time(start_input)

    print("\n✅ 설정 완료! 실시간 트래커 화면으로 넘어갑니다...")
    time.sleep(2)

    try:
        while True:
            now = datetime.datetime.now()
            
            # 미래 시간을 시작 시간으로 적었을 경우 방어
            if now > start_time:
                elapsed_seconds = (now - start_time).total_seconds()
            else:
                elapsed_seconds = 0
            
            # 시간 계산
            total_acc_seconds = (initial_accumulated_hours * 3600) + elapsed_seconds
            remaining_seconds = max(0, (TARGET_HOURS * 3600) - total_acc_seconds)
            remaining_hours = remaining_seconds / 3600
            
            # 터미널 화면 지우기 (윈도우는 cls, 맥/리눅스는 clear)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # 대시보드 출력
            print("=" * 50)
            print("            ⏱️ 80시간 실시간 대시보드 ⏱️")
            print("=" * 50)
            print(f" ▶ 오늘 출석 시작 : {start_time.strftime('%H시 %M분 %S초')}")
            print(f" ▶ 현재 시간      : {now.strftime('%H시 %M분 %S초')}")
            print("-" * 50)
            print(f" 📈 오늘 진행 시간 : {format_timedelta(elapsed_seconds)}")
            print(f" 🔥 총 누적 시간   : {format_timedelta(total_acc_seconds)} (카운트업 🔼)")
            print(f" ⏳ 남은 시간      : {format_timedelta(remaining_seconds)} (카운트다운 🔽)")
            print("-" * 50)
            print(" 💡 [최단 시간 달성 플랜 (일 최대 12시간 제한)]")
            print(f" 👉 {calculate_fastest_route(remaining_hours)}")
            print("=" * 50)
            print(" (프로그램을 종료하려면 키보드에서 Ctrl + C 를 누르세요)")
            
            # 1초 대기 후 화면 갱신
            time.sleep(1)

    except KeyboardInterrupt:
        # Ctrl + C를 눌렀을 때 깔끔하게 종료
        print("\n\n🛑 트래커를 종료합니다. 수고하셨습니다!\n")
        sys.exit()

if __name__ == "__main__":
    main()