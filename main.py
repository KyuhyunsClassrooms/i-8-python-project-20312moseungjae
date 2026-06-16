# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 
# 프로젝트 주제: 

# ============================================================
# 사용 안내
# ------------------------------------------------------------
# 이 파일은 예시 골격입니다.
# 그대로 제출하지 말고, 반드시 자신의 주제에 맞게 수정하세요.
#
# 필수 조건
# 1. 2차원 리스트 사용
# 2. 함수 2개 이상, 가능하면 3개 이상 분리
# 3. 조건문 사용
# 4. 반복문 사용
# 5. 실행 결과 출력
# ============================================================


# ------------------------------------------------------------
# 1. 데이터 준비: 2차원 리스트
# ------------------------------------------------------------
# 아래 데이터는 "친환경 생활 습관 점수 판정기" 기록입니다.
# 
# 현재 열의 의미:
# 0번 열: 요일 구분
# 1번 열: 텀블러 사용 횟수
# 2번 열: 분리배출 수행 횟수
# 3번 열: 대중교통 이용 횟수
# ------------------------------------------------------------

eco_records = [
    ["월요일", 1, 0, 1],
    ["화요일", 0, 1, 1],
    ["수요일", 1, 1, 0],
    ["목요일", 0, 0, 1],
    ["금요일", 1, 1, 1],
    ["토요일", 0, 0, 0],
    ["일요일", 1, 0, 0]
]


# ------------------------------------------------------------
# 2. 함수 정의
# ------------------------------------------------------------

def show_intro():
    """프로그램 제목과 안내를 출력한다."""
    print("=" * 40)
    print(" 친환경 생활 습관 점수 판정기 ")
    print("일주일간의 실천 기록을 분석해 드립니다.")
    print("=" * 40)

def get_user_name():
    """사용자의 닉네임을 입력받는다."""
    name = input("결과를 확인할 닉네임을 입력하세요: ")
    return name

def analyze_eco_data(data):
    """2차원 리스트를 반복하며 항목별 총합과 총점을 계산한다."""
    total_tumbler = 0
    total_recycle = 0
    total_transport = 0

    for row in data:
        total_tumbler = total_tumbler + row[1]
        total_recycle = total_recycle + row[2]
        total_transport = total_transport + row[3]

    total_score = (total_tumbler * 5) + (total_recycle * 3) + (total_transport * 4)

    totals = [total_tumbler, total_recycle, total_transport]
    return total_score, totals

def evaluate_grade(score):
    """총점에 따라 친환경 등급을 판정한다."""
    if score >= 60:
        return "최우수 지구 지킴이 "
    elif score >= 40:
        return "우수 실천가 "
    else:
        return "조금 더 노력이 필요해요 "

def print_report(name, score, grade, totals):
    """최종 결과를 출력한다."""
    print("\n[친환경 실천 분석 결과]")
    print(f"{name}님의 이번 주 총점은 {score}점입니다.")
    print(f"최종 등급: {grade}")
    print("-" * 30)
    print(f"텀블러 사용 총합: {totals[0]}회")
    print(f"분리배출 수행 총합: {totals[1]}회")
    print(f"대중교통 이용 총합: {totals[2]}회")
    print("-" * 30)


# ------------------------------------------------------------
# 3. 프로그램 실행
# ------------------------------------------------------------
def main():
    show_intro()
    name = get_user_name()
    score, totals = analyze_eco_data(eco_records) 
    grade = evaluate_grade(score) 
    print_report(name, score, grade, totals)
main()