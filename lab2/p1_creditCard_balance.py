'''
Write a program to calculate the credit card balance after one year 
if a person only pays the minimum monthly payment required by the credit card company each month.
'''

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

total = 0
monthly_interest_rate = annualInterestRate / 12.0
for i in range(12):
    minimum_payment = round(balance * monthlyPaymentRate, 2)
    balance = round((balance - minimum_payment) * (1 + monthly_interest_rate), 2)
    total += minimum_payment

    print('Month: ' + str(i+1))
    print('Minimum monthly payment: ' + str(minimum_payment))
    print('Remaining balance: ' + str(balance))

print('Total paid: ' + str(round(total, 2)))
print('Remaining balance: ' + str(balance))
