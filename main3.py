# from flask inport Flask, request, url_for, redirect, render_template

# app =  Flask(__name__)

# # GET Request - a GET message is sent and the server returns data
# # POST Reqeust - used to send HTML form data to the server

# @app.route('/',methods = ['POST', "GET"]) # http request. Server receives from client. REST.
# def home():
#     # return render_template("login.html")
#     if request.method == 'POST': # POST - request send html form data from client to server
#         return redirect(url_for('logged'))
#     # GET most common message sent from client the server returns data
#     return render_template("login.html")
# # Once logged in
# @app.route('/Real_news')
# def logged():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

# GET Request - a GET message is sent and the server returns data
# POST Request - used to send HTML form data to the server

@app.route('/',methods = ['POST', "GET"]) # http request. Server receives from client. REST.
def home():
    # return render_template("login.html")
    if request.method == 'POST': # POST - request send html form data from client to server
      return redirect(url_for('logged'))
    # GET most common message sent from client the server returns data
    return render_template("login.html")
# Once logged in
@app.route('/Real_niggas')
def logged():
    # return render_template("index.html")
    return "<h1> Hi </h1>"

if __name__ == "__main__":
    app.run(debug=True)