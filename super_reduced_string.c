char* superReduced(char *s){
	
	char final[100];
	int indx = -1;
	
	for(int i=0; s[i]; ++i){
		if((indx == -1) || (final[indx] != s[i])) 
			final[++indx] = s[i];
		
		else if(final[indx] == s[i])
			--indx;
	}
	if(indx == -1)
		return 'Empty String';
	final[++indx] = '\0';
	return final;
}
