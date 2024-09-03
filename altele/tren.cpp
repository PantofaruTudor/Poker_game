#include<iostream>
#include<algorithm>


using namespace std;

struct Muchie{
	int a;
	int b;
};

int mergeSort(Muchie v[],int st,int dr);
int _mergeSort(Muchie v[],Muchie temp[],int st,int dr);
int merge(Muchie v[],Muchie temp[],int st,int mij,int dr);

int main(){
	int maxSine;
	int n;
	cin>>maxSine>>n;
	Muchie v[n];
	for(int i=0;i<n;i++){
		cin>>v[i].a>>v[i].b;
	}
	sort(v,v+n,[](Muchie x,Muchie y){return x.a<y.a || x.a==y.a && x.b<y.b;});
	cout<<mergeSort(v,0,n-1);
	return 0;
}

int mergeSort(Muchie v[],int st,int dr){
	Muchie temp[dr+1];
	return _mergeSort(v,temp,st,dr);
}

int _mergeSort(Muchie v[],Muchie temp[],int st,int dr){
	if(st>=dr){
		return 0;
	}
	int mij=(st+dr)/2;
	int inv=0;
	inv+=_mergeSort(v,temp,st,mij);
	inv+=_mergeSort(v,temp,mij+1,dr);
	inv+=merge(v,temp,st,mij,dr);
	return inv;
}
		
int merge(Muchie v[],Muchie temp[],int st,int mij,int dr){
		int inv=0;
		int i=st;
		int j=mij+1;
		int k=st;
		while(i<=mij && j<=dr){
			if(v[i].b<=v[j].b){
				temp[k++]=v[i++];
			}
			else{
				temp[k++]=v[j++];
				inv+=(mij-i+1);
			}
		}
		while(i<=mij){
			temp[k++]=v[i++];
		}
		while(j<=dr){
			temp[k++]=v[j++];
		}
		for(int i=st;i<=dr;i++){
			v[i]=temp[i];
		}
		return inv;
}

