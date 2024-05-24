#Integrating HTML with Flask
#Render_template is used to search the templates folder for a particular file
#Request is used for reading the posted value
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=50:
        res='PASS'
    else:
        res="FAIL"

    return render_template('result.html',result=res)

#Result Checker submit HTML Page

@app.route('/submit',methods=['GET','POST'])
def submit():
    avg=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        physics=float(request.form['physics'])
        chemistry=float(request.form['chemistry'])
        avg=(science+maths+chemistry+physics)/4
    
    return redirect(url_for('success',score=avg))
    
    
        

if __name__=="__main__":
    app.run(debug=True)