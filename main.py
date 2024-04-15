from flask import Flask, render_template_string

app = Flask(__name__)

html_content = '''
<!DOCTYPE html>
<html>

<head>
    <title>Guess That Movie</title>
    <style>
        body {
            text-align: center;
        }
        input[type="text"] {
            padding: 10px;
            font-size: 16px;
            margin-bottom: 10px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h1>Guess that Movie!</h1>
    <p>Sample Text.</p>
    <input type="text" placeholder="Enter your guess">
    <br>
    <button>Submit</button>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)