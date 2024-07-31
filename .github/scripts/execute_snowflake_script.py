import os
import snowflake.connector
import re

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

def remove_comments(sql):
    # Remove inline comments
    sql = re.sub(r'--.*$', '', sql, flags=re.MULTILINE)
    # Remove multi-line comments
    sql = re.sub(r'/\*[\s\S]*?\*/', '', sql)
    return sql

try:
    cursor = conn.cursor()
    
    # Read SQL from file
    with open('.github/sql_script/snowflake_queries.sql', 'r') as file:
        sql_queries = file.read()
    
    # Remove comments and split into individual queries
    sql_queries = remove_comments(sql_queries)
    queries = [q.strip() for q in sql_queries.split(';') if q.strip()]
    
    # Execute SQL queries
    for query in queries:
        print(f"Executing query: {query}")
        cursor.execute(query)
        print("Query executed successfully")
    
    print("All queries executed successfully")

except snowflake.connector.errors.ProgrammingError as e:
    print(f"Error executing SQL: {e}")
finally:
    cursor.close()
    conn.close()
