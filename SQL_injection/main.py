import sqlite3
import pandas as pd
import argparse

def execute_query(sql):
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        result = cursor.execute(sql)
        rows = result.fetchall()
        df = pd.DataFrame(rows)
        df = df.rename(columns={0:"users", 1:"password"})
    return df

def parse_args():
    parser = argparse.ArgumentParser(description="A simple argparse function with two arguments: username and password.")
    parser.add_argument("-u", "--username", dest="username", type=str, required=True, help="The username.")
    parser.add_argument("-p", "--password", dest="password", type=str, required=True, help="The password.")
    args = parser.parse_args()
    return args.username, args.password

if __name__ == "__main__":
    username, password = parse_args()
    query = f"select * from users where username='{username}' and password='{password}'"
    print(query)
    result = execute_query(query)
    if len(result) == 0:
        print(f"Provided credentials [{username},{password}] doesn't exist")
    else:
        print(result)

