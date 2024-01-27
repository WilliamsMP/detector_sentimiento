import joblib

def predict_sentiment(text):
    model = joblib.load('best_model_ingles')
    vect_fit = joblib.load('vect_fit_ingles')
    prueba = [text]
    prueba_transformado = vect_fit.transform(prueba)
    resultado = model.predict(prueba_transformado)
    return resultado

def write_input_to_predictor():
    user_input = input("Enter text to predict sentiment: ")
    result = predict_sentiment(user_input)

    if result == 'POSITIVO':
        print('Sentiment: Positive')
    else:
        print('Sentiment: Negative')

def exit_program():
    print("Leaving the program...")
    exit()

menu = {
    "1": {"description": "Predict Sentiment", "function": write_input_to_predictor},
    "2": {"description": "Exit", "function": exit_program}
}

def show_menu():
    print("----- Menu -----")
    for option, data in menu.items():
        print(f"{option}. {data['description']}")
    print("----------------")

if __name__ == "__main__":

    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice in menu:
            menu[choice]["function"]()
        else:
            print("Invalid option. Please choose a valid option.")
            print()