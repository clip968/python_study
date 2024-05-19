#include<bits/stdc++.h>
using namespace std;

pair<vector<string>, bool> combine(vector<string> &arr) {
    set<string> answer, used_chk;
    int cnt, index;
    string s;
    bool chk = false;
    for (int i = 0; i < arr.size(); ++i) {
        for (int j = i + 1; j < arr.size(); ++j) {
            cnt = 0;
            for (int k = 0; k < arr[i].size(); ++k) {
                if (arr[i][k] != arr[j][k]) {
                    ++cnt;
                    index = k;
                }
            }
            if (cnt != 1) continue;
            // combine
            chk = true;
            s = arr[i];
            s[index] = '-';
            answer.insert(s);
            used_chk.insert(arr[i]);
            used_chk.insert(arr[j]);
        }
    }
    // 선택받지 못한 애들 마저 넣기
    for (int i = 0; i < arr.size(); ++i) {
        if (used_chk.find(arr[i]) == used_chk.end()) answer.insert(arr[i]);
    }
    return{ vector<string>(answer.begin(), answer.end()), chk };
}

bool answer_cmp(const string& a, const string& b) {
    for (int i = 0; i < min(a.size(), b.size()); ++i) {
        char ac = (a[i] == '-') ? '2' : a[i];  // '-'을 '2'로 처리
        char bc = (b[i] == '-') ? '2' : b[i];
        if (ac != bc) {
            return ac < bc;
        }
    }
    return false; // 같은 문자열임
}

bool chk_cover(string& a, string& b) {
    for (int i = 0; i < a.size(); ++i) {
        if (b[i] != '-' && a[i] != b[i]) return false;
    }
    return true;
}

vector<string> solution(vector<int> minterm) {
    // 2진 str로 변환
    vector<string> implicants, minterms;
    string s;
    for (int i = 2; i < minterm.size(); ++i) {
        s = "";
        for (int j = minterm[0] - 1; j >= 0; --j) {
            if (minterm[i] >= (1 << j)) {
                minterm[i] -= 1 << j;
                s.append("1");
            }
            else s.append("0");
        }
        implicants.push_back(s);
        minterms.push_back(s);
    }
    // 더이상 확장 안될때 까지 combine
    pair<vector<string>, bool> tmp;
    vector<string> answer;
    tmp.first = implicants;
    do {
        tmp = combine(tmp.first);
    } while (tmp.second);
    answer = tmp.first;
    sort(answer.begin(), answer.end(), answer_cmp);
    // epi 찾기
    set<int> epi;
    vector<int> epi_tmp;
    for (int i = 0; i < minterms.size(); ++i) {
        epi_tmp.clear();
        for (int j = 0; j < answer.size(); ++j) {
            if (chk_cover(minterms[i], answer[j])) {
                epi_tmp.push_back(j);
            }
        }
        if (epi_tmp.size() == 1) epi.insert(epi_tmp[0]);
    }
    answer.push_back("EPI");
    for (set<int>::iterator it = epi.begin(); it != epi.end(); ++it) {
        answer.push_back(answer[*it]);
    }
    return answer;
}