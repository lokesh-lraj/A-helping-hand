import java.util.*;
public static int isSumPossible(int arr[], int n, int input_no){
	Set<Integer> hash_set = new HashSet<Integer>();
	for(int i=0; i<n; ++i){
		int req = input_no - arr[i];
		if(hashset.contains(req)){
			return 1;
		}
		hashset.add(arr[i]);
	}
	return 0;
}