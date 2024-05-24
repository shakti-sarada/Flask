# Jinja2 template engine
'''
{%...%} used for conditional statements,loops.
{{ }} used for expressions to print output
{#...#} used for comments
'''


from flask import Flask,render_template,url_for,redirect,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res='PASS'
    else:
        res='FAIL'

    exp={'Score':score,'Result':res}
    return render_template('result.html',result=exp)


@app.route('/result',methods=['GET','POST'])
def result():
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
    
