#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int gcd(int a, int b)
{
    if (b==0)
       return a;
    return gcd(b, a%b);
}
int main()
{
    int n,m;
    cin>>n>>m;
    int v[n];
    for(int i=0;i<n;i++)
        cin>>v[i];
    int max=0;
    sort(v,v+n,greater<int>());
    if(m==2 && n!=2){
        if(n<=1)
            cout<<v[0]/m;
        else{
            max=v[0]+v[1];
            cout<<max/2;
            }
    }
    else if(n==2){    
        max=v[0]+v[1];
        cout<<max/m;
        
        //if(gcd(v[0],v[1])!=0)
    }
    else{
        for(int i=0;i<m;i++)
            max+=v[i];
        cout<<max/m;
    }
    return 0;
    

}
