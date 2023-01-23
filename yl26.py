def calculate_bonus(sales_dict):
    bonus_dict = {}
    for employee, sales in sales_dict.items():
        if sales > 10000:
            bonus = (sales - 10000) * 0.1
            bonus_dict[employee] = bonus
    return bonus_dict

sales = {'John': 15000, 'Sara': 12000, 'Bob': 9000}
print(calculate_bonus(sales)) # {'John': 500.0, 'Sara': 200.0}
