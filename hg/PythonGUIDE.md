
# Python 코딩 테스트 및 SWEA IM 프로젝트 가이드

이 문서는 파이썬(Python)을 사용하여 알고리즘 문제 및 SWEA IM 시험을 대비할 때 사용하는 작업 가이드 및 표준 템플릿 문서이다.

---

## 1. 프로젝트 구조 및 실행 방법

로컬 환경(VS Code, PyCharm 등)에서 `input.txt`를 활용해 입력을 테스트하고 온라인 저지에 제출한다.

```text
STUDY_PROJECT/
├─ .gitignore
├─ GUIDE.md
├─ input.txt            # 로컬 테스트용 입력 파일
├─ solution.py          # 현재 문제 풀이 파일
└─ README.md

```

### 로컬 실행 방법 (PowerShell / Terminal)

`input.txt`에 문제의 예제 입력을 넣어두고 아래 명령어로 실행하여 결과를 확인한다.

```powershell
# Windows PowerShell
Get-Content input.txt | python solution.py

# Bash / Mac Terminal
python solution.py < input.txt

```

---

## 2. 저지별 제출 규칙

| 사이트 | 제출 파일/함수 형식 | 출력 형식 |
| --- | --- | --- |
| **SWEA** | 전체 코드 제출 (`solution.py` 전체) | `#테스트케이스번호 정답` (예: `#1 71`) |
| **백준** | 전체 코드 제출 | 문제에서 요구하는 값만 출력 |
| **프로그래머스** | `def solution(...):` 함수 형태로 제출 | `return` 값으로 정답 제출 |

* 파이썬 제출 시 표준 라이브러리(`sys`, `collections`, `math` 등) 외 외부 패키지(`numpy`, `pandas` 등) 사용 금지.

---

## 3. SWEA IM 필수 파이썬 표준 템플릿

SWEA 특유의 여러 테스트 케이스 입력 구조와 런타임 에러(입력 형태 미스매치)를 완벽하게 방지하는 표준 템플릿이다.

```python
import sys

def solve():
    # 전체 입력을 한 번에 읽어 공백/줄바꿈 기준으로 분할
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # 첫 번째 값은 테스트 케이스 개수 T
    T = int(input_data[0])
    idx = 1

    for tc in range(1, T + 1):
        # 1. 입력 데이터 바인딩 (예시: N, M 입력)
        N = int(input_data[idx]); idx += 1
        M = int(input_data[idx]); idx += 1

        # 2. 2차원 격자 입력 받기 (N x M)
        grid = []
        for _ in range(N):
            row = []
            for _ in range(M):
                row.append(int(input_data[idx]))
                idx += 1
            grid.append(row)

        # 3. 문제 풀이 로직 수행
        answer = 0

        # 4. 정답 출력 (SWEA 형식)
        print(f"#{tc} {answer}")

if __name__ == "__main__":
    solve()

```

---

## 4. IM 대비 2차원 배열 & 델타 탐색 테크닉

SWEA IM 시험의 90% 이상을 차지하는 격자 조작 스니펫이다.

### ① 2차원 리스트 0으로 초기화 (방문/영역 표시용)

```python
# N x M 크기의 0 리스트 (주의: [[0]*M]*N 금지)
visited = [[0] * M for _ in range(N)]

```

### ② 상하좌우 4방향 델타 탐색

```python
# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# (r, c) 좌표에서 4방향 인접 칸 탐색
for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]

    # 격자 범위(Boundary) 체크 필수!
    if 0 <= nr < N and 0 <= nc < M:
        # 조건에 맞는 로직 수행
        pass

```

---

## 5. 문제 풀이 순서

1. **제약 사항 확인**: $N$의 크기를 보고 허용 가능한 시간 복잡도($O(N)$, $O(N^2)$ 등)를 계산한다.
2. **손으로 예제 풀기**: 입력 예시를 종이나 메모장에 직접 그리며 알고리즘 흐름을 정립한다.
3. **상태 초기화**: 각 테스트 케이스(`tc`)마다 사용되는 변수와 리스트가 초기화되었는지 확인한다.
4. **경계값 검증**: $N=1$이거나 리스트의 시작/끝 인덱스 참조 시 범위를 벗어나지 않는지 확인한다.
5. **디버깅**: `print(grid)` 등으로 중간 과정의 배열 상태를 출력하여 검증한다. (제출 전 삭제)

---

## 6. 필수 테스트 케이스 검증 목록

* [ ] $N=1$ 또는 배열 크기가 최소인 경우
* [ ] 격자의 모서리(0, 0) 및 경계 끝점에 위치한 데이터 처리
* [ ] 조건에 해당하는 값이 전혀 없는 경우 (예: 최빈수/최댓값이 모두 0인 경우)
* [ ] 동점/동일 값이 여러 개 발생하는 경우 (예: 최빈수가 여러 개일 때 큰 점수 선택)

---

## 7. 제출 전 최종 체크리스트

* [ ] 디버깅용 `print()` 문을 모두 제거했는가?
* [ ] 테스트 케이스 반복문 내에서 배열 및 변수가 매번 정상 초기화되는가?
* [ ] SWEA 출력 포맷(`f"#{tc} {answer}"`)을 준수했는가?
* [ ] 2차원 배열 인덱스 참조 시 `[행][열]` (`[row][col]`) 순서를 올바르게 썼는가?

```

```