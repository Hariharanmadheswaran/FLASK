from flask import Flask,render_template,url_for,redirect,request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="Hari9940877985"
app.config["MYSQL_DB"]="registration"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

@app.route("/")

def homepage():
    con=mysql.connection.cursor()
    query="select * from register"
    con.execute(query)
    res=con.fetchall()
    return render_template("homepage.html",datas=res)

@app.route("/adduser",methods=["GET","POST"])
def add_user():
    if request.method=="POST":
        name=request.form["name"]
        age=request.form["age"]
        city=request.form["city"]
        con=mysql.connection.cursor()
        query="insert into  register(NAME,AGE,CITY) values (%s,%s,%s)"
        inp=(name,age,city)
        con.execute(query,inp)
        mysql.connection.commit()
        con.close()
        return redirect(url_for("homepage"))
    return render_template("adding_user.html")

@app.route("/edit_user/<string:id>",methods=["GET","POST"])
def edit_user(id):
    # con = mysql.connection.cursor()
    if request.method=="POST":
        name = request.form["name"]
        age = request.form["age"]
        city = request.form["city"]
        query = "update register set NAME=%s ,AGE=%s,CITY=%s where id=%s"
        inp = (name, age, city,id)
        con = mysql.connection.cursor()
        con.execute(query, inp)
        mysql.connection.commit()
        con.close()
        return redirect(url_for("homepage"))
    con = mysql.connection.cursor()
    query = "select * from register where id=%s"
    con.execute(query, [id])
    res=con.fetchone()
    return render_template("edit_details.html",datas=res)

@app.route("/delete_user/<string:id>",methods=["GET","POST"])
def delete_user(id):
    con=mysql.connection.cursor()
    query="delete from register where id=%s"
    con.execute(query,[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for("homepage"))



if __name__=="__main__":
    app.run(debug=True)