#include<fstream>
#include<cstring>
using namespace std;
struct Nod{
    int val;
    Nod* stanga=NULL;
    Nod* dreapta=NULL;
};
void parcurgere(Nod* radacina, ofstream& writer);
int main()
{
    ifstream reader("problema1.in");
    ofstream writer("problema1.out");
    int n;
    reader>>n;
    Nod v[n];
    int a;
    int b;
    int nod;
    int tati[n];
    memset(tati,-1,4*n);
    for(int i=0;i<n;i++){
        reader>>nod>>a>>b;
        a--;
        b--;
        nod--;
        v[nod].val=nod;
        if(a!=-1){
            v[nod].stanga=&v[a];
            tati[a]=nod;
        }
        if(b!=-1){
            v[nod].dreapta=&v[b];
            tati[b]=nod;
        }
    }
    Nod* radacina;
    for(int i=0;i<n;i++){
        if(tati[i]==-1)
            radacina=&v[i];
    };
    parcurgere(radacina,writer);
    reader.close();
    writer.close();
    return 0;
}
void parcurgere(Nod* radacina, ofstream& writer){
    if(radacina==NULL)
        return;
    if(radacina->stanga==NULL && radacina->dreapta==NULL)
        writer<<radacina->val<<" ";
    parcurgere(radacina->stanga, writer);
    parcurgere(radacina->dreapta,writer);
}