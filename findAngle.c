int findAngle(int H, int M){
	if(H<0 || M<0 || H>12 || M>60)
		return -1;
	if(H==12)
		H = 0;
	if(M==60)
	{
		H = (H+1)%12;
		M = 0;
		if(H==0)
			H=12;
	}
	int hour_angle = 0.5 * (h*60 + m);
    int minute_angle = 6*m;

    int angle = abs(hour_angle - minute_angle);

	if(angle > 180) 
		return 360-angle;
	return angle;
}