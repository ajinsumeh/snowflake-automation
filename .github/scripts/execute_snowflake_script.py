import os
import sys
import snowflake.connector
import re

def remove_comments(sql):
    # Remove inline comments
    sql = re.sub(r'--.*$', '', sql, flags=re.MULTILINE)
    # Remove multi-line comments
    sql = re.sub(r'/\*[\s\S]*?\*/', '', sql)
    return sql

def execute_sql_file(file_path):
    print(f"Processing file: {file_path}")
    
    # Create a connection to SF with the credentials provided
    conn = snowflake.connector.connect(
        account=os.environ['SNOWFLAKE_ACCOUNT'],
        user=os.environ['SNOWFLAKE_USER'],
        password=os.environ['SNOWFLAKE_PASSWORD'],
        role=os.environ['SNOWFLAKE_ROLE'],
        warehouse=os.environ['SNOWFLAKE_WAREHOUSE'],
        database=os.environ['SNOWFLAKE_DATABASE']
    )
    try:
        # Cursors help in executing snowflake files
        cursor = conn.cursor()
        
        # Read content SQL from file
        with open(file_path, 'r') as file:
            sql_queries = file.read()
        
        print(f"Original SQL:\n{sql_queries}")
        
        # Remove comments and split into individual queries
        sql_queries = remove_comments(sql_queries)
        print(f"SQL after removing comments:\n{sql_queries}")
        
        # If there are multiple queries in a single file, split with ';' delimiter 
        queries = [q.strip() for q in sql_queries.split(';') if q.strip()]
        
        # Execute SQL queries 
        for i, query in enumerate(queries, 1):
            print(f"Query {i} is: {query}")
            cursor.execute(query)
            print("Query executed successfully")
        
        print(f"All queries in {file_path} executed successfully")
    except snowflake.connector.errors.ProgrammingError as e:
        print(f"Error executing SQL from {file_path}: {e}")
        raise  # fails the GitHub action
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:  # exactly 1 argument
        print("Usage: execute_snowflake_script.py <sql_file_path>")
        sys.exit(1)
    
    sql_file_path = sys.argv[1]
    execute_sql_file(sql_file_path)
