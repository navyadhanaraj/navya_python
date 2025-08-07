from flask import Flask, jsonify, request,render_template
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'navya_cse'

mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/getData')
def getData():
    id=request.args.get('id')
    sql=""
    if id is None:
        sql=f"SELECT * FROM user WHERE id = {id}"
    else:
        sql ="SELECT * FROM user"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    return f'{results}'

@app.route('/userDetail')
def userDetail():
    id="1"
    name = "navya"
    gmail="navya@gmail.com"
    passwords=2110
    return render_template("user_detail.html",
                            id=1,
                            name=navya,
                            email=navya@gmail.com,
                            password=navya
    )


@app.route('/myname')
def navya():
    return 'hello world'
@app.route('/myhtml')
def myHtml():
    return render_template('home.html')

@app.route('/register_save', methods=["GET","POST"])
def register_save():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        return f"{email} {password}"


if __name__ == '__main__':
    app.run(debug=True)
