from pathlib import Path
import platform
import random
import string
import subprocess
from flask import Flask, render_template, request, redirect

IS_WINDOWS = platform.system() == "Windows"
if IS_WINDOWS:
    BASE_DIR = "..\\files"
else:
    BASE_DIR = "/tmp/files"

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
Path(BASE_DIR).mkdir(parents=True, exist_ok=True)


def gen_id(size: int = 6, chars: str = string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def list_files(fdir: str | None):
    if not fdir:
        fdir = BASE_DIR

    cmd = "ls"
    if platform.system() == "Windows":
        cmd = "dir"

    return subprocess.check_output(cmd + " " + fdir, shell=True)


def get_content(fname: str | None) -> str:
    if not fname:
        return ""

    try:
        with open(BASE_DIR + "/" + fname) as f:
            return f.read()
    except:
        return "error occured, not found?"


@app.get("/view")
def view_paste():
    paste_id = request.args.get("id")
    content = get_content(paste_id)

    return render_template("paste.html", paste_id=paste_id, content=content)


@app.post("/new")
def new_paste():
    content = request.form.get("content")
    if not content:
        return redirect("/")

    id = gen_id(32)
    with open(f"{BASE_DIR}/{id}.txt", "w") as f:
        f.write(content)

    return redirect(f"/view?id={id}.txt")


@app.route("/")
def home():
    fdir = request.args.get("fdir")
    return render_template(
        "index.html",
        content=list_files(fdir).decode(),
    )
