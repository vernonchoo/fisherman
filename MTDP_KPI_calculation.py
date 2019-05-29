#coding = utf_8
#美团点评每月KPI计算方式

#输入完成变量
advertising_income = input('广告收入： ')
ads_online_merchants_number =input('推广通在线消耗数量： ')
newly_signed_poi_numbers = input('新开通poi数量： ')
materials_posted = input('物料张贴数量： ')

#输入当月考核变量
advertising_income_kpi = input('广告收入KPI: ')
ads_online_merchants_number_kpi = input('推广通在线消耗数量kpi: ')
newly_signed_poi_numbers_kpi = input('新开通poi数量kpi： ')
materials_posted_kpi = input('物料张贴数量kpi： ')

#定义考核公式：
income_completion = advertising_income/advertising_income_kpi
income_score = ''
if income_completion < 0.7:
    print(income_score = 0.7 * 0.6)
else:
    print(income_score = income_completion * 0.6)


