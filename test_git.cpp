#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int v[n];
    for(int i=0;i<n;i++)
        cin>>v[i];
    int f[n][n];
    int jos;
    int sus;
    for(int i=0;i<n;i++){
        jos=n-1;
        sus=0;
        for(int j=0;j<n;j++){
            if(i%2==0)
                f[j][i]=v[jos--];
            else
                f[j][i]=v[sus++];
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)
            cout<<f[i][j]<<" ";
        cout<<endl;
        {
    return 0;
}