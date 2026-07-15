# PLAN: Console MVC PoC

## 1. 구현 순서

1. 프로젝트 실행 방식을 정한다.
2. Model 역할의 간단한 시료 저장 객체를 만든다.
3. View 역할의 메뉴 출력/입력 안내 함수를 만든다.
4. Controller 역할의 메뉴 선택 처리 흐름을 만든다.
5. 예시 실행으로 등록/조회 흐름을 확인한다.
6. README 또는 문서에 최종 프로젝트 재사용 가능 지점을 적는다.

## 2. 예상 구조

```text
ConsoleMVC-myungjunkim-23048751/
├── CLAUDE.md
├── README.md
├── docs/
│   ├── PRD.md
│   ├── SPEC.md
│   └── PLAN.md
└── src/
    ├── model.py
    ├── view.py
    ├── controller.py
    └── main.py
```

구현 언어는 Python으로 확정한다.

## 3. 검증 방법

- 프로그램 실행 후 메인 메뉴가 표시되는지 확인한다.
- 시료 등록 후 목록 조회에서 같은 항목이 보이는지 확인한다.
- Model 파일에 콘솔 입출력이 들어가지 않았는지 확인한다.

## 4. 메인 프로젝트 재사용 계획

최종 프로젝트에서는 이 PoC의 MVC 분리 방식을 참고한다. 필요하다면 `src/poc_references/console_mvc`
같은 별도 디렉토리에 복사해 출처와 목적을 남기고, 실제 운영 코드는 최종 프로젝트 내부 구조에 맞춰
독립적으로 작성한다.
