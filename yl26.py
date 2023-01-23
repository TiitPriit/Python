def calculate_commission(revenue, expenses):
    commission = {}
    for salesperson in revenue:
        commission[salesperson] = 0
        for i in range(len(revenue[salesperson])):
            profit = revenue[salesperson][i] - expenses[salesperson][i]
            if profit > 0:
                commission[salesperson] += profit * 0.062
    return commission

revenue = {"Frank": [120, 243], "Jane": [145, 265]}
expenses = {"Frank": [130, 143], "Jane": [59, 198]}
print(calculate_commission(revenue, expenses))

def calculate_commission(revenue, expenses):
    commission = {}
    for salesperson in revenue:
        commission[salesperson] = 0
        for i in range(len(revenue[salesperson])):
            profit = revenue[salesperson][i] - expenses[salesperson][i]
            if profit > 0:
                commission[salesperson] += profit * 0.062
    return commission

revenue = {"Johnver": [190, 325, 682, 829], "Vanston": [140, 19, 14, 140], "Danbree": [1926, 293, 852, 609], "Vansey": [14, 1491, 56, 120], "Mundyke": [143, 162, 659, 87]}
expenses = {"Johnver": [120, 300, 50, 67], "Vanston": [65, 10, 299, 254], "Danbree": [890, 23, 1290, 89], "Vansey": [54, 802, 12, 129], "Mundyke": [430, 235, 145, 76]}
print(calculate_commission(revenue, expenses))
