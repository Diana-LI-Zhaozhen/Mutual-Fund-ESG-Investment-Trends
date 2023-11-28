
#set up database
import clickhouse_connect
import os, pandas as pd
from sqlalchemy import create_engine, Column, MetaData
import clickhouse_driver
from clickhouse_sqlalchemy import (
Table, make_session, get_declarative_base, types, engines
)
import getpass,time
from IPython.display import display, HTML

#%%
#local server via clickhouse_connect
def clickhouse_query(query):
    """
    :param query: the query string
    :return: the query result
    """
    # feed the password for this query
    # read a file that contains the password
    # report timings

    start_time = pd.Timestamp.now()
    end_time = pd.Timestamp.now()
    elapsed_time = end_time - start_time
    print(f'Elapsed time: {elapsed_time} seconds')    
    client = clickhouse_connect.get_client(host='localhost')
    df = client.query_df(query)
    return df

#%%
#class server

# username
user='#username'
password = '#password'

'''
# read the password
with open('../dianali_password.txt') as f:
    # read the password
    password=f.readline().strip()
    print(f.readline().strip())
'''

#%%
#class clickhouse server
def class_clickhouse_query(query):
    """
    :param query: the query string
    :return: the query result
    """
    # feed the password for this query
    # read a file that contains the password
    # report timings
    start_time = pd.Timestamp.now()
    db_con = clickhouse_driver.Client(host='', port=, user=user,
                                    password=password,
                                        database='crsp',
                                        settings={'use_numpy': True})
    end_time = pd.Timestamp.now()
    elapsed_time = end_time - start_time
    print(f'Elapsed time: {elapsed_time} seconds')    
    df, types=db_con.execute(query,with_column_types=True)
    # convert df to dataframe
    df2=pd.DataFrame(df)
    # retrieve columns to the dataframe
    df2.columns=[x[0] for x in types]
    return df2
#%%
#class mysql server
def mysql_query(query,user=user, password=password, host='', port=):
    # start time
    start_time = time.time()

    name_of_sql='mysql'

    engine = create_engine('mysql+pymysql://'+user+':'+password+'@'+host+':'+str(port))
    df = pd.read_sql(query, engine)
    # end time
    end_time = time.time()
    # seconds
    elapsed_time = end_time - start_time
    print(f'{name_of_sql} --> Elapsed time: {elapsed_time} seconds')
    return df    
