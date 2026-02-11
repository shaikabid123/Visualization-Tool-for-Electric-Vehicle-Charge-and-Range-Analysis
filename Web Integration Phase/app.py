from flask import Flask, render_template, request

# Initialize the Flask app
# We tell Flask to map the URL '/assets' to your 'static/assets' folder
app = Flask(__name__, static_url_path='/assets', static_folder='static/assets')

@app.route('/')
def home():
    # Flask looks inside the 'templates' folder for index.html
    return render_template('index.html')

# This route intercepts the contact form submission from your HTML
@app.route('/forms/contact.php', methods=['POST'])
def contact():
    # Extract the data submitted by the user
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    # Print the data to the command prompt terminal
    print("\n--- NEW CONTACT FORM SUBMISSION ---")
    print(f"Name:    {name}")
    print(f"Email:   {email}")
    print(f"Subject: {subject}")
    print(f"Message: {message}")
    print("-----------------------------------\n")

    # The template's JavaScript expects the exact string "OK" to show the success message
    return "OK"

if __name__ == '__main__':
    # Run the server in debug mode
    app.run(debug=True, port=5000)
