from flask import Flask, abort
import os
import subprocess

app = Flask(__name__)


@app.route('/')
def home():
    return """<html><body><h1>Hello, world!</h1></body></html>"""

@app.route('/gitinfo')
def gitinfo():
    GITINFO_FILE_PATH="gitinfo.txt"

    if os.path.exists(GITINFO_FILE_PATH):
        with open(GITINFO_FILE_PATH) as fd:
            gitinfo_text = "\n".join(fd.readlines())
            return gitinfo_text
    elif os.path.exists(".git"):
        try:
            proc = subprocess.run(["git", "show", "-s"], stdout=subprocess.PIPE)
            return proc.stdout.decode("utf8")
        except:
            abort(500)
    else:
        abort(404)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)