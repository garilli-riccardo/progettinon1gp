from flask import Flask 
 

app = Flask(__name__) 
lista_spesa = []

@app.route('/') 
def home(): 
 return "Per ora funziona tutto" 

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    x = input()
    lista_spesa.append(x)
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista_spesa):
    lista_spesa.pop(indice - 1)
    return redirect(url_for('home'))

@app.route('/svuotalista', methods=['POST'])
def svuotalista():
    lista_spesa.clear()
    return redirect(url_for('home'))

#avvio dell'app Flask 
if __name__ == '__main__': 
    app.run(debug=True)