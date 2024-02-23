#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ofstream writer("bac.txt");
    int x;
    int y;
    cin>>x>>y;
    int z=2*x-y+2;
    writer<<y<<" "<<x<<" "<<z<<" ";
    while(z!=0){
        y=x;
        x=z;
        z=2*x-y+2;
        writer<<z<<" ";
    }
    writer.close();
    return 0;
}