#include <iostream>

using namespace std;

int sum(int a, int b); // prototype 

int sum(int a, int b) {
     return a + b;
}

int main() {
    int a = 5;
    int b = 5;
    int result = sum(a,b);
    cout << result << endl;
    return 0;
}
    