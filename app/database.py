import pandas as pd
import sqlite3
from datetime import datetime
def createdb():
    global df1, df2, df3, df4, df5
    df1 = pd.read_csv('customers.csv')
    df2 = pd.read_csv('customer_companies.csv')
    df3 = pd.read_csv('deliveries.csv')
    df4 = pd.read_csv('orders.csv')
    df5 = pd.read_csv('order_items.csv')


    cust_comp = pd.merge(left = df1,right = df2, left_on='company_id',right_on='company_id')
    items_order = pd.merge(left = df5,right = df4, left_on='order_id',right_on='id')
    items_order.drop(['id_x','id_y'],axis =1,inplace=True)
    items_delivery = pd.merge(left = df5,right = df3, left_on= 'id',right_on='order_item_id')
    items_delivery.drop(['id_x','id_y'],axis =1,inplace=True)
    newcsv = pd.merge(left = items_delivery[['order_id','order_item_id','delivered_quantity']],how = 'right', right = items_order, left_on='order_id',right_on='order_id')


    newcsv['Total_Amount'] = newcsv.apply(lambda row: row.delivered_quantity * row.price_per_unit, axis = 1)

    newcsv1 = newcsv[['order_name','product','customer_id','created_at','delivered_quantity','Total_Amount']]

    conn1 = sqlite3.connect('sense1.db')
    conn2 = sqlite3.connect('sense2.db')
    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()
    print("Opened database successfully")
    try:
        newcsv1.to_sql('order_details', conn1)
        cust_comp.to_sql('company_details', conn2)


    except ValueError:
        print('already exists')

    newsql = pd.read_sql_query("SELECT * FROM order_details", conn1)
    newsql1 = pd.read_sql_query("SELECT * FROM company_details", conn2)

    newcsv2 = pd.merge(left = newsql,right = newsql1[['user_id','company_name']],left_on='customer_id',right_on='user_id')
    newcsv2.drop(['user_id','index'],axis = 1,inplace=True)

    finalframe = newcsv2[['order_name','product','company_name','customer_id','created_at','Total_Amount']]
    finalframe[['Date', 'Time']] = finalframe.created_at.str.split("T", expand=True, )

    finalframe['Date'] = pd.to_datetime(finalframe['Date'])
    finalframe['Date'] = finalframe['Date'].dt.strftime('%d/%m/%Y')
    return finalframe

createdb()
