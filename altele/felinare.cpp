#include<iostream>
#include<algorithm>

using namespace std;

struct Interval{
	int a;
	int b;
};

int main(){
	int n;
	cin>>n;
	Interval v[n];
	int power;
	for(int i=0;i<n;i++){
		cin>>power;
		v[i].a=i-power;
		v[i].b=i+power;
	}
	sort(v,v+n,[](Interval x,Interval y){return x.a<y.a;});
	for(int i=0;i<n;i++)
		cout<<v[i].a<<" ";
	cout<<'\n';
	for(int i=0;i<n;i++)
		cout<<v[i].b<<" ";	
	int start=0;
	int end=start-1;
	int cnt=0;
	for(int i=0;i<n;i++){
		if(v[i].a<=start){
			end=max(end,v[i].b);
		}
		else{
			start=end;
			cnt++;
			if(v[i].a>end || end>n){
				break;
			}
		}
	}
	cout<<endl;
	cout<<cnt;
	return 0;
}
