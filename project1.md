# 📑 자동화 도구 비교 및 자유 주제 워크플로우 구현 보고서

## 1. 개념 정리 및 핵심 이론
본 과제를 수행하며 학습한 노코드(No-Code) 자동화의 핵심 개념은 다음과 같습니다.

* **Trigger (트리거):** 자동화 워크플로우가 시작되도록 만드는 **'계기(이벤트)'**입니다.  
  *(예: 매일 아침 07:30 정해진 시각, RSS 최신 글 수집, 구글 폼 응답 제출 등)*
* **Action (액션):** 트리거 발생 후 자동화 도구가 **'수행하는 작업'**입니다.  
  *(예: Gemini AI를 통한 텍스트 요약, 디스코드 메시지 전송, 구글 시트 행 추가 등)*
* **Filter / Router (조건 분기):** 수집된 데이터의 조건에 따라 실행 여부를 결정하거나 경로를 나누는 **'제어 장치'**입니다.
  * **Filter:** 특정 조건(예: 비속어/SKIP 문구 미포함)을 만족하는 데이터만 다음 단계로 통과시킵니다.
  * **Router:** 조건별로 각기 다른 실행 경로(예: 긴급건 ➔ 디스코드, 일반건 ➔ 구글 시트 적재)로 분기합니다.

---

## 2. [프로젝트 1] 자동화 도구 비교 구현 (Make vs. Zapier)

### 2.1. 프로젝트 1 워크플로우 정의
* **업무명:** 2030 클린 이슈 자동 요약 및 디스코드 아침 브리핑
* **목적:** 대형 커뮤니티의 자극적·편향적 콘텐츠를 제어하고, 매일 아침 07:30에 정제된 주요 이슈(주식/증시, 재테크/부동산, 국제정세/정치)만 디스코드로 수신
* **구조:** `Trigger(일정/RSS)` ➔ `Action 1(데이터 병합)` ➔ `Action 2(Gemini AI 분석)` ➔ `Filter(SKIP 검증)` ➔ `Action 3(디스코드 웹훅 전송)`

---

### 2.2. Make 구현

#### 1) 워크플로우 구성 요소
1. **Trigger:** `Schedule` (매일 07:30) + `RSS - Retrieve RSS items`
   * Google News RSS를 통해 주식, 재테크, 국제정세 키워드 뉴스 수집 (최대 15개)
2. **Action 1:** `Tools - Text Aggregator`
   * 수집된 15개 뉴스 텍스트 데이터를 하나의 통문장(`text`)으로 병합
3. **Action 2:** `Google Generative AI - Generate Content` (Gemini Flash)
   * 프롬프트를 통해 부적절한 데이터 감지 시 "SKIP" 출력, 정상 시 3가지 카테고리 요약 및 대화 질문 생성
4. **Filter:** `SKIP 제거 필터`
   * Gemini 출력값에 `SKIP` 단어가 포함되지 않은 경우만 통과 (`Text operators: Does not contain 'SKIP'`)
5. **Action 3:** `HTTP - Make a request`
   * 디스코드 웹훅 URL로 JSON 형태 데이터 POST 전송

#### 2) 화면 캡처
* **구현 화면:**
  ![Make 전체 시나리오 노드 구성]([캡처 1: Make 전체 시나리오 노드 구성 화면 (RSS -> Text Aggregator -> Gemini -> Filter -> HTTP)])
* **실행 결과 및 조건 분기(Filter) 통과/차단 검증:**
  ![Make 실행 결과 및 필터 검증]([캡처 2: Make 실행 결과 버블 캡처 - 정상 처리 건(Discord 수신) 및 SKIP으로 필터링된 건 로그])

---

### 2.3. Zapier 구현

#### 1) 워크플로우 구성 요소
1. **Trigger:** `Schedule by Zapier` (Every Day at 07:30 AM)
2. **Action 1:** `Webhooks by Zapier (GET)`
   * 구글 뉴스 RSS 인코딩 URL로 응답 데이터(XML/Raw) 수집
3. **Action 2:** `Google Gemini (Generate Content)`
   * Make와 동일한 프롬프트로 3대 영역 요약문 생성
4. **Filter:** `Filter by Zapier`
   * Gemini 응답 결과가 `SKIP`을 포함하지 않는 경우만 통과 (`Text Does Not Contain 'SKIP'`)
5. **Action 3:** `Discord (Send Channel Message)` 또는 `Webhooks by Zapier (POST)`
   * 디스코드 채널로 메시지 자동 게시

#### 2) 화면 캡처
* **구현 화면:**
  ![Zapier 단계별 설정 화면]([캡처 3: Zapier 단계별 설정 화면 (Schedule -> Webhooks -> Gemini -> Filter -> Discord)])
* **실행 결과 화면:**
  ![Zapier Task History 실행 성공]([캡처 4: Zapier Task History 실행 성공 데이터 및 디스코드 메시지 캡처])

---

### 2.4. 비교 분석 보고서 (Make vs. Zapier)

| 비교 항목 | Make (구 Integromat) | Zapier |
|---|---|---|
| **1. UI/UX 캔버스** | **시각적 무제한 노드 캔버스**<br>(드래그 앤 드롭, 데이터 흐름이 직관적) | **선형 리스트(Top-Down) 방식**<br>(단계별 순서 파악이 명확) |
| **2. 설정 난이도** | 중상 (변수 매핑, JSON/Array 구조 이해 필요) | 하 (직관적이며 입력 칸이 명확함) |
| **3. 연동 서비스 범위** | 약 1,500+개 (주요 앱 완벽 지원) | **약 6,000+개 (업계 최대 앱 연동폭)** |
| **4. 무료 플랜 제공 범위** | **월 1,000 Operations / 모듈 수 무제한** | 월 100 Tasks / 2개 단계(Single-zap) 한정 |
| **5. 데이터 가공 및 모듈** | **`Text Aggregator`, `Iterator` 등 가공 도구 강력** | 별도 Formatter 단계를 소비해야 함 |
| **6. 실행 로그 및 디버깅** | **각 모듈별 입력/출력 버블을 3D 시각화하여 확인 가능** | Data In/Out을 데이터 탭에서 텍스트로 확인 |

#### 장단점 정리 및 적합한 상황 추천

* **Make**
  * **장점:** 무료 플랜 작업 건수(1,000 Ops)가 넉넉함. 시각적 캔버스 덕분에 복잡한 다중 분기(Router) 및 데이터 모으기(Text Aggregator) 처리가 매우 강력함.
  * **단점:** 초기 학습 곡선이 있으며 Array/JSON 등 기본 데이터 구조 이해가 필요함.
  * **추천 상황:** 복잡한 조건 분기가 필요하거나, AI 연동 및 데이터 가공 단계가 많은 워크플로우를 **무료/저비용**으로 구축하고자 할 때.

* **Zapier**
  * **장점:** 압도적인 연동 서비스 보유 수. UI가 매우 쉬워서 초보자도 5분 만에 구축 가능.
  * **단점:** 무료 플랜(100 Tasks, 2-Step 제한)이 야박하여 필터/AI 등 3단계 이상 구성 시 유료 결제가 필수적임.
  * **추천 상황:** 마이너한 사내 툴 연동이 필요하거나, 복잡한 로직 없이 **빠르고 직관적으로 단순 연동**을 구현해야 할 때.