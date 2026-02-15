from flask import Flask, render_template, request
import mysql.connector
from llm_to_sql import nl_to_sql

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="labuser",      
    password="lab123",
    database="nl_db"
)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    sql_query = None

    if request.method == "POST":
        user_query = request.form["query"]

        sql_query = nl_to_sql(user_query)

        cursor = db.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()

    return render_template(
        "index.html",
        result=result,
        sql_query=sql_query
    )

if __name__ == "__main__":
    app.run(debug=True)