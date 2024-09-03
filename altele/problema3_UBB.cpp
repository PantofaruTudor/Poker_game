#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream reader("problema3.txt");
    long long int A,B;
    long long int S;
    reader>>A>>B;
    S=A/B;
    cout<<S;
    return 0;
}