int main(){
	int t, n;
	scanf("%d",&t);
	for(int i=0; i<t; i++){
		scanf("%d",&n);
		if(n<0){
			printf("Wrong");
		}
		else{
			float bill = 0
			if(n<=199)	
				bill = n*2.0;
			if(n >= 200)
				bill += (n-199)*3.5;
			if(n>= 400)
				bill += (n-399)*5.8;
			if(n>=600)
				bill +=(n-599)*7.0;
			if(bill > 2000)
				bill = (21*bill/20);
			printf("%.1f",bill);
		}
	}
	return 0;
}