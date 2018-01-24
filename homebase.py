from flask import Flask, render_template,request

from src.vm.MenuVM import MenuVM

app = Flask(__name__)


@app.route('/')
def hello_world():
    menuVm = MenuVM(request.args.get('hey'))
    return render_template("menu.html", vm=menuVm)


if __name__ == '__main__':
    app.run()
