# 스토리보드 기획안

## 1. 브랜드 아이덴티티
* **브랜드명:** 센트 오브 아카이브 (Scent of Archive)
* **정체성:** 단순히 '좋은 향'을 넘어, 누군가의 마음속 깊은 곳에 자리한 '특정 시공간의 기억'을 조향하는 향수 브랜드. 화려함보다는 일상 속의 아련함, 위로, 그리고 향수를 자극하는 서정적인 감성을 지향합니다.

## 2. 캠페인 목표 및 핵심 메시지
* **캠페인 명:** "그해 여름, 소나기 (The Summer Shower)" 컬렉션 론칭 캠페인
* **캠페인 목표:** 소비자들에게 어린 시절의 순수했던 감각을 일깨워 제품에 대한 정서적 유대감을 형성하고, '기억을 담은 향수'라는 브랜드 포지셔닝을 강화합니다.
* **핵심 메시지:** **"향기는 가장 선명한 타임머신이다. 당신의 가장 눈부셨던 여름으로 안내합니다."**

## 3. 사용 도구 목록
* **Gemini 3.5 Pro:** 스토리보드 씬별 세부 기획, 이미지/영상 생성을 위한 프롬프트 엔지니어링 및 감성적인 내레이션 텍스트 작성, 텍스트 프롬프트를 기반으로 씬별 고해상도 초실사 비디오(동영상) 일괄 생성
* **Vrew:** BGM 추가 및 최종 영상 컷편집
* **OpenAI Sora 2:** 영상 생성 도구의 대기열 시 대체 도구로 준비
* * **Capcut:** 영상 컷편집 도구의 대기열 시 대체 도구로 준비
## 3.1. 사용 도구 선정 이유
* ** Gemini 3.5 Pro:** 최신 AI 모델로, 감성적이고 사실적인 영상 생성에 최적화되어 있으며, 프롬프트 기반으로 세밀한 씬 연출이 가능하여 브랜드의 정서적 메시지를 효과적으로 전달할 수 있습니다. 
* 추가로 추상적이고 감성적인 기억을 시각화하는 업무를 수행하고자 하므로 사용자와 ai간의 상호작용이 필수적이므로 토큰의 비용면에서 우수한 Gemini를 선택하였습니다.
* * **Vrew:** Gemini 3.5 Pro에서 생성된 영상 클립을 효율적으로 편집하고, 여러 씬을 한번에 합치고 비율을 수정하는 것에 최적화된 도구라고 판단하여 Vrew를 선택하였습니다.
---

## 4. 씬(Scene) 구성

### Scene 01
| 항목 | 내용 |
| :--- | :--- |
| **씬 번호 / 길이** | Scene 01 / 3초 |
| **목표 메시지** | 일상 속에서 우연히 마주한 추억의 시작. |
| **화면 구성** | **구도:** 클로즈업<br>**피사체:** 투명한 향수병의 캡을 여는 손<br>**배경:** 나른한 오후의 햇살이 비치는 차분한 방<br>**텍스트:** 없음 |
| **내레이션/카피** | (내레이션) "어떤 향기는 순식간에 우리를 그 시절로 데려간다." |
| **사용 도구** | **Gemini 3.5 Pro** (기획/프롬프트,고화질 영상 생성), **Vrew** (컷 편집) |
| **입력 프롬프트** | `Cinematic close-up of a hand gently opening a minimalist glass perfume bottle, soft afternoon sunlight shining through the window, photorealistic, 4k, 60fps` |
| **출력 결과 요약** | 부드러운 햇살 아래 향수병을 여는 감성적인 고해상도 영상. |
| **생성 결과 파일명** | `SC01_Perfume_Open_v1.mp4` |

### Scene 02
| 항목 | 내용 |
| :--- | :--- |
| **씬 번호 / 길이** | Scene 02 / 5초 |
| **목표 메시지** | 향기가 빗방울이 되어 과거의 감각(후각/시각)을 깨움. |
| **화면 구성** | **구도:** 익스트림 클로즈업에서 줌아웃<br>**피사체:** 향수 방울이 흙바닥 웅덩이에 떨어지는 모습<br>**배경:** 비 오는 날의 짙은 흙바닥<br>**텍스트:** [화면 중앙] "기억나? 흙내음 가득했던 그날" |
| **내레이션/카피** | (내레이션) "비가 오면 짙어지던 흙내음, 그리고..." |
| **사용 도구** | **Gemini 3.5 Pro** (슬로우 모션 영상 생성), **Vrew** (사운드 믹싱) |
| **입력 프롬프트** | `Macro shot of a clear water drop falling into a muddy puddle, rippling water, smell of rain visual metaphor, dark wet dirt background, slow motion, cinematic, hyper-detailed` |
| **출력 결과 요약** | 흙탕물 웅덩이에 물방울이 떨어지며 파장이 넓게 퍼지는 실사 슬로우 모션. |
| **생성 결과 파일명** | `SC02_Raindrop_Puddle_v1.mp4` |

### Scene 03
| 항목 | 내용 |
| :--- | :--- |
| **씬 번호 / 길이** | Scene 03 / 4초 |
| **목표 메시지** | 옷이 다 젖어도 마냥 즐거웠던 순수한 어린 시절의 향수 극대화. |
| **화면 구성** | **구도:** 미디엄 샷, 트래킹 샷<br>**피사체:** 흠뻑 젖은 옷을 입고 해맑게 웃으며 뛰노는 아이들<br>**배경:** 푸른 여름 나무가 우거진 1990년대 한국의 오래된 골목길<br>**텍스트:** 없음 |
| **내레이션/카피** | (내레이션) "온몸이 다 젖어도 웃음이 끊이지 않았던" |
| **사용 도구** | **Gemini 3.5 Pro** (동적 인물 영상 생성), **Vrew** (컷 편집) |
| **입력 프롬프트** | `Korean children running and laughing in the rain, fully soaked clothes, 1990s Korean retro alleyway, green summer trees, joyful and deeply nostalgic atmosphere, cinematic lighting, dynamic camera tracking, photorealistic` |
| **출력 결과 요약** | 비를 맞으며 오래된 골목길을 달리는 한국 아이들의 생동감 넘치는 모습. |
| **생성 결과 파일명** | `SC03_Children_Playing_Rain_v2.mp4` |

> **💡 [Scene 03 프롬프트 수정 전/후 및 수정 이유]**
> * **수정 전 프롬프트:** `Children playing in the rain, summer vacation, happy, realistic, 4k`
> * **수정 이유:** 초기 프롬프트로는 노란 우비를 입은 서구권 아이들의 정형화된 이미지가 출력되었습니다. 기획 의도인 '한국인의 여름방학, 흙장난, 젖은 옷'이라는 특정 향수를 자극하기 위해 Gemini 3.5 Pro를 통해 인종(`Korean children`), 디테일(`fully soaked clothes`), 시대 및 공간적 배경(`1990s Korean retro alleyway`), 카메라 워크(`dynamic camera tracking`)를 추가하여 프롬프트를 수정했습니다.

### Scene 04
| 항목 | 내용 |
| :--- | :--- |
| **씬 번호 / 길이** | Scene 04 / 2초 |
| **목표 메시지** | 추억의 향으로 인해 정서적 위로를 얻고 미소 짓는 현재의 모습. |
| **화면 구성** | **구도:** 바스트 샷<br>**피사체:** 눈을 감고 옅은 미소를 지으며 향수를 손에 쥔 20~30대 여성<br>**배경:** 빗방울이 맺힌 창가 밖으로 흐릿하게 보이는 푸른 잎사귀<br>**텍스트:** 없음 |
| **내레이션/카피** | ... |
| **사용 도구** | **Gemini 3.5 Pro** (인물 미세 표정 영상 생성), **Vrew** (컷 편집) |
| **입력 프롬프트** | `A young Korean woman in her 20s standing by a window with gentle raindrops, eyes closed with a soft nostalgic smile, holding a glass perfume bottle to her chest, soft cinematic mood lighting, extremely lifelike facial expression` |
| **출력 결과 요약** | 창가에서 눈을 감고 추억에 젖어 평온하게 미소 짓는 여성의 사실적인 영상. |
| **생성 결과 파일명** | `SC04_Woman_Smiling_v1.mp4` |

### Scene 05 (Outro)
| 항목 | 내용 |
| :--- | :--- |
| **씬 번호 / 길이** | Scene 05 / 3초 |
| **목표 메시지** | 브랜드 각인 및 캠페인 핵심 메시지 전달. |
| **화면 구성** | **구도:** 중앙 정렬 (제품 강조)<br>**피사체:** 물방울이 맺힌 향수병 단독 컷<br>**배경:** 비 온 뒤 맑게 갠 하늘과 싱그러운 나뭇잎<br>**텍스트:** [중앙 상단] 향기는 가장 선명한 타임머신이다. [중앙 하단] Scent of Archive |
| **내레이션/카피** | (화면 텍스트와 동일) |
| **사용 도구** | **Gemini 3.5 Pro	** (제품 배경 영상 생성), **Vrew** (최종 텍스트 레이아웃 및 렌더링) |
| **입력 프롬프트** | `Clear glass perfume bottle resting on a wet green leaf, bright clear sky after rain background, fresh and crisp atmosphere, premium commercial product videography, gentle breeze` |
| **출력 결과 요약** | 산들바람이 부는 청량한 배경 속, 물방울이 맺힌 향수병의 프리미엄 제품 영상. |
| **생성 결과 파일명** | `SC05_Product_Outro_v1.mp4` |

### 5. 최종 영상 요약
- 파일명: scent_of_archive_video_final.mp4
- 길이: 18초
- 해상도: 1920x1080
- 프레임레이트: 30fps