import json

from flask import Flask
from flask import render_template
from flask import request

from castle.castle import Castle

app = Flask(__name__)

api_secret = '<PUT_YOUR_API_SECRET_HERE>'

@app.route('/')
def index():
    request_metadata = {
        'X-Castle-Ip': request.remote_addr,
        'X-Castle-Cookie-Id': request.cookies.get('__cid'),
        'X-Castle-Headers': json.dumps({
            'Accept': request.headers.get('ACCEPT'),
            'Accept-Encoding': request.headers.get('ACCEPT_ENCODING'),
            'Accept-Language': request.headers.get('ACCEPT_LANGUAGE'),
            'User-Agent': request.headers.get('USER_AGENT'),
        })
    }
    castle = Castle(api_secret=api_secret, request_metadata=request_metadata)
    castle.track(name='$login.succeeded', user_id='<PUT_A_FAKE_USER_ID_HERE>')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8181)
