#include<stdio.h>
#include<conio.h>

int main(){
	int t, n;
	scanf("%d",&t);
	for(int i=0; i<t; ++i){
		scanf("%d",&n);
		int var, bob_w=0, bob_l=0;
		for(int j=0; j<n; ++j){
			scanf("%d",&var);
			
			if(var <= 0);
			
			else if(var%5 == 3 || var%5 == 0)
				++bob_w;
			else
				++bob_l;
		}
		if(bob_w or bob_l)
		{
			printf("Bob wins in the game %d times.\n",bob_w);
			printf("Bob loses in the game %d times.\n",bob_l);
		}
		else{
			printf("Game not possible\n");
		}

	}
	return 0
}
