import os
import secrets
from pathlib import Path

from flask import Flask

# sys.path.append("../")

app = Flask(__name__)

_secret_key_file = Path(__file__).resolve().parents[2] / "data" / ".flask_secret_key"
if os.environ.get("FLASK_SECRET_KEY"):
    app.secret_key = os.environ["FLASK_SECRET_KEY"]
else:
    _secret_key_file.parent.mkdir(parents=True, exist_ok=True)
    if not _secret_key_file.exists():
        _secret_key_file.write_text(secrets.token_hex(32))
    app.secret_key = _secret_key_file.read_text().strip()

from dao.webserver.app.routes import *


#  if __name__ == '__main__':
#      app.run()
#  app.run(port=5000, host='0.0.0.0')
#  if __name__ == '__main__':
#      app.run(port=5000, host='0.0.0.0')
