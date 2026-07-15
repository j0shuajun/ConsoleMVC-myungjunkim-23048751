"""Console output and input prompts. No business logic belongs here."""

MAIN_MENU = """
==============================================
반도체 시료 생산주문관리 시스템 (Console MVC PoC)
----------------------------------------------
[1] 시료 등록   [2] 시료 목록 조회   [0] 종료
=============================================="""


def show_main_menu():
    print(MAIN_MENU)


def prompt_choice():
    return input("선택 > ").strip()


def prompt_sample_input():
    sample_id = input("시료 ID > ").strip()
    name = input("이름 > ").strip()
    average_production_time = float(input("평균 생산시간(min/ea) > ").strip())
    yield_rate = float(input("수율(0~1) > ").strip())
    return sample_id, name, average_production_time, yield_rate


def show_registered(sample):
    print(f"등록 완료: {sample.sample_id} ({sample.name})")


def show_duplicate_error(sample_id):
    print(f"이미 등록된 시료 ID입니다: {sample_id}")


def show_sample_list(samples):
    if not samples:
        print("등록된 시료가 없습니다.")
        return
    print(f"등록 시료 목록 (총 {len(samples)}종)")
    for sample in samples:
        print(
            f"  {sample.sample_id}\t{sample.name}\t"
            f"{sample.average_production_time}min/ea\t수율 {sample.yield_rate}"
        )


def show_unknown_choice():
    print("올바른 번호를 선택해주세요.")


def show_goodbye():
    print("프로그램을 종료합니다.")
