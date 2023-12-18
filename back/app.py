import json
from flask import Flask, render_template, request
api = Flask(__name__)

my_email = "waga.baga@gmail.com"
my_email2= "nadavgever@gmail.com"
my_email3= "guygever@gmail.com"
username = "shonbaron"
password = "1234"
ar= [ "shon","guy","nadav"]
users =[]
name = 'shon'
users_file = 'users.json'

    

def load_data(users):# load a list from a file
    
    try:
        with open(users, 'r') as file:
            json_string = file.read()
            users = json.loads(json_string)
    except: pass
    users=[]


@api.route('/')
def hello():
    return 'Hello, World!'

@api.route('/about')
def about():
    return render_template("index.html",data=my_email)

@api.route('/les')
def les():
    return render_template("about.html", context={"myemail":'waga.baga@gmail.com',"ar":ar,"my_email2":'nadavgever@gmail.com',"my_email3":"guygever@gmail.com"})







@api.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        req_username = request.form.get('username')
        req_password = request.form.get('password')
        for user in users:
            if (req_username == user['username']  and  user['password'] == req_password):

                return render_template('success.html' , req_username == username)
    else:
        return render_template('login.html')
       
      

@api.route('/signup', methods=['GET', 'POST'])
def signup():
    global password
    if request.method == 'POST':
        username = request.form.get('username')
        email= request.form.get('email')
        password = request.form.get('password')

        for user in users : 
            if user["username"]== username:
                errormsg ='username is allready registered'
                return render_template('signup.html', errormsg=errormsg)
            
        users.append({'username' : username, 'password': password, 'email':email })

        with open(users_file, 'w') as file:
    # Use json.dump() to write the data to the file
            json.dump(users, file)

        # Add your signup logic here
        # Example: Store the user information in a database

        return render_template('success.html')
    


    return render_template('signup.html')







if __name__ == '__main__':
    api.run(debug=True)



