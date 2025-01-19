from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock user database
users = [
    {"email": "zhengpou@gmail.com", "password": "phpzindabad", "username": "callmecj_3"},
    {"email": "asharjaffery7@gmail.com", "password": "gptzindabad", "username": "muhammad.ashar7"}
]

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_or_username = request.form.get('email_or_username')
        password = request.form.get('password')

        # Check email or username
        for user in users:
            if user["email"] == email_or_username or user["username"] == email_or_username:
                if user["password"] == password:
                    flash(f"Welcome back {user['username']}!", "success")
                    return redirect(url_for('home'))
                else:
                    flash("Incorrect password!", "danger")
                    return redirect(url_for('login'))
        flash("No account found with those credentials!", "danger")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        # Add new user to the database
        users.append({"email": email, "password": password, "username": username})
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
