import os
import snowflake.connector

# Snowflake connection parameters
account = os.environ['SNOWFLAKE_ACCOUNT']
user = os.environ['SNOWFLAKE_USER']
password = os.environ['SNOWFLAKE_PASSWORD']
role = os.environ['SNOWFLAKE_ROLE']
warehouse = os.environ['SNOWFLAKE_WAREHOUSE']
database = os.environ['SNOWFLAKE_DATABASE']

# Connect to Snowflake
conn = snowflake.connector.connect(
    account=account,
    user=user,
    password=password,
    role=role,
    warehouse=warehouse,
    database=database
)

try:
    cursor = conn.cursor()
    
    # Read SQL from file
    with open('snowflake_queries.sql', 'r') as file:
        sql_queries = file.read()
    
    # Execute SQL queries
    for query in sql_queries.split(';'):
        if query.strip():
            cursor.execute(query)
    
    print("Queries executed successfully")

finally:
    cursor.close()
    conn.close()
