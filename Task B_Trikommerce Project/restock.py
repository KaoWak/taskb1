def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
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


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''
    if current_day == 0 :#set 0 to restock day aswell
        restock_amount = 2000 
        available_items = 2000 # Update available items to max limit after restocking
        inventory_records.append([current_day, 0, restock_amount, available_items])
    elif current_day % 7 == 0: # Calculate restock amount (max inventory 2000)
        restock_amount = 2000 - available_items  
        # If its not day to restock do not restock
        available_items = 2000 #+= restock_amount  # Update available stock
        # when  restocking day - sales are 0
        inventory_records.append([current_day, 0, restock_amount, available_items])


    return available_items


