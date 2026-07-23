# [프로젝트 2] 자유 주제 자동화 설계 및 구현 보고서

## 1. 반복 업무 정의 및 문제 인식
* **업무명:** 개인/가족 맞춤형 데일리 리서치 및 모바일 푸시 브리핑 업무
* **기존 문제점:** 실시간 검색어 폐지 이후 주요 뉴스, 정치, 경제, 스포츠, 영화, 여행지, 맛집 정보 등 수많은 분야의 최신 소식을 직접 찾아보고 요약하는 데 매일 30분 이상의 비효율적인 시간이 소요됨.
* **자동화 목표:** 매일 아침 8시, AI가 분야별 RSS 피드를 자동으로 읽고 모바일 전용 템플릿으로 핵심 요약하여 아이폰/안드로이드 구분 없이 푸시 알림을 즉시 발송하는 무인 자동화 환경 구축.

---

## 2. 자동화 도구 선정 및 선정 이유
* **선정 도구:** **Make (Integromat)**
* **선정 이유:**
  1. **복잡한 다중 RSS 데이터 수집 및 취합 능력:** 9개 분야의 독립된 RSS 피드를 동시에 수집하고 `Text Aggregator` 모듈로 병합하는 고난도 데이터 처리 능력이 우수함.
  2. **오픈 API 및 HTTP Webhook 유연성:** 별도의 토큰 갱신 리스크가 없는 `ntfy.sh` REST API 통신 및 `Google Gemini 2.5 Flash` AI 모델 연동 지원.
  3. **과금 리스크 최소화:** 무료 플랜(월 1,000 Operations) 내에서 완벽하게 구동 가능.

---

## 3. 워크플로우 설계 문서

### 3.1 워크플로우 개념 다이어그램

[Trigger: Schedule (매일 08:00)]  
│  
├───> [Action 1: RSS Feed Read (9개 카테고리 동시 수집)]  
│        ├── 사건사고 / 증권주식 / 국내정치 / 국제정치  
│        └── 야구 / 축구 / 영화 / 여행지 / 맛집  
│  
├───> [Action 2: Text Aggregator (데이터 하나로 병합)]  
│  
├───> [Condition Branch: Filter (유효 데이터 존재 여부 검증)]  
│  
├───> [Action 3 (AI): Gemini 2.5 Flash (카테고리별 1~2줄 요약 생성)]  
│  
└───> [Action 4: HTTP POST (ntfy.sh REST API 푸시 발송)]  


### 3.2 단계별 매핑 데이터 상세
1. **Trigger (Schedule):** 매일 지정 시각 자동 개시
2. **Action 1 (RSS Read):** Google News RSS 퍼센트 인코딩 주소 입력
   * *예시(사건사고):* `https://news.google.com/rss/search?q=%EC%82%AC%EA%B1%B4+%EC%82%AC%EA%B3%A0&hl=ko&gl=KR&ceid=KR:ko`
3. **Action 2 (Text Aggregator):** 각 RSS 모듈의 `{{title}}`과 `{{description}}`을 하나의 텍스트 블록으로 결합
4. **Condition Branch (Filter):** Aggregated Text의 길이(`length > 0`) 검증
   * *역할:* RSS 수집 데이터가 비어있을 경우 AI API 호출 과금을 방지하고 실행을 안전하게 중단함.
5. **Action 3 (Gemini AI 요약):** `gemini-2.5-flash` 모델을 통한 가독성 높은 모바일 메시지 생성
6. **Action 4 (ntfy HTTP Request):**
   * **URL:** `https://ntfy.sh/Todays`
   * **Method:** `POST`
   * **Header:** `Priority: default`, `Tags: newspaper`, `Content-Type: text/plain; charset=utf-8`

---

## 4. 개념 설명 및 요구사항 충족 검증

### 4.1 개념 설명
* **Trigger (트리거):** 워크플로우를 시작시키는 이벤트 (예: 매일 지정된 시각 스케줄 실행).
* **Action (액션):** 트리거 발생 후 시스템이 수행하는 실제 작업 (예: RSS 읽기, AI 요약, HTTP 요청).
* **Filter / Router (조건 분기):** 조건 만족 여부에 따라 실행 경로를 제어하거나 불필요한 실행을 차단하는 가드 역할.

### 4.2 과제 요구사항 충족표
* **Trigger 1개 이상:** Schedule / Timer 모듈 적용 완료
* **Action 2개 이상:** RSS Read, Text Aggregator, Gemini AI, HTTP POST (총 4개) 적용 완료
* **조건 분기(Filter) 1개 이상:** 데이터 유효성 검증 필터 적용 완료
* **생성형 AI 연동 (보너스 1):** Google Gemini 2.5 Flash 적용 완료

---

## 5. 구현 및 실행 결과 화면

* **Make 시나리오 전체 구현 화면 (캡처 위치):**
  > `[Make Scenario Builder 전체 흐름 캡처 이미지 첨부]`
* **Filter 실행 및 조건 만족 처리 화면 (캡처 위치):**
  > `[Make Filter 통과 결과(Filter 돋보기 아이콘 클릭) 캡처 이미지 첨부]`
* **최종 스마트폰 푸시 알림 수신 화면 (캡처 위치):**
  > `[iOS / Android ntfy 앱 모닝 뉴스 푸시 알림 수신 스크린샷 첨부]`

---

## 6. 보안 및 민감정보 보호 조치
* 제출된 모든 결과물(스크린샷, URL)의 API Key, Webhook 개인 토픽명, 계정 이메일 주소는 보안 가이드라인에 따라 마스킹 처리(`***`) 완료하였습니다
