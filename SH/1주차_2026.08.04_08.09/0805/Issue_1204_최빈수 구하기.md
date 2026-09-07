## 💡 깃허브 이슈(Issue) 작성 가이드 & 템플릿

깃허브 이슈 게시판은 혼자 공부한 기록을 남기거나, 팀 프로젝트에서 문제 해결 과정을 공유하는 아주 좋은 공간입니다. 코딩 테스트(SWEA) 풀이와 어려웠던 점을 기록할 때는 "무엇을 풀었고, 어떤 에러를 만났으며, 어떻게 해결했는가"가 한눈에 보이도록 작성하는 것이 좋습니다.

---

### 📋 추천하는 이슈 작성 형식 (마크다운 템플릿)

이슈를 생성할 때 아래의 형식을 복사해서 내용만 채워 넣으시면 깔끔하게 정리됩니다.


## 📌 문제 정보
- **플랫폼:** SW Expert Academy (SWEA)
- **문제 번호/이름:** 1204번 - 최빈수 구하기
- **난이도:** D2

---

## 💻 제출 코드
```python
# Raw_data를 가져오기
T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    scores = list(map(int, input().split()))

# for문을 활용해 성적들을 하나씩 출력하고 딕셔너리에 점수별 개수를 측정
    score_counts = {}
    for score in scores:
        if score in score_counts:
            score_counts[score] += 1
        else:
            score_counts[score] = 1

# for문을 활용해 딕셔너리의 개수를 하나씩 출력하고 가장 높은 개수의 키 값을 출력
    max_score_1 = 0
    max_score_2 = 0

    for score, count in score_counts.items():
        if count > max_score_1:
            max_score_1 = count
            max_score_2 = score
        elif count == max_score_1:
            if score > max_score_2:
                max_score_2 = score

    print(f"#{num} {max_score_2}")

```

---

## 🔥 어려웠던 점 & 트러블 슈팅 (Troubleshooting)

1. **문제 상황 / 고민:**
* 알고리즘을 푸는 것이 처음이다 보니 모든게 낯설었음.
* 문제 구상은 파이썬 월간평가 공부했던 것이 많은 도움이 되었지만 아직 익숙하지 않아 많은 공부가 필요함을 느낌.
* 데이터를 불러오고 활용하는 방법을 몰라 처음에 시간을 허비함.
* 오타로 인해 결과가 출력이 안돼 당황했음.


2. **원인 분석:**
* SWEA 문제 제출 부부을 제대로 안봄.
* 자동완성을 이용해야했지만 일일이 치는 버릇때문에 오타가 발생함.



3. **해결 방법:**
* 데이터를 불러오는 방법은 혜강이의 도움으로 해결함.
* 데이터를 활용할 수 있도록 바꾸는 코드인 "scores = list(map(int, input().split()))"은 AI의 도움을 받음.



---

## 💡 배운 점 / 느낀 점

* 파이썬 월간평가 공부했던 것 덕분에 빈도수를 구하는 알고리즘은 시간은 오래 걸렸지만 결국 해냈음. 다만, 아직 알고리즘 푸는 것이 익숙하지 않아 많은 공부가 필요함을 느낌.

```

---

### 🚀 깃허브에 올리는 방법 (순서)

1. **저장소(Repository) 이동:** 본인의 알고리즘 공부용 깃허브 저장소로 들어갑니다.
2. **Issues 탭 클릭:** 상단 메뉴에 있는 **`Issues`** 탭을 클릭합니다.
3. **New issue 클릭:** 초록색 **`New issue`** 버튼을 누릅니다.
4. **제목 작성:** 직관적으로 알아볼 수 있게 작성합니다.
   * *예시: `[SWEA] D2 1204번 - 최빈수 구하기 풀이 및 트러블 슈팅`*
5. **내용 작성:** 위에서 제공한 템플릿을 붙여넣고 본인의 생각이나 추가하고 싶은 내용을 적습니다.
6. **라벨(Labels) 부착 (선택):** 우측 메뉴에서 `algorithm`, `python`, `trouble-shooting` 같은 라벨을 붙여주면 나중에 모아보기 편합니다.
7. **Submit new issue 클릭:** 완료 버튼을 누르면 등록됩니다!