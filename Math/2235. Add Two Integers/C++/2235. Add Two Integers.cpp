#include <iostream>

using namespace std;

int sum(int num1, int num2){
    int x = num1 + num2;
    return x;
}

int main(){
    cout << sum(12,5) <<endl;
    cout << sum(-10,4);
}
