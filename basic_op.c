#include<stdio.h>
#include<conio.h>

int main()
{
  int a, b, sum_i, sub_i;
  float c, d, sum_f, sub_f;
  scanf("%d%d",&a, &b);
  scanf("%f%f", &c, &d);
  sum_i = a+b;
  sub_i = a-b;
  sum_f = c+d;
  sub_f = c-d;
  printf("%d %d", sum_i, sub_i);
  printf("%d %d",sum_f, sub_f);
  return 0;
}
