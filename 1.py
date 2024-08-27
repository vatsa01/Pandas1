Problem 1 : Make a Pandas DataFrame with two-dimensional list
import pandas as pd
l1 = [[1,2,3], [4,5,6]]
    df = pd.DataFrame(l1, columns = ['X-Axis', 'Y-Axis', 'Z-Axis'])
    return df

Problem 2 :Big Countries
import pandas as pd
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['population'] >= 25000000) | (world['area'] >= 3000000)]
    return df[['name', 'population', 'area']]

Problem 3 :Recyclable and Low Fat Products
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return df[['product_id']] 

Problem 4 :Customer Who Never Order
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders['customerId'])]
    return df[['name']].rename(columns = {'name':'Customers'})

    df = customers.merge(orders, left_on = 'id',right_on = 'customerId', how = 'left')
    df = df[df['customerId'].isna()]
    return df[['name']].rename(columns = {'name':'Customers'})
    
