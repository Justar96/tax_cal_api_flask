from flask import Flask, render_template ,redirect, url_for ,request
import requests

app = Flask(__name__)

#Calculation of Personal Income Tax in Thailand (Function)
def tax_cal_annual(net_income):
    #Variable
    income_limit = [150000,300000,500000,750000,1000000,2000000,5000000]
    tax_var_multi = [0.05,0.10,0.15,0.20,0.25,0.3,0.35]
    tax_amount = 0
    
    #Calculate
    if net_income > income_limit[6]:
        tax_amount += int((net_income-income_limit[6])*tax_var_multi[6])
        net_income = income_limit[6]

    if net_income > income_limit[5]:
        tax_amount += int((net_income-income_limit[5])*tax_var_multi[5])
        net_income = income_limit[5]

    if net_income > income_limit[4]:
        tax_amount += int((net_income-income_limit[4])*tax_var_multi[4])
        net_income = income_limit[4]

    if net_income > income_limit[3]:
        tax_amount += int((net_income-income_limit[3])*tax_var_multi[3])
        net_income = income_limit[3]

    if net_income > income_limit[2]:
        tax_amount += int((net_income-income_limit[2])*tax_var_multi[2])
        net_income = income_limit[2]

    if net_income > income_limit[1]:
        tax_amount += int((net_income-income_limit[1])*tax_var_multi[1])
        net_income = income_limit[1]

    if net_income > income_limit[0]:
        tax_amount += int((net_income-income_limit[0])*tax_var_multi[0])
        net_income = income_limit[0]
        
    return ("Your total tax amount due is: "+str("{:,}".format(tax_amount))+" Baht")


@app.route('/tax-cal' ,methods=['POST','GET'])
def main():
    if request.method == 'POST':
        data = request.get_json()
        get_value = data['value']
        return tax_cal_annual(get_value)
    else:
        get_value = request.args.get('value')
        get_value = int(get_value)

        return tax_cal_annual(get_value)



if __name__ == '__main__':
    # app.run(host='8.213.211.211',port=8080,ssl_context='adhoc')
    app.run()