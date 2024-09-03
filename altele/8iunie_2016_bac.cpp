//SUB 3 EX 3
/*
#include<iostream>
using namespace std;
int cifreImpare(int n);
int main()
{
    int n;
    cin>>n;
    cout<<cifreImpare(n);
    return 0;
}
int cifreImpare(int n){
    int contorP=0;
    int contorI=0;
    int v[9];
    int i=0;
    int nr=0;
    while(n!=0){
        if((n%10)%2==0){
            v[i++]=n%10;
            contorP++;
        }
        else
            contorI++;
        n/=10;
    }
    if(contorP==0 || contorI==0)
        return -1;
    else{
        for(int i=contorP-1;i>=0;i--){
            nr=nr*10+v[i];
        }
    }
    return nr;

}*/

//SUB 3 EX 4
#include<iostream>
using namespace std;
int main()
{
    
}