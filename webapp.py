from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/") #annotation tells the url that will make this function run
def render_main():
    return render_template('home.html')

@app.route("/Paragraph1")
def render_page1():
    return render_template('page1.html')

@app.route("/Paragraph2")
def render_page2():
    return render_template('page2.html')

@app.route("/Paragraph3")
def render_page3():
    return render_template('page3.html')
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
