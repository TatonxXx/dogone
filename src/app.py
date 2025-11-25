from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
     full_id = "67110832"

    student_id = full_id[:2] + "XXXX" + full_id[-4:]

    name = "Tepnarin Hongyok"
    git_url = "https://github.com/TatonxXx/yaimai"
    docker_url = "https://hub.docker.com/r/tatonx/oppa"

    return render_template(
        "index.html",
        name=name,
        student_id=student_id,
        git_url=git_url,
        docker_url=docker_url
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html");

if __name__ =="__main__":
        app.run(host='0.0.0.0', port=80, debug=True)
