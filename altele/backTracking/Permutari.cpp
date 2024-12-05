#include<fstream>
using namespace std;
bool isLegal(int s[],int k);
void logan(int s[],int n,int k,ofstream& writer);
int main()
{
    ifstream reader("permutari.in");
    ofstream writer("permutari.out");
    int n;
    reader>>n;
    int s[n];
    logan(s,n,0,writer);
    reader.close();
    writer.close();
    return 0;
}
void logan(int s[],int n, int k, ofstream& writer)
{
    if(k==n){
        for(int i=0;i<n;i++)
            writer<<s[i]<<" ";
        writer<<endl;
        return;
    }
    for(int i=1;i<=n;i++){
        s[k]=i;
        if(isLegal(s,k))
            logan(s,n,k+1,writer);
    }
}
bool isLegal(int s[],int k){
    for(int i=0;i<k;i++)
        if(s[k]==s[i])
            return false;
    return true;

}