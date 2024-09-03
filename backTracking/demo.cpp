#include <fstream>
#include <chrono>
#include <thread>
#include <iostream>
using namespace std;
const int DIM=9;
bool hasSolution(int** mat, int i, int j);
bool getEmpty(int** mat,int &ii, int &jj);
bool isLegal(int** mat, int i, int j);
bool getEmpty(int** mat,int &ii, int &jj);
bool isUniqueLine(int** mat, int i, int j);
bool isUniqueColumn(int** mat, int i, int j);
bool isUniqueSquare(int** mat, int i, int j);
int main()
{
    ifstream reader("sudoku.in");
    ofstream writer("sudoku.out");
    int** mat=new int*[DIM];
    for(int i=0;i<DIM;i++)
        mat[i]=new int[DIM];
    for(int i=0;i<DIM;i++)
        for(int j=0;j<DIM;j++)
            reader>>mat[i][j];
    if(hasSolution(mat,0,0))
        for(int i=0;i<DIM;i++)
        {
            for(int j=0;j<DIM;j++)
                writer<<mat[i][j]<<" ";
            writer<<endl;
        }
    for(int i=0;i<DIM;i++)
        delete[] mat[i];
    delete[] mat;
    reader.close();
    writer.close();
    return 0;
}
bool hasSolution(int** mat, int i, int j){
    this_thread::sleep_for(chrono::milliseconds(500));
    system("cls");
    for(int i=0;i<DIM;i++)
    {
        for(int j=0;j<DIM;j++)
            cout<<mat[i][j]<<" ";
        cout<<endl;

    }
    if(!getEmpty(mat,i,j)){
        
        return true;
    }
        
    for(int k=1;k<=DIM;k++)
    {
        mat[i][j]=k;
        if(isLegal(mat,i,j) && hasSolution(mat,i,j))
            return true;
        mat[i][j]=0;
    }
    return false;
}
bool getEmpty(int** mat,int &ii, int &jj)
{
    for(int i=ii;i<DIM;i++)
        for(int j=0;j<DIM;j++){
            if(mat[i][j]==0)
            {
                ii=i;
                jj=j;
                return true;
            }
        }
    return false; 
}
bool isLegal(int** mat, int i, int j){
    return isUniqueLine(mat,i,j) && isUniqueColumn(mat,i,j) && isUniqueSquare(mat,i,j);
}
bool isUniqueLine(int** mat, int i, int j){
    for(int k=0;k<DIM;k++)
        if(mat[i][j]==mat[i][k] && k!=j)
            return false;
    return true;   

}
bool isUniqueColumn(int** mat, int i, int j){
    for(int k=0;k<DIM;k++)
        if(mat[i][j]==mat[k][j] && k!=i)
            return false;
    return true;
}
bool isUniqueSquare(int** mat, int i, int j){
    int iS=(i/3)*3;
    int jS=(j/3)*3;
    for(int ii=iS;ii<iS+3;ii++)
        for(int jj=jS;jj<jS+3;jj++){
            if(mat[i][j]==mat[ii][jj] && (i!=ii || j!=jj))
                return false;
        }
    return true;
}
