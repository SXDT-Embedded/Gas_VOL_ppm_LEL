/*
 * @Author       : yzy
 * @Date         : 2023-02-20 15:55:43
 * @LastEditors  : yzy
 * @LastEditTime : 2023-07-20 13:41:18
 * @FilePath     : \可燃气体VOL-ppm-LEL\vol_2_ppm_lel.c
 * @Description  : VOL转ppm和LEL
 *
 * Copyright (c) 2023 by yzy, All Rights Reserved.
 */
#include <stdio.h>

double vol, lel, ppm;

//                  爆炸浓度 (V%)
// 物质名称	分子式	下限 LEL	上限 UEL
// 甲烷	    CH4	    5	        15
// 乙烷	    C2H6	3	        15.5
// 丙烷	    C3H8	2.1	        9.5

// 甲烷的爆炸下限为 5.0VOL%，即 100% LEL=5.0VOL%
// 那么 10% LEL = 5.0VOL% × 10% = 0.5 VOL%
// 10000 ppm = 1 Vol%

int main(void)
{
    printf("输入VOL%%: \r\n");
    scanf("%lf", &vol);
    printf("VOL%% = %.2f\r\n", vol);

    ppm = 10000 * vol;
    printf("ppm = %.2lf\r\n", ppm);

    lel = vol / 0.05 ;
    printf("lel = %.2lf\r\n", lel);

    return 0;
}
