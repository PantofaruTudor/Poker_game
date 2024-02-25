#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    char c[101];
    char s[101];
    cin.getline(s,101);
    cin.getline(c,101);
    char vFinal[strlen(c)]="";
    char v[strlen(c)*2]="";
    char par[]="02468";
    int m=strlen(c);
    int p=m-1;
    int np=m+1;
    if(strlen(s)!=strlen(c))
        cout<<"cod incorect";
    else{
        v[m]=s[0];
        for(int i=1;i<strlen(c);i++){
            if(strchr(par,c[i])!=NULL){
                v[p--]=s[i];
            }
            else
                v[np++]=s[i];
        }
    }

    for(int i=0;i<strlen(c)*2;i++)
        if(v[i]!='0')
            strcat(vFinal,v+i);
    cout<<vFinal<< " ";
    return 0;
    

}