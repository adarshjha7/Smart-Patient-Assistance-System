from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your own secret key

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def authenticate():
    # Perform authentication logic here, e.g., check username and password
    username = request.form.get('username')
    password = request.form.get('password')

    # Debugging: Print username and password
    print(f"Username: {username}, Password: {password}")

    # Check if the provided username and password match
    if username == 'S2AS2' and password == 'S2AS2':
        # Store user information in the session
        session['username'] = username
        print("Login successful")

        # No need to perform redirection here; JavaScript will handle it
        return "Success"  # You can return a response if needed
    else:
        print("Login failed")
        return "Failure"  # You can return a response if needed

if __name__ == '__main__':
    app.run(debug=True)
