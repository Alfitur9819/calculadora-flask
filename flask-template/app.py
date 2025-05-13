# filepath: c:\Users\Alfonso Iturbide\calculadora-web\flask-template\app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Obtener datos del formulario
        unidad = request.form['unidad']
        nombreUnidad = request.form['nombreUnidad']
        precio = float(request.form['precio'])
        enganche = float(request.form['enganche'])
        meses = int(request.form['meses'])

        # Determinar el interés según la unidad
        interes_anual = 0.0987 if unidad == 'Auto' else 0.1349
        interes_mensual = interes_anual / 12

        # Calcular el monto restante después del enganche
        monto_restante = precio - enganche

        # Calcular la mensualidad usando la fórmula estándar
        mensualidad = (monto_restante * interes_mensual * (1 + interes_mensual) ** meses) / \
                      ((1 + interes_mensual) ** meses - 1)

        # Renderizar la plantilla con los resultados
        return render_template(
            'home.html',
            nombreUnidad=nombreUnidad,
            precio=precio,
            enganche=enganche,
            mensualidad=round(mensualidad, 2),  # Redondear a 2 decimales
            meses=meses
        )
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)