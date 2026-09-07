## 💡 깃허브 이슈(Issue) 작성 가이드 & 템플릿

깃허브 이슈 게시판은 혼자 공부한 기록을 남기거나, 팀 프로젝트에서 문제 해결 과정을 공유하는 아주 좋은 공간입니다. 코딩 테스트(SWEA) 풀이와 어려웠던 점을 기록할 때는 "무엇을 풀었고, 어떤 에러를 만났으며, 어떻게 해결했는가"가 한눈에 보이도록 작성하는 것이 좋습니다.

---

### 📋 추천하는 이슈 작성 형식 (마크다운 템플릿)

이슈를 생성할 때 아래의 형식을 복사해서 내용만 채워 넣으시면 깔끔하게 정리됩니다.


## 📌 문제 정보
- **플랫폼:** SW Expert Academy (SWEA)
- **문제 번호/이름:** 1974번 - 스도쿠 검증
- **난이도:** D2

---

## 💻 제출 코드
```python
# 10개의 스도쿠 게임 만듬
T = int(input())
for test_case in range(1, T + 1):
    puzzle = []
    for i in range(9):
        raw_data = list(map(int, input().split()))
        puzzle.append(raw_data)

    result = 1

# 가로열 검증
    for row in puzzle:
        row_nums = []
        for num in row:
            if num in row_nums:
                result = 0
                break
            else:
                row_nums.append(num)


# 세로열 검증
    if result == 1:
        for c in range(9):
            col_nums = []
            for r in range(9):
                column_num = puzzle[r][c]
                if column_num in col_nums:
                    result = 0
                    break
                else:
                    col_nums.append(column_num)


# 3x3 범위 검증
    if result == 1:
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box_nums = []
                for i in range(3):
                    for j in range(3):
                        num = puzzle[r + i][c + j]
                        if num in box_nums:
                            result = 0
                            break
                        else:
                            box_nums.append(num)


    print(f"#{test_case} {result}")

```

---

## 🔥 어려웠던 점 & 트러블 슈팅 (Troubleshooting)

1. **문제 상황 / 고민:**
* 문제 구상은 했지만, 문제 풀이과정에서 3x3범위를 어떻게 검증해야하는지 생각을 못함.
* 결과 출력 단계에서 검증 성공 시 1, 실패 시 0을 출력하는 부분에서 방향을 잡지 못함.


2. **원인 분석:**
* 반복문으로 범위 지정을 하는 법을 몰랐음.
* if 문으로 처음 시도했지만 결과가 잘나오지 못해 AI 도움을 받음.


3. **해결 방법:**
* AI도움으로 문제를 풀었고 강사님이 설명해주셔서 이해할 수 있었음.
* AI의 도움으로 기존 result 값에 1을 할당하고 검증 실패 시 0을 재할당하는 방법으로 해결.



---

## 💡 배운 점 / 느낀 점

* 중첩 행렬에 대해 처음 배웠고 아직 익숙하지 않지만 원리를 이해함
* 

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