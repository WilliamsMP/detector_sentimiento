import tkinter as tk
import joblib

def predict_sentiment(text):
    model = joblib.load('best_model_espanol')
    vect_fit = joblib.load('vect_fit_espanol')
    prueba = [text]
    prueba_transformado = vect_fit.transform(prueba)
    resultado = model.predict(prueba_transformado)
    return resultado

def check_sentiment():
    user_input = text_entry.get("1.0", "end-1c")
    result = predict_sentiment(user_input)

    if result == 1:
        sentiment_label.config(text='Sentimiento: Positivo', fg='green')
    else:
        sentiment_label.config(text='Sentimiento: Negativo', fg='red')

def exit_program():
    root.destroy()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Análisis de Sentimiento")

# Marco para la entrada de texto y botones
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Etiqueta para instrucciones
instruction_label = tk.Label(input_frame, text="Ingresa el texto a analizar:", font=('Arial', 12))
instruction_label.pack()

# Entrada de texto
text_entry = tk.Text(input_frame, height=10, width=40)
text_entry.pack(pady=5)

# Botón para predecir sentimiento
predict_button = tk.Button(input_frame, text="Predecir Sentimiento", command=check_sentiment)
predict_button.pack(pady=5)

# Etiqueta para mostrar el sentimiento
sentiment_label = tk.Label(root, text="Sentimiento: ", font=('Arial', 12))
sentiment_label.pack()

# Botón para salir
exit_button = tk.Button(root, text="Salir", command=exit_program)
exit_button.pack(pady=10)

root.mainloop()