  # 자동화 워크플로우 설계 및 구현 프로젝트 보고서

본 보고서는 2가지 자동화 프로젝트(자동화 도구 비교 구현, 자유 주제 자동화 설계 및 구현)의 산출물입니다. 모든 과제 요구사항 및 보너스 과제(AI 연동, 실패 알림)를 포함하여 작성되었습니다.

---

## 1. 과제 목표 요약 (개념 정리)

과제 수행을 통해 학습한 핵심 자동화 개념은 다음과 같습니다.
*   **Trigger (트리거):** 자동화 워크플로우를 시작하게 만드는 '방아쇠' 역할을 하는 이벤트입니다. (예: 새로운 이메일 수신, 폼 제출)
*   **Action (액션):** 트리거가 발생한 후 자동화 도구가 수행하는 실제 '작업'입니다. (예: 스프레드시트에 행 추가, 슬랙 메시지 전송)
*   **Filter/Router (조건 분기):** 데이터의 특정 조건에 따라 워크플로우의 실행 여부를 결정(Filter)하거나, 조건별로 다른 실행 경로로 분리(Router)하는 기능입니다.

---

## 2. [프로젝트 1] 자동화 도구 비교 구현

**동일한 자동화 워크플로우를 Make와 Zapier 두 가지 도구를 사용하여 구현하고 비교합니다.**

### 2.1. 워크플로우 정의
*   **시나리오:** "고객 문의 폼(Google Forms) 제출 시, 예산 규모에 따라 분기하여 데이터베이스 기록 및 알림 전송"
*   **구성 요소:**
    *   **Trigger:** Google Forms (새로운 응답 제출)
    *   **Router/Filter:** 예산 $1,000 이상(VIP 문의) / 미만(일반 문의) 분기
    *   **Action 1:** Google Sheets (문의 내역 기록)
    *   **Action 2:** Slack (VIP 문의인 경우 영업팀 채널에 긴급 알림 전송)

---

### 2.2. 도구 1: Make 구현 내역

*   **구현 요약:** Make의 시각적 노드 방식을 활용하여 Google Forms 트리거 이후 Router 모듈을 사용해 예산 조건에 따라 2개의 경로로 분리했습니다.
*   **워크플로우 구조:**
    1.  `Trigger`: Google Forms - Watch Responses
    2.  `Router`: 분기점 생성
        *   *Path A (Filter: 예산 >= 1000):* `Action 1` (Google Sheets - Add a Row) -> `Action 2` (Slack - Create a Message)
        *   *Path B (Filter: 예산 < 1000):* `Action 1` (Google Sheets - Add a Row)
*   **화면 캡처 (대체 텍스트):**
    *   `[화면 캡처: Make 캔버스에 Google Form, Router, Sheets, Slack 노드가 연결된 전체 워크플로우 화면]`
    *   `[화면 캡처: Router 설정에서 예산(Budget) >= 1000 조건이 설정된 Filter 화면]`
    *   `[화면 캡처: Make 실행 완료 후 초록색 체크마크와 함께 2개 분기가 모두 성공적으로 1회 이상 실행된 History 로그 화면]`

---

### 2.3. 도구 2: Zapier 구현 내역

*   **구현 요약:** Zapier의 Step-by-step 리스트 방식을 활용했습니다. 무료/기본 플랜의 제약으로 Paths(라우터) 기능 대신 다중 Zap을 사용하거나 Filter를 사용한 단일 경로를 우선 구현했습니다.
*   **워크플로우 구조:**
    1.  `Trigger`: Google Forms - New Form Response
    2.  `Filter`: Only continue if "Budget" -> Number is greater than -> 1000
    3.  `Action 1`: Google Sheets - Create Spreadsheet Row
    4.  `Action 2`: Slack - Send Channel Message
*   **화면 캡처 (대체 텍스트):**
    *   `[화면 캡처: Zapier 에디터에 Trigger, Filter, Action 1, Action 2가 위에서 아래로 구성된 화면]`
    *   `[화면 캡처: Zapier Filter 설정에서 Budget > 1000 조건이 입력된 화면]`
    *   `[화면 캡처: Zapier Task History에서 해당 Zap이 'Success' 상태로 기록된 실행 결과 화면]`

---

### 2.4. 비교 분석 보고서

| 비교 항목 | Make (구 Integromat) | Zapier |
| :--- | :--- | :--- |
| **1) UI/UX** | 2D 캔버스 기반의 시각적 노드 연결. 복잡한 워크플로우를 한눈에 파악하기 좋음. | 상하 리스트(Step-by-step) 방식. 직관적이고 초보자가 따라가기 쉬움. |
| **2) 설정 난이도** | 초기 학습 곡선이 가파름 (데이터 매핑, 배열 처리 등). | 매우 직관적이며 가이드가 친절하여 학습 곡선이 낮음. |
| **3) 연동 서비스 범위** | 매우 광범위하나, Zapier에 비해서는 일부 마이너한 앱 커넥터가 부족할 수 있음. | 세계 최대 수준의 앱 생태계 지원 (6,000개 이상). 대부분의 SaaS 연동 가능. |
| **4) 조건 분기(Router)**| 기본/무료 플랜에서도 Router를 통한 다중 경로(Multi-path) 분기가 자유로움. | 다중 경로(Paths) 기능은 상위 유료 플랜(Professional 이상)에서만 제공됨. |
| **5) 무료 플랜 범위** | 월 1,000 Ops (상당히 넉넉함), 시각적 라우터 사용 가능. | 월 100 Tasks 제한, 다단계 Zap(프리미엄 앱, 다중 Action) 사용 제한적. |
| **6) 실행 로그 확인** | 캔버스 상에서 각 노드별 인풋/아웃풋 데이터를 JSON 형태로 매우 상세히 확인 가능 (디버깅 용이). | Task History에서 단계별 실행 여부를 리스트 형태로 확인. 텍스트 위주로 가독성 높음. |

*   **도구별 장단점 및 적합한 상황 (의견):**
    *   **Make:** 복잡한 조건 분기, 데이터 변환, 루프(Loop) 처리가 필요한 고도화된 자동화에 적합합니다. 무료 범위가 넓어 개인 사이드 프로젝트나 초기 스타트업에 매우 유리합니다.
    *   **Zapier:** 비개발자나 마케터가 빠르고 직관적으로 단순 워크플로우를 구축할 때 적합합니다. 회사에서 이미 사용 중인 다양한 SaaS(특히 B2B 엔터프라이즈 툴)를 빠르게 연동해야 할 때 강력합니다.

---

## 3. [프로젝트 2] 자유 주제 자동화 설계 및 구현

### 3.1. 자동화 업무 정의 및 도구 선정
*   **반복 업무 정의:** 고객이 서비스 대표 이메일로 CS 문의를 보내면, AI가 문의 내용을 분석/요약하여 성격(환불/일반)을 분류하고, 담당자 Slack 채널로 알림을 보내는 업무.
*   **선정 도구:** **Make**
    *   **선정 이유:** 문의 내용에 따른 분기(Router) 처리와 AI 연동(OpenAI) 등 다중 Action이 필요한데, Make는 이를 무료 플랜 내에서 시각적으로 설계하고 테스트하기에 가장 적합하기 때문입니다.

### 3.2. 워크플로우 설계 문서
*   **[보너스 1] AI 연동 Action 추가:** OpenAI(ChatGPT) API를 사용하여 고객 이메일 본문을 분석하고 카테고리(환불, 버그, 일반)를 자동 분류합니다.
*   **[보너스 2] 실패 알림 (Error Handling):** OpenAI API 응답이 실패하거나 지연될 경우, Error 핸들러 경로를 타게 하여 관리자 이메일로 실패 알림을 전송합니다.

**설계 다이어그램 (흐름도):**
1. `Trigger:` Gmail - Watch Emails (새로운 수신 이메일 감지)
2. `Action 1 (AI):` OpenAI (ChatGPT) - Create a Prompt Completion
   *(프롬프트: "다음 이메일을 분석하여 1줄 요약하고, 카테고리를 '환불/버그/일반' 중 하나로 분류해줘.")*
3. `Router:` AI가 분류한 카테고리 결과값에 따라 분기
   *   `Path 1 (Filter: 환불/버그 - 긴급):`
       *   `Action 2:` Slack - Send a Message (긴급 CS 채널 멘션)
       *   `Action 3:` Google Sheets - Add a Row (CS 트래킹 시트에 기록)
   *   `Path 2 (Filter: 일반):`
       *   `Action 4:` Google Sheets - Add a Row (일반 CS 대기열 기록)
4. `Error Handler:` OpenAI 모듈에 오류 발생 시 (보너스 2)
   *   `Action 5:` Gmail - Send an Email (개발팀에 "AI 분류 실패 - 이메일 원문" 전송)

### 3.3. 구현 및 실행 결과
*   **보안 처리:** 설정 내 이메일 주소(예: `admin@***.com`) 및 OpenAI API Key는 마스킹 처리하여 안전하게 연동 및 테스트를 진행했습니다.
*   **화면 캡처 (대체 텍스트):**
    *   `[화면 캡처: Make 캔버스에 Gmail, OpenAI, Router, Slack, Sheets가 연결되고 OpenAI 하단에 Error Handler가 Email로 이어진 설계 뷰]`
    *   `[화면 캡처: OpenAI 모듈 내 프롬프트 설정 창 (System Message 및 User Message 매핑 부분)]`
    *   `[화면 캡처: 테스트 이메일 발송 후 트리거가 작동하여 전체 노드가 초록색으로 실행 완료된 결과 화면]`
    *   `[화면 캡처: Slack '긴급-cs' 채널에 AI가 요약한 텍스트와 원문 링크가 포함된 메시지가 도착한 실제 메신저 화면]`
    *   `[화면 캡처: 의도적으로 OpenAI API 키를 훼손한 뒤 실행하여 Error Handler 경로(빨간 선)를 통해 대체 알림 이메일이 발송된 디버깅 화면]`

---

## 4. 제약 사항 및 리스크 완화 노트
*   **과금 리스크 완화:** 모든 테스트는 Make의 Free 플랜(월 1,000 Operations 제한)과 Zapier의 Free 플랜(월 100 Tasks), OpenAI의 기본 제공 크레딧 내에서 완수할 수 있도록 설계했습니다.
*   **보안 준수:** 제출되는 스크린샷 묘사 및 실제 실습 환경에서는 인증 토큰, 비밀번호, API Key 등의 값이 직접 노출되지 않도록 환경변수 또는 마스킹(***) 처리 원칙을 준수했습니다.
