"""
Python for web development

We have many web frameworks in python
-flask
-django
-fastapi
many more
"""

"""
We are discussing, flask-framework
"""

"""
Using flask-framework,
1. Using flask-framework, we can develop websites
2. Using flask-framework, we can develop REST-API
3. Using flask-framework, we can develop Microservices
"""

"""
Here, 
We will discuss,
How to use flask-framework to create REST-API
"""

"""
Just to understand REST-API/API

Example:
Suppose if we want to provide access to our-database
then how we can provide access to others/public?

One option, we can create separate credetials with restricted permissions
and we can share with others

This OPTION is LIMITED
"""

"""
We got 2 solutions
1. SOAP: Simple Object Access Protocol
2. REST: REpresentational State Transfer

both are called architectures/designs/styles

both tells to introduce some DOOR/GATE/INTERFACE between
our-app/db with others
It is like,

our-app/db  <--INTERFACE -->  others/public
This INTERFACE is also called as APPLICATION PROGRAMMING INTERFACE(API)

both tells how to write such INTERFACE

"""

"""
REST came after SOAP
- REST is easy to implement
- REST popular
"""
"""
To create REST-API, we no need to implement REST architecture
from the scratch.
BECAUSE
flask-framework is already REST architecture,
SO,
we just need to know, how to create REST-API using flask
"""

"""
To run any web application/api, we need WEB SERVER.

flask-framework has builtin web server
- this builtin web server, we can use it for development purpose only
- for production, we need to make use of some other PRODUCTION server
"""

"""
Assume, we are planning to provide full-access/complete-access
to our DB my_database.db

full-access/complete-access means
- Creating new record in our table
- Reading existing records from our table
- Updating existing records in our table
- Deleting existing records from our table 
"""

"""
HTTP web standards: 
Http methods: GET, POST, PUT, PATCH, DELETE

POST        - Creating new record in our table
GET         - Reading existing records from our table
PUT/PATCH   - Updating existing records in our table
DELETE      - Deleting existing records from our table 
"""

"""
In this release, we are planning create REST-API
to get db data
PLANNED END POINT: http://127.0.0.1:5000/getdbdata
"""

# ---------
# Create APP
###########
import flask
# my_rest_api_app = flask.Flask("Any Name")
my_rest_api_app = flask.Flask(__name__) # This will display file name
#######################

# ---------
# END POINT - 1: GET db data API
# PLANNED END POINT: http://127.0.0.1:5000/getdbdata
###########
@my_rest_api_app.route("/getdbdata", methods=["GET"])
def get_db_data_api_function():
    import sqlite3
    my_db_connection = sqlite3.connect(r"C:\python_training\rest_api\my_database.db")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("SELECT * FROM MY_TABLE")
    my_db_result = my_db_cursor.fetchall()
    return flask.jsonify(my_db_result)
#######################

# ---------
# Run builtin server
###########
my_rest_api_app.run() # default host='127.0.0.1', port=5000
# my_rest_api_app.run(host='', port='')
#######################