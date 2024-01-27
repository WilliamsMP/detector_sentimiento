import joblib

def predict_sentiment(text):
    model = joblib.load('best_model_espanol')
    vect_fit = joblib.load('vect_fit_espanol')
    prueba = [text]
    prueba_transformado = vect_fit.transform(prueba)
    resultado = model.predict(prueba_transformado)
    return resultado

def write_input_to_predictor():
    user_input = input("Ingresa el texto para predecir el sentimiento: ")
    result = predict_sentiment(user_input)

    if result == 1:
        print('Sentimiento: Positivo')
    else:
        print('Sentimiento: Negativo')

def exit_program():
    print("Saliendo del programa...")
    exit()

menu = {
    "1": {"description": "Predecir Sentimiento", "function": write_input_to_predictor},
    "2": {"description": "Salir", "function": exit_program}
}

def show_menu():
    print("----- Menú -----")
    for option, data in menu.items():
        print(f"{option}. {data['description']}")
    print("----------------")

if __name__ == "__main__":

    while True:
        show_menu()
        choice = input("Elige una opción: ")
        if choice in menu:
            menu[choice]["function"]()
        else:
            print("Opción inválida. Por favor, elige una opción válida.")
            print()