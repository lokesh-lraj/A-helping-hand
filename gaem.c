#include<stdio.h>
#include<conio.h>

int main(){
	int t, n;
	scanf("%d",&t);
	for(int i=0; i<t; ++i){
		scanf("%d",&n);
		int arr[n], bob_w=0, bob_l=0;
		for(int j=0; j<n; ++j){
			scanf("%d",&arr[j]);
		}
		for(int j=0; j<n; ++j){
			if(arr[j]%5 == 3 || arr[j]%5 == 0)
				++bob_w;
			else if(arr[j] <= 0)
			{}
			else
				++bob_l;
		}
		if(bob_w or bob_l)
		{
			printf("Bob wins in the game %d times.",bob_w);
			printf("Bob loses in the game %d times.",bob_l);
		}
		else{
			printf("Game not possible");
		}

	}
	return 0
}
