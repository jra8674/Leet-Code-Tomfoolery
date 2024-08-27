#include <iostream>

using namespace std;

//Define Function
int sumOfMultiples(int n){
    int out = 0;
    for ( int i = 1; i < n+1; i++){
        if (i % 3 == 0){
            out += i;
        }
        else if (i % 5 == 0){
            out += i;
        }
        else if (i % 7 == 0){
            out += i;
        }
    }
    return out;

}

//Run Scenarios
int main(){
    cout << sumOfMultiples(7) << endl;
    cout << sumOfMultiples(10) << endl;
    cout << sumOfMultiples(9);
}
