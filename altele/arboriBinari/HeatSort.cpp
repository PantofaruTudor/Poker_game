#include<fstream>
using namespace std;
void heapSort(int v[],int n);
void heapify(int v[],int curent,int dimensiune);
int main()
{
    ifstream reader("heap_sort.in");
    ofstream writer("heap_sort.out");
    int n;
    reader>>n;
    int* v=new int[n];
    for(int i=0;i<n;i++)
        reader>>v[i];
    heapSort(v,n);
    for(int i=0;i<n;i++)
        writer<<v[i]<<" ";
    delete[] v;
    reader.close();
    writer.close();
    return 0;
}
void heapSort(int v[],int n){
    for(int i=n/2-1;i>=0;i--)
        heapify(v,i,n);
    for(int i=n-1;i>=0;i--){
        swap(v[0],v[i]);
        heapify(v,0,i);
    }
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