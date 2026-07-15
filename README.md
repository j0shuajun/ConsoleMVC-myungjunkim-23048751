# ConsoleMVC PoC

반도체 시료 생산주문관리 시스템 과제의 **콘솔 MVC 구조 검증 PoC**입니다.

## 역할

콘솔 애플리케이션에서 사용자 입력(Controller), 데이터/상태(Model), 화면 출력(View)의
책임을 어떻게 나눌지 최종 프로젝트를 만들기 전에 작은 예제로 검증합니다.

## 주요 기능

- 콘솔 메인 메뉴 표시
- 시료 등록 (Controller가 입력을 받아 Model에 반영)
- 시료 목록 조회 (View가 Model의 현재 상태를 출력)
- 프로그램 종료

## 구조 원칙

| 계층 | 책임 |
|---|---|
| Model | 시료 데이터와 상태 보관, 콘솔 입출력에 관여하지 않음 |
| View | 메뉴/결과 출력, 입력 안내 |
| Controller | 입력 해석, Model 변경, View 호출 |

## 실행 환경

- 구현 언어: Python
- 데이터는 메모리에만 보관합니다 (영속성은 [DataPersistence PoC](https://github.com/j0shuajun/DataPersistence-myungjunkim-23048751) 참고).

## 문서

- [`docs/PRD.md`](docs/PRD.md): 이 PoC가 검증하려는 사용자 가치
- [`docs/SPEC.md`](docs/SPEC.md): 기능 명세와 MVC 책임 분리 기준
- [`docs/PLAN.md`](docs/PLAN.md): 구현 순서와 메인 프로젝트 재사용 계획
- [`CLAUDE.md`](CLAUDE.md): 이 저장소에서의 작업 규칙

## 메인 프로젝트와의 관계

이 PoC의 MVC 분리 구조는 최종 프로젝트인
[SampleOrderSystem](https://github.com/j0shuajun/SampleOrderSystem-myungjunkim-23048751)의
콘솔 CLI 경계 설계에 참고 자료로 사용됩니다.
