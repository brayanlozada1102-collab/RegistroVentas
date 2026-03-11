
def sales_register(product_name,quantity,unit_value,daily_sales):
    update = {"name":product_name,
         "quantity" : quantity,
         "unitvalue" : unit_value
         }
    daily_sales.append(update)

def show_summary(daily_sales):
    for i in range(len(daily_sales)):
        print(f"{daily_sales[i]['name']} \nQuantity sold: {daily_sales[i]['quantity']} \nPrice per unit sold: ${daily_sales[i]['unitvalue']}")
        print("--------------------")