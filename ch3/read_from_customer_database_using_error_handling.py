
import pandas as pd
import pyodbc

conn = pyodbc.connect("DRIVER={SQLite3 ODBC Driver};SERVER=localhost;" \
                      "DATABASE=customers.db;Trusted_connection=yes")

def process_data(conn = conn):

    customer_key_features = pd.read_sql(conn,
                                        """SELECT churn,
                                                  total_day_charge,
                                                  total_intl_minutes,
                                                  number_customer_service_calls
                                           FROM customer_data""")

    if customer_key_features.shape[0] == 0:
        raise Exception("Empty data returned")

    # [...additional code]
    
    return customer_key_features