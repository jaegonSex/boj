#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
#include <set>

using namespace std;
vector<vector<int>> adj;

bool isVowel(char c) {
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}
void combinationRec(vector<char> &chars, int size, int index, vector<vector<char>> &result, vector<char> &tmp) {
    if (size == 0) {
        vector<char> t;
        t.assign(tmp.begin(), tmp.end());
        result.push_back(t);
        return;
    }
    if (index >= chars.size()) {
        return;
    }
    tmp.push_back(chars[index]);
    combinationRec(chars, size - 1, index + 1, result, tmp);
    tmp.pop_back();
    combinationRec(chars, size, index + 1, result, tmp);
}


vector<vector<char>> combination(vector<char> &chars, int size) {
    vector<vector<char>> result;
    vector<char> tmp;
    combinationRec(chars, size, 0, result, tmp);

    return result;
}

bool isValid(vector<char> &password) {
    int vowelCount = 0;
    for (int i = 0; i < password.size(); ++i) {
        if (isVowel(password[i])) ++vowelCount;
    }
    int consonantCount = password.size() - vowelCount;
    return vowelCount >= 1 && consonantCount >= 2;
}

int main() {
    int l, c;
    cin >> l >> c;
    vector<char> chars(c);
    for (int i = 0; i < c; ++i) {
        cin >> chars[i];
    }
    sort(chars.begin(), chars.end());


    vector<vector<char>> passwords = combination(chars, l);
    for (auto password: passwords) {
        if (isValid(password)){
            for (int i = 0; i < password.size(); ++i) {
                cout << password[i];
            }
            cout<<'\n';
        }
    }

}


