import os
import matplotlib.pyplot as plt
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
@app.route('/inicio')
def inicio():

    for item in os.listdir('static'):
        if item in os.listdir('static'):
            if item != 'fontAwesome':
                os.remove(f'static/{item}')

    return render_template('app.html')


@app.route('/resposta', methods=['POST'])
def resposta():

    t = list()
    i = 0
    while True:
        if request.form.get(f'time{str(i)}') is None:
            break
        else:
            t.append(request.form.get(f'time{str(i)}'))
            i += 1

    resultA = list()
    i = 0
    while True:
        if request.form.get(f'resulta{str(i)}') is None:
            break
        else:
            resultA.append(float(request.form.get(f'resulta{str(i)}')))
            i += 1

    resultB = list()
    i = 0
    while True:
        if request.form.get(f'resultb{str(i)}') is None:
            break
        else:
            resultB.append(float(request.form.get(f'resultb{str(i)}')))
            i += 1

    resultC = list()
    i = 0
    while True:
        if request.form.get(f'resultc{str(i)}') is None:
            break
        else:
            resultC.append(float(request.form.get(f'resultc{str(i)}')))
            i += 1

    result = list()
    for i in range(len(t)):
        result.append((resultA[i] + resultB[i] + resultC[i]) / 3)

    plt.plot(t, result)
    plt.savefig('static/graph.png')

    return render_template('grafico.html')


if __name__ == '__main__':
    app.run(debug=True)
