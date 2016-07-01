'''
write a program that calculates the minimum fixed monthly payment 
needed in order to pay off a credit card balance within 12 months.
the monthly payment must be a multiple of $10
'''

balance = 4773
annualInterestRate = 0.2

monthly_interest_rate = annualInterestRate / 12.0
fixed_payment = 0
balanceCopy = balance
while balance > 0:
    balance = balanceCopy
    fixed_payment += 10
    for i in range(12):
        balance = (balance - fixed_payment) * (1 + monthly_interest_rate)
print('Lowest Payment: ' + str(fixed_payment))
