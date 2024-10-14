#include <iostream>
using namespace std;
bool isLegal(int s[],int k);
void logan(int s[],int n,int a,int b,int k);
int main()
{
    int a;
    int b;
    cin>>a;
    cin>>b;
    int n=b-a+1;
    int s[n];
    logan(s,n,a,b,0);
    return 0;
}
void logan(int s[],int n,int a,int b,int k){
    if(n==k){
        for(int i=0;i<n;i++)
            cout<<s[i]<<" ";
        cout<<endl;
        return;
    }
    for(int i=a;i<=b;i++){
        s[k]=i;
        if(isLegal(s,k))
            logan(s,n,a,b,k+1);
    }
}
bool isLegal(int s[],int k){
    for(int i=0;i<k;i++)
        if(s[i]==s[k])
            return false;
    return true;
}

    