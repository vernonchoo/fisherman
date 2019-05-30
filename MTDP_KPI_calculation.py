# -*- coding: UTF-8 -*-
#美团点评每月KPI计算方式

#输入当月指标完成变量
advertising_income = int(input('广告收入： '))
ads_online_merchants_number =int(input('推广通在线消耗数量： '))
newly_signed_poi_numbers = int(input('新开通poi数量： '))
materials_posted = int(input('物料张贴数量： '))
coupon_income = int(input('团购交易收入： '))

#输入当月考核变量
advertising_income_kpi = int(input('\n广告收入KPI: '))
ads_online_merchants_number_kpi = int(input('推广通在线消耗数量kpi: '))
newly_signed_poi_numbers_kpi = int(input('新开通poi数量kpi： '))
materials_posted_kpi = int(input('物料张贴数量kpi： '))

#定义考核公式：
#定义考核系数：
income_completion = float(advertising_income/advertising_income_kpi)
income_score = float(income_completion * 0.6)
if income_completion <= 0.7:
    income_score = 0.7 * 0.6
elif income_completion > 0.7 and income_completion <= 1.3:
    income_score = income_completion * 0.6
elif income_completion > 1.3:
    income_score = 1.3 * 0.6
print(income_score)

ads_online_merchants_number_completion = float(ads_online_merchants_number/ads_online_merchants_number_kpi)
ads_online_merchants_number_score = float(ads_online_merchants_number_completion * 0.2)
if ads_online_merchants_number_completion <= 0.7:
    ads_online_merchants_number_score = 0.7 * 0.2
elif ads_online_merchants_number_completion > 0.7 and ads_online_merchants_number_completion <= 1.5:
    ads_online_merchants_number_score = ads_online_merchants_number_completion * 0.2
elif ads_online_merchants_number_completion > 1.5:
    ads_online_merchants_number_score = 1.5 * 0.2
print(ads_online_merchants_number_score)

newly_signed_poi_numbers_completion = float(newly_signed_poi_numbers/newly_signed_poi_numbers_kpi)
newly_signed_poi_numbers_score = float(newly_signed_poi_numbers_completion * 0.2)
if newly_signed_poi_numbers_completion <= 0.7:
    newly_signed_poi_numbers_score = 0.7 * 0.2
elif newly_signed_poi_numbers_completion > 0.7 and newly_signed_poi_numbers_completion <= 1.5:
    newly_signed_poi_numbers_score = newly_signed_poi_numbers_completion * 0.2
elif newly_signed_poi_numbers_completion > 1.5:
    newly_signed_poi_numbers_score = 1.5 * 0.2
print(newly_signed_poi_numbers_score)
business_coefficients = float(income_score + ads_online_merchants_number_score + newly_signed_poi_numbers_score)
print(business_coefficients)

#定义管理系数：
materials_posted_completion = float(materials_posted/materials_posted_kpi)
materials_posted_score = float(materials_posted_completion)
if materials_posted_completion <= 0.8:
    materials_posted_score = 0.8
elif materials_posted_completion > 0.8 and materials_posted_completion <= 1.1:
    materials_posted_score = materials_posted_completion
elif materials_posted_completion > 1.1:
    materials_posted_score = 1.1
management_coefficients = materials_posted_score
print(management_coefficients)

#定义整体KPI计算公式
commission_basement = 0.3
current_month_final_commission = int((advertising_income + coupon_income) * business_coefficients *
                                     management_coefficients * commission_basement)
current_month_final_commission_rate = float(current_month_final_commission/(advertising_income + coupon_income))
print('当月总佣金为： ' + str(current_month_final_commission))
print('当月实际返佣比为: ' + str(current_month_final_commission_rate))