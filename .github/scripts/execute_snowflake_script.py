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
    
    # Execute SQL to alter the table
    alter_sql = "ALTER TABLE TEST_DB.PUBLIC.EMPLOYEE MODIFY COLUMN NAME VARCHAR(30)"
    cursor.execute(alter_sql)
    
    print("Table altered successfully")

finally:
    cursor.close()
    conn.close()
