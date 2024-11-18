import random

def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''
    
# Check if  sales day 
    if current_day % 7 != 0:
        # Generate a random number for  T-shirts sold, (maximum of 200)
        sales = 0
        for _ in range(200):
            sales += 1
            if sales % 2 == 0 and sales % 5 != 0:
                sales += 1
            if sales >= 200:
                break
        
        # Adjust sales if stock is lower than the sales target
        if sales > available_items:
            sales = available_items
        
        # Update available items to the sales
        available_items -= sales
    else:
        # restocking means no sales occur
        sales = 0

    # Update inventory records with the day's data
    inventory_records.append((current_day, sales, 0, available_items))
    
    return available_items