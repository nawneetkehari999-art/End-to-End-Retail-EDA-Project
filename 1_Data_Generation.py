#------------------------- # EDA Project # ---------------------------
#---------------------------
# Step 1 : Import librarise
import pandas as pd
import numpy as np
import random 
from faker import Faker 
#---------------------------
# Initialize Faker for generating fake data 
fake = Faker ()
#---------------------------

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#---------------------------
# Step 2: Define Base list
#---------------------------
categories = {
    "Furniture" : ["Office Chari", "Study Table", "Sofa","Bookshelf", "Dining Table"],
    "Office Supplise" : ["Pen", "Notebook", "Stapler", "File Folder", "Calculator"],
    "Electroincs" : ["Laptop", "Keyboard", "Mouse", "Headphones", "Monitor"],
    "Grocery" : ["Rice Bag", "Cooking Oil","Sugar", "Snacks","Juice Pack"],
}

regions = ["North", "South", "East", "West"]
payment_modes = ["Cash", "Credit Card", "UPI", "Net Banking"]
delivery_status = ["Delivered", "Pending" ,"Returned", "Cancelled"]
customer_segments = ["Consumer", "Corprate", "Home Office"]
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#---------------------------
# Step 3: Generate dataset
#---------------------------
record = [] # Empty list to store all rows

for i in range(1000): # 1000 fake orders
    order_id = f"ODR{1000 +i}"
    order_date = fake.date_between(start_date='-2y', end_date='today')
    ship_date = order_date + pd.Timedelta(days=random.randint(1, 7))

    customer_name = fake.name()
    customer_id = f"CUST{random.randint(100, 999)}"
    customer_segment = random.choice(customer_segments)

    category = random.choice(list(categories.keys()))
    product_name = random.choice(categories[category])
    product_id = f"PROD{random.randint(1000, 9999)}"

    region = random.choice(regions)
    state = fake.state()
    city = fake.city()

    quantity = random.randint(1, 10)
    unit_price = random.randint(100, 5000)
    discount = random.choice([0, 5, 10, 15, 20])

    sales_amount = quantity * unit_price * (1 - discount / 100)
    cost_price = sales_amount * random.uniform(0.6, 0.9)
    profit = sales_amount - cost_price

    stock_left = random.randint(0, 50)

    # -------------- STOCK & REORDER LOGIC -------------
    if  stock_left < 10:
        auto_reoder = "Yes"
        reorder_quantity = random.randint(20, 50)
    else: 
        auto_reorder = "No"
        reorder_quantity = 0
    # ------------------------------------------------

        supplier_name = fake.company()
        supplier_email= fake.company()
        payment_mode = random.choice(payment_modes)
        delivery = random.choice(delivery_status)
    # ===---------------**********-----------------===
    #  Append row as a dictionary
    # ===---------------**********-----------------===
    record.append({
        "OrderId" : order_id,
        "Order Date" : order_date,
        "Ship Date" : ship_date,
        "Customer ID" : customer_id,
        "Custommer Name" : customer_name,
        "Customer Segment" :customer_segment,
        "Product ID" : product_id,
        "Product Name" : product_name,
        "Category" : category,
        "Region" : region,
        "State" : state,
        "City" : city,
        "Quantity" : quantity,
        "Unit Price" : unit_price,
        "Discount(%)" : discount,
        "sale Amount" : round (sales_amount, 2),
        "Cost Price" : round (cost_price, 2),
        "profit" : round(profit,2),
        "Payment Mode" : payment_mode,
        "Delivery Status" : delivery,
        "Supplier Name " : supplier_name,
        "Supplier Email" : supplier_email,
        "Stock Left" : stock_left,
        "Auto Reorder" : auto_reorder,
        "Reorder Quantity" : reorder_quantity,
    })  

    # ===---------------**********----------------===
    #  Step 4: Create DataFrame and save to CSV
    # ===---------------**********----------------===
    df =pd.DataFrame(record)
    try:
        df.to_csv("Superstore_Management_System.csv", index=False)
        print(" ✅ Dataset genrated successfully! File saved as 'Superstore_Management_System.csv")
    except PermissionError:
        print(" ⚠️ Please close the file 'Superstore_Management_System.csv' if it's opne in Excel or Power BI, and try again." )

# ===---------------**********-----------------======---------------**********-----------------======-----------***********----------=======










    