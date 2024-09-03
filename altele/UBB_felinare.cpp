#include<iostream>
using namespace std;
struct felinare{
    int pc;
    int uc;
    int p;
};
int cautare(int sp1, int sp2, int sp3, int sp4, felinare v[]);
int main()
{
    int n;
    cin>>n;
    felinare v[n];
    int putere;
    int rez;
    for(int i=0;i<n;i++){
        cin>>putere;
        v[i].pc=i-putere;
        v[i].uc=i+putere;
        if(v[i].pc<0)
            v[i].pc=0;
        if(v[i].uc>n)
            v[i].uc=n;
        v[i].p=putere;
    }
    rez=cautare(0,n/2,n/2,n,v);
    cout<<rez;
    return 0;
   
}
int cautare(int sp1, int sp2, int sp3, int sp4,felinare v[]){
    if(sp2==0)
        return 0;
    int suma;
    
     
}
/*
int main()
{
    int n;
    cin>>n;
    int v[n];
    for(int i=0;i<n;i++)
        cin>>v[i];
    felinare v2[n];
    int sum=0;
    int p1,p2;
    for(int i=0;i<n;i++){
        v2[i].pc=i-v[i];
        if(v2[i].pc<0)
            v2[i].pc=0;
        v2[i].uc=v[i]+i;
        if(v2[i].uc>n-1)
            v2[i].uc=n-1;
        v2[i].suma=v2[i].uc-v2[i].pc+1;
        if(v2[i].suma>sum){
            p1=v2[i].pc;
            p2=v2[i].uc;
        }   
    }
    cautare(0,p1,p2,n-1);
    return 0;
}*/
