from flask import Flask
from psycopg2 import connect
import os

app= Flask(__name__)

@app.route("/")
def main():
    table_name="aplication"
    conn= connect(
            dbname= os.getenv('dbname'),
            user= os.getenv('user'),
            host= os.getenv('IP_POSTGRES'),
            password= os.getenv('password')
            )
    cursor=conn.cursor()
    cursor.execute(f"Select * from {table_name};")
    result=[record for i, record in enumerate(cursor)]
    cursor.close()
    conn.close()
    return str(result)

if __name__=="__main__":
    app.run()

