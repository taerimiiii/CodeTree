#include <iostream>
#include <deque>
using namespace std;

int main() {
    // Please write your code here.
    int N, i;
    string cmd[10000];
    int num[10000];
    deque<int> dq;

    cin >> N;

    for (i = 0; i < N; i++) {
        cin >> cmd[i];
        if (cmd[i] == "push_front") {
            cin >> num[i];
            dq.push_front(num[i]);
        }
        else if (cmd[i] == "push_back") {
            cin >> num[i];
            dq.push_back(num[i]);
        }
        else if (cmd[i] == "pop_front") {
            cout << dq.front() << "\n";
            dq.pop_front();
        }
        else if (cmd[i] == "pop_back") {
            cout << dq.back() << "\n";
            dq.pop_back();
        }
        else if (cmd[i] == "size") {
            cout << dq.size() << "\n";
        }
        else if (cmd[i] == "empty") {
            if (dq.empty()) {
                cout << "1\n";
            }
            else {
                cout <<"0\n";
            }
        }
        else if (cmd[i] == "front") {
            cout << dq.front() << "\n";
        }
        else {
            cout << dq.back() << "\n";
        }
    }

    return 0;
}