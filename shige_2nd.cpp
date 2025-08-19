#include<stdio.h>
#include<stdlb.h>
#include<time.h>

bool dice(int num1,int num2);

int main(void){
  srand((unsigned int)time(NULL));

  printf("1dn m?\n>>");
  int num1,num2;

  scanf_s("%d %d",&num1,&num2);

  if(dice(num1,num2)){
    printf("成功です\n");
    return 0;
  }

  printf("失敗です\n");

  return 0;
}

bool dice(int num1,int num2){
  bool ans = true;
  return ans;
}