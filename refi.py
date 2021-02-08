#!/usr/bin/env python

INIT_LOAN_AMOUNT = 1000000
INIT_LOAN_RATE = 0.02875
INIT_YEARS = 30
PAYMENT_PER_YEAR = 12
INIT_MONTHS_PAID = 14

# How much initial principle was paid on the month of closing, e.x. $500. This is a small adjustment to make the calculation more accurate. 
# You can easily find it on the mortgate portal, or, set it to zero to simplify the calculation.
INIT_PRINCIPLE_PAID = 0

REFI_LOAN_RATE = 0.026
REFI_LOAN_YEARS = 30

def get_monthly_payment(loan_amount, loan_rate, loan_years, payment_per_year):
	return 1.0 * (loan_amount * (1.0 * loan_rate / payment_per_year) * (1 + (1.0 * loan_rate / payment_per_year)) ** (payment_per_year * loan_years)) / ((1 + 1.0 * loan_rate / payment_per_year) ** (payment_per_year * loan_years) - 1)

def get_total_balance_and_interest(init_balance, months, monthly, loan_rate, payment_per_year):
	total_intest = 0
	cur_balance = init_balance
	for i in range(0, months):
		month_interest = cur_balance * loan_rate / payment_per_year
		month_principle = monthly - month_interest
		total_intest += cur_balance * loan_rate / 12
		cur_balance -= month_principle
	return (cur_balance, total_intest)


init_monthly = get_monthly_payment(INIT_LOAN_AMOUNT, INIT_LOAN_RATE, INIT_YEARS, PAYMENT_PER_YEAR)

# Calculate all interest paid
remain_balance, init_total_interst = get_total_balance_and_interest(INIT_LOAN_AMOUNT - INIT_PRINCIPLE_PAID, INIT_MONTHS_PAID, init_monthly, INIT_LOAN_RATE, PAYMENT_PER_YEAR)
print("Remained balance before refi {remain_balance}, total interest paid {init_total_interst}".format(remain_balance=remain_balance, init_total_interst=init_total_interst))

refi_monthly = get_monthly_payment(remain_balance, REFI_LOAN_RATE, REFI_LOAN_YEARS, PAYMENT_PER_YEAR)
refi_remain_balance, refi_total_interest = get_total_balance_and_interest(remain_balance, 30 * 12, refi_monthly, REFI_LOAN_RATE, PAYMENT_PER_YEAR)
print("Refi balance {refi_remain_balance}, refi total interst {refi_total_interest}".format(refi_remain_balance=refi_remain_balance, refi_total_interest=refi_total_interest))


_, total_intest_without_refi = get_total_balance_and_interest(INIT_LOAN_AMOUNT - INIT_PRINCIPLE_PAID, 30 * 12, init_monthly, INIT_LOAN_RATE, PAYMENT_PER_YEAR)

total_intest_without_refi = total_intest_without_refi
total_intest_with_refi = init_total_interst+refi_total_interest
total_intest_saving_with_refi = total_intest_without_refi - total_intest_with_refi

print("Monthly cashflow savings {montly_saving}".format(montly_saving=init_monthly - refi_monthly))
print("Total interest without refi {total_intest_without_refi}".format(total_intest_without_refi=total_intest_without_refi))
print("Total interest with refi {total_intest_with_refi}".format(total_intest_with_refi=total_intest_with_refi))
print("Total saving with refi {total_intest_saving_with_refi}".format(total_intest_saving_with_refi=total_intest_saving_with_refi))
