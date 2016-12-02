# Castle.io Python Library

So the tricky thing about this is the request metadata, which is totally necessary for good tracking, has to be fed in manually on initialization. There's a demo in the little flask app showing how to handle it with Flask's awesome reqeust module, but the general idea is:

```
import json
from flask import request
from castle.castle import Castle

api_secret = '<YOUR_API_SECRET>'
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
castle.track(name='$login.succeeded', user_id='<PUT_A_USER_ID_HERE>')
```

To verify, add your `app_id`, `api_secret`, and a fake `user_id` in the appropriate places in `flask_demo_server.py`. Start it up with `python flask_demo_server.py` and visit `localhost:8181`. Refresh the page so Castle has a chance to recognize the cookie, and verify through Castle's dashboard that a user with your fake id has been tracked.

### License: MIT
