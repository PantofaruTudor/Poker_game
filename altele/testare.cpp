#include<bits/stdc++.h>
#include<cstring>
using namespace std;
int main()
{
    int c=0;
    char s[21];
    int i=0;
    for(i;i<=10;i++){
        cin>>s;
        char voc[6]="aeiou";
        char con[22]="bcdfghjklmnpqrstvwxyz";
        if(strlen(s)==2){
            if(strchr(voc,s[0])!=NULL){
                if(strchr(con,s[1])!=NULL)
                    c=1;
            }
            else if(strchr(con,s[0])!=NULL)
                if(strchr(voc,s[1])!=NULL)
                    c=1;
        }
    }
    cout<<c;
    return 0;
}