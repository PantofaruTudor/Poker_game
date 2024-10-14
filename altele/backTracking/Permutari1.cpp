#include<fstream>
#include<iostream>
using namespace std;
bool legal(int n,int s[]);
void BackTracking(int n,int s[],int k,ofstream& writer);
int main()
{
    ifstream reader("permutari1.in");
    ofstream writer("permutari1.out");
    int n; 
    reader>>n;
    int s[n];
    BackTracking(n,s,0,writer);
    reader.close();
    writer.close();
    return 0;
}
void BackTracking(int n, int s[],int k,ofstream& writer){
    if(k==n){
        for(int i=0;i<n;i++)
            writer<<s[i]<<" ";
        writer<<endl;
        return;
    }
    for(int i=n;i>=1;i--){
        s[k]=i;
        if(legal(k,s))
            BackTracking(n,s,k+1,writer);
    }
}
bool legal(int k,int s[]){
    for(int i=0;i<k;i++)
        if(s[k]==s[i])
            return false;
    return true;
}