#include <iostream>
using namespace std;

int main() {
  int count;
  cin >> count;

  for (int i = 1; i <= count; i++) {
    for (int j = 0; j < count - i; j++) {
      cout << " ";
    }
    for (int j = 0; j < i * 2 - 1; j++) {
      cout << "*";
    }
    cout << endl;
  }
}