#include <iostream>
using namespace std;

void printStar(int n){
    for(int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            cout << "*";
        }
        printf("\n");
    }
}
int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n;
    scanf("%d",&n);
    printStar(n);
    return 0;
}

