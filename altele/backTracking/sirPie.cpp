#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
bool legal(int k,int s[]);
void print(int s[],int n,ofstream& writer,int v[]);
int cmmdc(int a,int b);
int main()
{
    ifstream reader("sirpie.in");
    ofstream writer("sirpie.out");
    int n;
    reader>>n;
    int v[n];
    int s[n];
    int k=0;
    for(int i=0;i<n;i++)
        reader>>v[i];
    sort(v,v+n);
    s[k]=-1;
    while(k>-1){
        while(s[k]<n-1){
            s[k]++;
            if(legal(k,s)){
                if(k==n-1)
                    print(s,n,writer,v);
                else
                    s[++k]=-1;
            }
            
        }
        k--;
    }
    reader.close();
    writer.close();
    return 0;
}
bool legal(int k,int s[]){
    if(k==0)
        return true;
    if(cmmdc(s[k],s[k-1])!=1)
        return false;
    for(int i=0;i<k;i++)
        if(s[k]==s[i])
            return false;
    return true;
}
void print(int s[],int n,ofstream& writer,int v[]){
    for(int i=0;i<n;i++)
        writer<<v[s[i]]<<" ";
    writer<<endl;
}
int cmmdc(int a,int b){
    if(b==0)
        return a;
    return cmmdc(b,a%b);
}