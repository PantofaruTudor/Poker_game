#include<fstream>
using namespace std;
int main()
{
    ifstream reader("complet.in");
    ofstream writer("complet.out");
    int n;
    reader>>n;
    int v[n];
    for(int i=0;i<n;i++)
        reader>>v[i];
    int m;
    reader>>m;
    int op;
    int k;
    int sum;
    for(int i=0;i<m;i++){
        reader>>op;
        reader>>k;
        k--;
        if(op==1){
            if(k!=0)
                writer<<v[(k-1)/2];
            else
                writer<<0;
        }
        else{
            sum=0;
            if(k*2+1<n)
                sum+=v[k*2+1];
            if(k*2+2<n)
                sum+=v[k*2+2];
            writer<<sum;
        }
            
        writer<<'\n';
    }
    reader.close();
    writer.close();
    return 0;
}