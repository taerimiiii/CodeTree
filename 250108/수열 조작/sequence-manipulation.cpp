#include <iostream>
#include <queue>

using namespace std;

int main() {
    // Please write your code here.
    int N, i;
    queue<int> q;

    cin >> N;

    for (i = 1; i <= N; i++) {
        q.push(i);
    }

    while (q.size() > 1) {
        q.pop();
        q.push(q.front());
        q.pop();
    }

    cout << q.front();

    return 0;
}