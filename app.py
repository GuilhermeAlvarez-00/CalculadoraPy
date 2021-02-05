from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")


@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")

    else:
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        opt = request.form["opc"]

        if (num1 == "" or num2 == ""):
             return "Informe um valor válido nos dois campos!"

        else:
            
            
            
            if (opt == 'soma'):
                som = int(num1) + int(num2)
                return str(som)
            elif (opt == 'subt'):
                sub = int(num1) - int(num2)
                return str(sub)
            elif (opt == 'divi'):
                div = int(num1) / int(num2)
                return str(div)
            elif (opt == 'mult'):
                mul = int(num1) * int(num2)
                return str(mul)
    

# criar rota para exibição de erro
@app.errorhandler(404)
def not_found(error):
    return "Essa página não existe!"


app.run(port=4000, debug=True)