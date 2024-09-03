#include<iostream>
using namespace std;
struct Nod{
    int val;
    Nod* stanga=NULL;
    Nod* dreapta=NULL;
};
void add(Nod*& curent,int x);
void preordineRSD(Nod* curent);
void ordineSRD(Nod* curent);
void postordineSDR(Nod* curent);
void sterge(Nod*& curent);
int main()
{
    Nod* radacina=NULL;
    add(radacina,6);
    add(radacina,7);
    add(radacina,3);
    add(radacina,4);
    add(radacina,1);
    add(radacina,2);
    add(radacina,10);
    add(radacina,8);
    add(radacina,11);
    add(radacina,14);
    //preordineRSD(radacina);
    //ordineSRD(radacina);
    //postordineSDR(radacina);
    sterge(radacina);

}
void add(Nod*& curent,int x){
    Nod* nou=new Nod;
    nou->val=x; //val din stanga diferit de val din dreapta
    if(curent==NULL){
        curent=nou;
        return;
    }
    if(x>curent->val)
        add(curent->dreapta,x);
    else
        add(curent->stanga,x);

        
}
void preordineRSD(Nod* curent){
    if(curent==NULL)
        return;
    cout<<curent->val<<" ";
    preordineRSD(curent->stanga);
    preordineRSD(curent->dreapta);
}
void ordineSRD(Nod* curent){
    if(curent==NULL)
        return;
    ordineSRD(curent->stanga);
    cout<<curent->val<<" ";
    ordineSRD(curent->dreapta); 
}
void postordineSDR(Nod* curent){
    if(curent==NULL)
        return;
    postordineSDR(curent->stanga);
    postordineSDR(curent->dreapta);
    cout<<curent->val<<" ";
}
void sterge(Nod*& curent){
    if(curent==NULL)
        return;
    sterge(curent->stanga);
    sterge(curent->dreapta);
    delete curent;
    curent=NULL;
}

