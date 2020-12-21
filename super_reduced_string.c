char* superReduced(char *s, int n){
	char final[n];
	int indx = -1;
	for(int i=0; i<n; ++i){
		if(indx == -1){
			++indx;
			final[indx] = s[i];
		}
		else if(final[indx] == s[i]){
			--indx;
		}
		else{
			++indx;
			final[indx] = s[i];
		}
	}
	if(indx == -1)
		return 'Empty String'
	final[++indx] = '\0';
	return final;
}
