from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Flask Deployment Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 2rem;
            line-height: 1.6;
            background: #f7f7f7;
            color: #222;
        }
        .container {
            max-width: 760px;
            margin: 0 auto;
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        }
        h1 {
            margin-top: 0;
        }
        code {
            background: #f0f0f0;
            padding: 0.15rem 0.35rem;
            border-radius: 4px;
        }
        ul {
            padding-left: 1.2rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Flask Deployment Example</h1>
        <p>
            This is a minimal Flask application used as part of a self-hosted deployment example.
        </p>

        <h2>Stack</h2>
        <ul>
            <li>Flask application</li>
            <li>uWSGI application server</li>
            <li>Nginx reverse proxy</li>
            <li>systemd service management</li>
        </ul>

        <h2>Status</h2>
        <p>The application is running correctly through the deployment stack.</p>

        <h2>Purpose</h2>
        <p>
            The purpose of this demo is to show how a simple Python web app can be deployed
            in a more production-oriented way than using <code>flask run</code>.
        </p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
