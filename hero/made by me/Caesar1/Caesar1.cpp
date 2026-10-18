#include <iostream>
#include <string>
using namespace std;

int main() {

    int T;
    cin >> T;

    for (int testCase = 1; testCase <= T; testCase++) {

        int N;          // 한 단어의 글자 수
        string S;       // 해독해야 하는 암호문

        cin >> N;
        cin >> S;

        string result = "";

        // 암호문을 앞에서부터 한 글자씩 확인
        for (int i = 0; i < S.length(); i++) {

            // 알파벳을 숫자로 변환
            // A = 0, B = 1, C = 2, Z = 25
            int num = S[i] - 'A';

            // 문자열의 인덱스는 0부터 시작하지만
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

                // C++에서는 음수에 % 연산을 하면
                // 결과가 음수가 될 수 있다.
                // 따라서 음수라면 26을 더해서
                // 다시 0부터 25 사이의 값으로 만든다.
                if (num < 0) {
                    num += 26;
                }
            }

            // 계산한 숫자를 다시 알파벳으로 변환
            char decoded = 'A' + num;

            // 해독된 문자를 result에 추가
            result += decoded;
        }

        // result에는 공백이 없는 원래 문장이 저장되어 있다.
        // 예를 들어 YOUCANWIN과 같은 형태이다.

        string answer = "";

        // 해독된 문자열을 N글자씩 자른다.
        // N이 3이라면 0, 3, 6과 같은 위치에서 시작한다.
        for (int i = 0; i < result.length(); i += N) {

            // 첫 번째 단어가 아니라면 앞에 공백을 추가한다.
            if (!answer.empty()) {
                answer += " ";
            }

            // 현재 위치부터 N글자를 잘라서 추가한다.
            // substr(시작 위치, 가져올 글자 수)
            //
            // 예를 들어 N이 3이고 YOUCANWIN이라면
            // YOU, CAN, WIN으로 나누어진다.
            answer += result.substr(i, N);
        }

        // 테스트 케이스 번호와 해독된 문장을 출력
        cout << "#" << testCase << " " << answer << '\n';
    }

    return 0;
}
