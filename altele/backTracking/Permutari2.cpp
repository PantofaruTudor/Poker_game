#include<fstream>
#include<iostream>
#include<algorithm>
using namespace std;
bool legal(int k,int s[]);
void print(int s[],int n,ofstream& writer,int v[]);
int main()
{
    ifstream reader("permutari2.in");
    ofstream writer("permutari2.out");
    int n;
    reader>>n;
    int v[n];
    int s[n];
    for(int i=0;i<n;i++)
        reader>>v[i];
    int aux=0;
    // for(int j=0;j<n;j++)
    //     for(int i=0;i<n-1-j;i++){
    //         if(v[i]>v[i+1])
    //         {
    //             aux=v[i];
    //             v[i]=v[i+1];
    //             v[i+1]=aux;
    //         }
    //     }
    sort(v,v+n);
    int k=0;
    int i;
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
}
bool legal(int k,int s[]){
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