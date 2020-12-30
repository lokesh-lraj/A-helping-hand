float findDurationToClimb(float l, float X, float P, float Y, float Q)
{
	float up_in_hour = (X/P);
	float down_in_hour = (Y/Q);

	float diff = (up_in_hour - down_in_hour);
	diff = 1/diff;
	return diff*l;
}
