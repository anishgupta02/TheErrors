from flask import Flask,render_template, request
import model


app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def hello():
    text=""
    a=""
    if request.method=="POST":
        tex=request.form['review']
        text=model.prediction(tex)
        if text==1:
            a='POSITIVE REVIEW'
        elif text==-1:
            a='NEGATIVE REVIEW'
        else:
            a='NEUTRAL REVIEW'
    return render_template("index2.html",myreview=a)


'''
@app.route("/sub",methods=["POST"])
def submit():
    if request.method=="POST":
        name=request.form["review"]
    return render_template("sub.html",n=name)
'''


if __name__=="__main__":
    app.run(debug=True)