# 부분집합을 구하는 재귀 함수 정의
def generate_subsets(idx):
    # [종료 조건] 모든 원소(N개)에 대해 포함 여부를 결정했을 때
    if idx == N:
        subset = [arr[i] for i in range(N) if selected[i]]
        print(subset)
        return

    # 1. idx번째 원소를 포함하는 경우
    selected[idx] = True
    generate_subsets(idx + 1)

    # 2. idx번째 원소를 포함하지 않는 경우
    selected[idx] = False
    generate_subsets(idx + 1)

# 사용 예시
arr = ['A', 'B', 'C']
N = len(arr)
selected = [False] * N  # 원소 포함 여부 체크 배열

# 0번 인덱스부터 결정 시작
generate_subsets(0)