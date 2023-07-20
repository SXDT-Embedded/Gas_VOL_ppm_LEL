/*
 * @Author       : yzy
 * @Date         : 2023-02-20 15:55:43
 * @LastEditors: xt 1834031381@qq.com
 * @LastEditTime: 2023-07-20 16:35:06
 * @FilePath     :\可燃气体VOL-ppm-LEL\vol_2_ppm_lel.c
 * @Description  :  VOL转ppm和LEL
 *
 * Copyright (c) 2023 by yzy, All Rights Reserved.
 */
#include <stdio.h>
#include <string.h>

#define METHANE_LEL   0.05
#define ETHANCE_LEL   0.03
#define PROPANCE_LEL  0.021

char change_name[4];
char gas_name[5];
double vol, lel, ppm, gas_lel;

void GasChange(void);
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
    while(1)
    {
        printf("输入气体的分子式,如CH4、C2H6、C3H8。若退出转化,输入break\r\n");
        scanf("%s", &gas_name);
        
        if (!strcmp(gas_name, "CH4"))
        {
        gas_lel = METHANE_LEL;
        }
        else if (!strcmp(gas_name, "C2H6"))
        {
        gas_lel = ETHANCE_LEL;
        }
        else if (!strcmp(gas_name, "C3H8"))
        {
        gas_lel = PROPANCE_LEL;
        }
        else if (!strcmp(gas_name, "break"))
        {
            break;
        }
        else
        {
            printf("输入有误,");
            continue;
        }
        GasChange();
    }

    return 0;
}

void GasChange(void)
{
    while(1)
    {
        printf("输入转化的名称,如VOL、ppm、LEL。若退出该气体,输入break。\r\n");
        scanf("%s", &change_name);
        if (!strcmp(change_name, "VOL"))
        {
            printf("输入VOL%%: \r\n");
            scanf("%lf", &vol);
            ppm = 10000 * vol;
            lel = vol / gas_lel;
        }
        else if (!strcmp(change_name, "ppm"))
        {
            printf("输入ppm\r\n"); 
            scanf("%lf", &ppm);
            vol = ppm / 10000;
            lel = vol / gas_lel;
        }
        else if (!strcmp(change_name, "LEL"))
        {
            printf("输入LEL\r\n"); 
            scanf("%lf", &lel);
            vol = lel * gas_lel;
            ppm = 10000 * vol;
        }
        else if (!strcmp(change_name, "break"))
        {
            break;
        }
        else
        {
            printf("输入有误,");
            continue;
        }
        printf("VOL%% = %.4lf\r\n", vol);
        printf("ppm = %.4lf\r\n", ppm);
        printf("LEL = %.4lf\r\n", lel);
    }
}