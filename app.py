from flask import Flask, render_template, request, redirect, url_for, session
import secrets
# Generate a random 16-byte key and convert it to a hexadecimal string
secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.secret_key = secret_key  # Replace with your actual secret key

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        
        # Dummy authentication - replace with your actual authentication logic
        if username == 'avishek' and password == '1234' and role in ['student', 'teacher', 'parent', 'admin']:
            session['username'] = username
            session['role'] = role

            if role == 'student':
                return redirect(url_for('student_dashboard'))
            elif role == 'teacher':
                return redirect(url_for('teacher_dashboard'))
            elif role == 'parent':
                return redirect(url_for('parent_dashboard'))
            elif role == 'admin':
                return redirect(url_for('admin_dashboard'))
        else:
            return "Invalid credentials"
    
    return render_template('login.html')

@app.route('/student-dashboard')
def student_dashboard():
    return render_template('student_dashboard.html')

@app.route('/teacher-dashboard')
def teacher_dashboard():
    return render_template('teacher_dashboard.html')

@app.route('/parent-dashboard')
def parent_dashboard():
    return render_template('parent_dashboard.html')

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/logout')
def logout():
    # Clear user session or perform logout logic here
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
