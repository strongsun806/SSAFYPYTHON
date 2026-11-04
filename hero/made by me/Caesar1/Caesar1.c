#include <stdio.h>
#include <string.h>

int main() {

    int T;
    scanf("%d", &T);

    for (int testCase = 1; testCase <= T; testCase++) {

        int N;                  // 한 단어의 글자 수
        char S[10001];          // 해독해야 하는 암호문
        char result[10001];     // 해독된 문자열을 저장할 배열

        scanf("%d", &N);
        scanf("%s", S);

        int length = strlen(S);

        // 암호문을 앞에서부터 한 글자씩 확인
        for (int i = 0; i < length; i++) {

            // 알파벳을 숫자로 변환
            // A = 0, B = 1, C = 2, Z = 25
            int num = S[i] - 'A';

            // 배열의 인덱스는 0부터 시작하지만
            // 문제에서 문자의 위치는 1부터 시작한다.
            // 따라서 현재 문자의 위치는 i + 1이다.
            int position = i + 1;

            // 홀수 번째 문자는 오른쪽으로 이동
            // 1번째는 1칸
            // 3번째는 3칸
            // 5번째는 5칸
            if (position % 2 == 1) {
                num = (num + position) % 26;
            }

            // 짝수 번째 문자는 왼쪽으로 이동
            // 2번째는 2칸
            // 4번째는 4칸
            // 6번째는 6칸
            else {
                num = (num - position) % 26;

                // C에서는 음수에 % 연산을 하면
                // 결과가 음수가 될 수 있다.
                // 따라서 음수라면 26을 더해서
                // 다시 0부터 25 사이의 값으로 만든다.
                if (num < 0) {
                    num += 26;
                }
            }

            // 계산한 숫자를 다시 알파벳으로 변환해서 저장
            result[i] = 'A' + num;
        }

        // C 문자열의 마지막에는
        // 문자열의 끝을 나타내는 널 문자가 필요하다.
        result[length] = '\0';

        // 테스트 케이스 번호 출력
        printf("#%d ", testCase);

        // 해독된 문자열을 앞에서부터 출력한다.
        for (int i = 0; i < length; i++) {

            // 첫 번째 글자가 아니면서
            // N글자 단위의 새로운 단어가 시작되는 위치라면
            // 먼저 공백을 하나 출력한다.
            //
            // 예를 들어 N이 3이라면
            // i가 3, 6, 9일 때 공백을 추가한다.
            if (i > 0 && i % N == 0) {
                printf(" ");
            }

            // 현재 글자 출력
            printf("%c", result[i]);
        }

        // 하나의 테스트 케이스가 끝나면 줄바꿈
        printf("\n");
    }

    return 0;
}
