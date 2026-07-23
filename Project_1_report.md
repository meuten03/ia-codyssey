# [프로젝트 1] 자동화 도구 비교 구현 보고서

## 1. 개요 및 과제 목표
본 보고서는 동일한 '실시간 다중 카테고리 RSS 수집 및 AI 요약 데일리 뉴스 푸시 알림' 워크플로우를 **Make**와 **Zapier** 2가지 도구로 직접 구축하고, 각 도구의 구조적 특징과 UI/UX, 비용 구조 등을 비교 분석한 결과서입니다.

---

## 2. 워크플로우 정의 및 아키텍처
* **주제:** 매일 아침 분야별(사건사고, 증권, 국내/국제정치, 야구/축구, 영화, 여행, 맛집) 최신 RSS 피드를 수집하여 생성형 AI(Gemini / ChatGPT)로 요약 후 크로스 플랫폼 푸시 알림(ntfy.sh) 전송
* **워크플로우 흐름 구조:**
  1. **Trigger:** Schedule / Timer (매일 지정 시각 자동 실행)
  2. **Action 1 (수집):** RSS Feed Fetcher (총 9개 카테고리 Google News RSS 수집)
  3. **Action 2 (취합):** Text Aggregator / Formatter (9개 피드 원문 데이터 하나로 결합)
  4. **Action 3 (AI 요약 - 보너스 과제 1):** Gemini 2.5 Flash / ChatGPT (카테고리별 1~2줄 요약 텍스트 생성)
  5. **Action 4 (푸시 알림):** HTTP Webhooks (ntfy.sh REST API 호출을 통한 iOS/Android 푸시 발송)

---

## 3. 도구별 워크플로우 구현 화면 및 실행 결과

### 3.1 Make (Integromat) 구현
* **워크플로우 구성 화면 (캡처 위치):**
  > `[Make Scenario Builder 캡처 이미지 첨부]`
  > *(RSS 모듈 9개 $\rightarrow$ Text Aggregator 9개 $\rightarrow$ Gemini 2.5 Flash $\rightarrow$ HTTP POST ntfy 모듈 연결 캔버스)*
* **실행 결과 화면 (캡처 위치):**
  > `[Make Run Once 실행 성공 로그 & ntfy 푸시 알림 수신 캡처 이미지 첨부]`
  > *(Status Code: 200 / ntfy 모바일 앱 상단바 알림 스크린샷)*

### 3.2 Zapier 구현
* **워크플로우 구성 화면 (캡처 위치):**
  > `[Zapier Zap Editor 캡처 이미지 첨부]`
  > *(Schedule by Zapier $\rightarrow$ RSS by Zapier $\rightarrow$ AI Formatter $\rightarrow$ Webhooks by Zapier POST)*
* **실행 결과 화면 (캡처 위치):**
  > `[Zapier Test Step 실행 결과 & ntfy 푸시 알림 수신 캡처 이미지 첨부]`

---

## 4. 자동화 도구 비교 분석 보고서 (Make vs Zapier)

| 비교 항목 | Make (Integromat) | Zapier |
| :--- | :--- | :--- |
| **1. UI / UX 및 가시성** | **비주얼 캔버스 형태**로 모듈 간 맵핑 흐름과 데이터 전달 과정을 한눈에 직관적으로 파악 가능 | **단계별 순차적 목록(Linear List)** 형태로 초보자가 차례대로 따라 하기 쉬움 |
| **2. 설정 난이도** | 데이터 변환 연산자(Parser, Aggregator 등) 활용도가 높아 복잡한 로직 구현 시 약간의 학습 필요 | AI Copilot 및 템플릿 제공이 우수하여 자연어 입력만으로 빠르게 초안 작성 가능 |
| **3. 연동 서비스 범위** | 1,500개 이상의 주요 서비스 지원 및 Custom HTTP Request 기능이 매우 유연함 | 6,000개 이상의 독보적인 앱 연동 수 보유 |
| **4. 무료 플랜 범위** | 월 1,000 오퍼레이션(Operation) 제공. 단일 시나리오 내 다중 모듈 구성에 제약이 적음 | 월 100 오퍼레이션(Tasks) 제한 및 2단계 이상 Multi-step Zap 구성 시 제약 존재 |
| **5. 실행 로그 확인 방식** | 실행 단위별 모듈의 Data In/Out(JSON 구조)을 실시간 다이어그램상에서 클릭하여 정밀 디버깅 가능 | Zap History 메뉴에서 단계별 성공/실패 여부 및 입력/출력값 텍스트 확인 |

---

## 5. 도구별 장단점 및 적합한 상황 제안

### 1) Make (Integromat)
* **장점:** 복잡한 다중 분기(Router), 데이터 취합(Aggregator), 커스텀 HTTP Webhook 처리가 매우 자유롭고 무료 플랜 오퍼레이션 수가 여유로움.
* **단점:** 초기 진입 장벽이 높고 노드 간 데이터 구조(Array, Collection)를 이해해야 함.
* **적합한 상황:** 데이터 변환 작업이 많거나, 3단계 이상의 복잡한 멀티 스텝 자동화 및 비용 효율적인 자동화를 원할 때.

### 2) Zapier
* **장점:** 직관적인 UI와 뛰어난 자연어 기반 AI 구축 기능, 압도적인 타사 앱 연동성.
* **단점:** 무료 플랜 범위가 매우 협소하고 multi-step 자동화 시 유료 플랜 전환 압박이 큼.
* **적합한 상황:** 1:1 방식의 단순 연동을 빠르게 구축하고 싶거나 전용 앱 연동성이 최우선일 때.