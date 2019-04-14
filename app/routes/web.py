from app import app, render_template


@app.route("/", methods=["GET"])
def main():
    print("OI CAMILA")
    return render_template("main_module/index.html")
