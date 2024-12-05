#include<fstream>
using namespace std;
void add(int v[], int& dimensiune, int m, int k);
int remove(int v[], int& dimensiune);
void heapify(int v[],int curent,int dimensiune);
void reverseHeapify(int v[], int curent);
int main()
{
    ifstream reader("heap.in");
    ofstream writer("heap.out");
    int m;
    reader>>m;
    int op;
    int k;
    int v[m];
    int dimensiune=0;
    for(int i=0;i<m;i++){
        reader>>op;
        if(op==1){
            reader>>k;
            add(v,dimensiune,m,k);
        }
        else
            writer<<remove(v,dimensiune)<<'\n';
    }
    reader.close();
    writer.close();
    return 0;
}
void add(int v[], int& dimensiune, int m, int k){
    v[dimensiune]=k;
    reverseHeapify(v,dimensiune);
    dimensiune++;
}
int remove(int v[], int& dimensiune){
    int maxim=v[0];
    v[0]=v[dimensiune-1];
    dimensiune--;
    heapify(v,0,dimensiune);
    return maxim;
}
void heapify(int v[],int curent,int dimensiune){
    int aux;
    int indexStanga=curent*2+1;
    int indexDreapta=curent*2+2;
    int maxim=curent;
    if(indexStanga<dimensiune && v[indexStanga]>v[maxim])
        maxim=indexStanga;
    if(indexDreapta<dimensiune && v[indexDreapta]>v[maxim])
        maxim=indexDreapta;
    if(maxim!=curent){
        aux=v[maxim];
        v[maxim]=v[curent];
        v[curent]=aux;
        heapify(v,maxim,dimensiune);
    }
}
void reverseHeapify(int v[], int curent){
    if(curent==0)
        return;
    if(v[curent]>v[(curent-1)/2]){
        swap(v[curent],v[(curent-1)/2]);
        reverseHeapify(v,(curent-1)/2);
    }
}