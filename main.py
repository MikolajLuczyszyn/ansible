from flask import Flask
from psycopg2 import connect

app= Flask(__name__)

@app.route("/")
def main():
    table_name="aplication"
    conn= connect(
            dbname= "test",
            user= "postgres",
            host= "postgres_db",
            password= "admin"
            )
    cursor=conn.cursor()
    cursor.execute(f"Select * from {table_name};")
    result=[record for i, record in enumerate(cursor)]
    cursor.close()
    conn.close()
    return str(result)

if __name__=="__main__":
    app.run()
