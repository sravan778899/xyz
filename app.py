from flask import Flask, render_template, request

app = Flask(__name__)

# Simple rule-based spam keyword checker
def is_spam_email(content):
    spam_keywords = [
        "win", "free", "cash", "prize", "limited time", "act now",
        "click here", "buy now", "offer", "congratulations", "urgent",
        "claim", "guarantee", "risk free", "you have been selected"
    ]
    score = 0
    content = content.lower()
    for keyword in spam_keywords:
        if keyword in content:
            score += 1
    if score == 0:
        return "Not Spam"
    elif score <= 3:
        return "Suspicious"
    else:
        return "Spam"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    email_text = ""
    if request.method == 'POST':
        email_text = request.form['email_text']
        result = is_spam_email(email_text)
    return render_template('index.html', result=result, email_text=email_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
