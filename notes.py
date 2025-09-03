# from flask import Flask,render_template, request
# from db import Database
# ------------------------------------------------------------------------------------------------
# request is used to handle incoming requests in Flask, similar to how we use req in Express.js.
# ------------------------------------------------------------------------------------------------
# render_template is used to render HTML templates in Flask, but it is not used in this snippet.
# similar to how we use templates in Express.js with res.render().
#-----------------------------------------------------------------------------------------------
# app = Flask(__name__) # Initialize the Flask application
#the name __name__ is a special variable in python that is set to the name of the module in which it is used.
# dbo = Database()
#-----------------------------------------------------------------------------------------------

# @app.route('/') # Define the route for the root URL
# oh so is this similar to the app.get("/") in express?
# Yes, it is similar to app.get("/") in Express.js. It defines a route for the root URL of the application.
# def index():
#     return "hoho hooo ho ho"
# ------------------------------------------------------------------------------------------------

# @app.route('/perform_registration', methods=['POST'])
# we need to specify the method as POST to handle form submissions

# @app.route('/perform_registration', methods=['POST'])
# we need to specify the method as POST to handle form submissions
# def perform_registration():
#     name = request.form.get('username')
#     email = request.form.get('email')
#     password = request.form.get('password')
#     responce = dbo.insert(username=name,email=email,password=password)
#     if responce:
#         return render_template('login.html' , message="Registration successful. Login to proceed")
#     else:
#         return "email already exists"

# {#<!-- similar to dynamic routing in express / ejs  <% %> -->#}
#  <!-- here in flask we have jinja templet  {% %} for that -->
#-----------------------------------------------------------------------------------------------
# app.run(debug=True) # Run the application
# This will start the Flask development server.
# debug=True enables debug mode, which provides detailed error messages and auto-reloads the server on code changes.
# basically  like nodemon in express.
#-----------------------------------------------------------------------------------------------

# db.py -->
    # def search(self, email, password):
    #     """
    #     Searches for a user in the database by email and verifies the password.

    #     Args:
    #         email (str): The email of the user to search for.
    #         password (str): The password to verify for the user.

    #     Returns:
    #         int: Returns 1 if the user exists and the password matches, 
    #              otherwise returns 0.
    #     """
    #     with open ('project/user.json') as file:
    #         data = json.load(file)
    #         if email not in data :
    #             return 0
    #         else:
    #             if data[email]['password'] == password:
    #                 return 1
    #             else: 
    #                 return 0
# -----------------------------------------------------------------------------------
    # <form action="/perform_ner">
    #     <label > Type your text here </label><br>
    #     <textarea name="ner_text"></textarea><br>
    #     <input type="submit" value="Perform NER">
    # </form>

    # action is basically ki jab submit karo then redirect it to /perform_ner (route de rahe hai !)

# how to make sure that only login users can access a route ??
#  by creating a session !!
# import session from flask 
# now check in every route if session is on or off. ..