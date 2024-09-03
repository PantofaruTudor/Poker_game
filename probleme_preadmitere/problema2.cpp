#include <bits/stdc++.h>
#include<cstring>
using namespace std;
int gcd(int a, int b)
{
    if (b==0)
       return a;
    return gcd(b, a%b);
}

int pour(int fromCap, int toCap, int d, char c[][20], int index)
{

    int from = fromCap;
    int to = 0;

    int step = 1;
    while (from != d && to != d)
    {

        int temp = min(from, toCap - to);
 
        to   += temp;
        from -= temp;
        strcpy(c[index++],"VARSA A IN B");
        cout<<"";

        step++;
 
        if (from == d || to == d)
            break;
 
        if (from == 0)
        {
            from = fromCap;
            strcpy(c[index++],"UMPLE A");
            step++;
        }

        if (to == toCap)
        {
            to = 0;
            strcpy(c[index++],"GOLESTE B");
            step++;
        }
    }
    return step;
}
 

int minSteps(int m, int n, int d, char c[][20], int index)
{

    if (m > n)
        swap(m, n);

    if (d > n)
        return -1;

    if ((d % gcd(n,m)) != 0)
        return -1;
 
    return min(pour(n,m,d,c,index),pour(m,n,d,c,index)); 
}
 

int main()
{
    int n,m,d;
    cin>>n>>m>>d;
    int step;
    int index=0;
    char aa[28]="ABCDEFGHIJKLMNOPRQSTUVWXYZ ";
    char c[100][20];
    for(int i=0;i<100;i++)
        for(int j=0;j<20;j++)
            c[i][j]='\0';
    if (minSteps(m,n,d,c,0)<0)
        cout<<"IMPOSIBIL";
    else{
        step=minSteps(m, n, d,c,0);
        cout<<step;
        for(int i=0;i<20;i++){
            if(strchr(aa,c[i][0])!=NULL)
                index++;
            else
                break;
        }
    }
    cout<<index<<'a';


    return 0;
}