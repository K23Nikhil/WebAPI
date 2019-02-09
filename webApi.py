from flask import Flask,jsonify
import pyodbc
app = Flask(__name__)


@app.route('/')
def hello():
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=qsrxGIGI;"
                      "Trusted_Connection=yes;")
    cursor = cnxn.cursor()
    cursor.execute('select * from vxstore')
    data = []
    rows = cursor.fetchall()
    for row in rows:
        data.append([x for x in row])
    return jsonify({"jsondata":data})

if __name__ == '__main__':
    app.run()
