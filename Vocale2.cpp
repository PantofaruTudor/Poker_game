#include <iostream>
#include <cstring>
using namespace std;
const int DIM=256;
int main()
{
    int delta='a'-'A';
    char v[256];
    char vocale[]="aeiou";
    cin.getline(v,256);
    for(int i=0;i<strlen(v);i++)
        if(strchr(vocale,v[i]))
            v[i]-=delta;
    cout<<v;
            
    return 0;
}