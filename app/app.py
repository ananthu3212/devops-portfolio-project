from flask import Flask, render_template_string
import socket
import datetime
import os

app = Flask(__name__)


@app.route('/')
def home():
    # Get system information
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # HTML template (simple but looks professional)
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Portfolio</title>
        <style>
            body { font-family: Arial; margin: 40px; background: #f0f0f0; }
            .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 10px; }
            h1 { color: #333; }
            .info { background: #e8f4f8; padding: 15px; border-radius: 5px; }
            .success { color: green; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 DevOps Portfolio Project</h1>
            <div class="info">
                <p><strong>Status:</strong> <span class="success">Application Running Successfully</span></p>
                <p><strong>Hostname:</strong> {{ hostname }}</p>
                <p><strong>IP Address:</strong> {{ ip_address }}</p>
                <p><strong>Current Time:</strong> {{ current_time }}</p>
                <p><strong>Message:</strong> Ready for Junior DevOps Engineer role!</p>
            </div>
            <p><small>Built with Flask • Docker • GitHub Actions • Terraform</small></p>
        </div>
    </body>
    </html>
    """

    return render_template_string(html, hostname=hostname, ip_address=ip_address, current_time=current_time)


@app.route('/health')
def health():
    return {"status": "healthy", "timestamp": str(datetime.datetime.now())}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

