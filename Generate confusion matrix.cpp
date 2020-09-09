#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <cmath>
#define maxn 30020
using namespace std;
double a[16];
struct pos{
	int wz;
	double score;
}b[16];
char name[102];
bool cmp(pos x,pos y){
	return x.score > y.score;
}
int main()
{
	freopen("test.txt","r",stdin);
	freopen("test_result.txt","w",stdout);
	for(int i=0;i<40;++i){
		scanf("%s",name);
		double aug = 0;
		for(int j=0;j<16;++j){
			scanf("%lf",&a[j]);
			a[j] = exp(a[j]);
			aug += a[j];
			b[j].wz = j;
			b[j].score = a[j];
		}
		sort(b,b+16,cmp);
		printf("%s ",name);
		for(int j=0;j<5;++j)printf("%d ",b[j].wz);
		for(int j=0;j<16;++j)printf("%.4lf ", a[j]/aug);
		printf("\n");
	}
	return 0;
}
