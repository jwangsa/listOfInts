from flask import Flask, render_template, request

app = Flask(__name__)

def combo(num, target, part = []):
    s = sum(part)
    if s == target:
        return part
    if s >= target:
        return None
    for i in range(0, len(num)):
        n = num[i]
        remaining = num[i+1:]
        result = combo(remaining, target, part + [n])
        if result is not None:
            return result
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/find_combination", methods=["POST"])

def find_combination():
    try:
        num = [float(x.strip()) for x in request.form["num"].split(",")]
        target = float(request.form["target"])
        result = combo(num, target)
        if result is not None:
            result_int = [int(x) if x.is_integer() else x for x in result]
            result_str = ", ".join([f"{y}" for y in result_int])
            return render_template("result.html", result=result_str)
        else:
            return render_template("result.html", result="No combination found")
    except ValueError:
        return render_template("error.html", message="Please enter a valid input")

if __name__ == "__main__":
    app.run(debug=True)