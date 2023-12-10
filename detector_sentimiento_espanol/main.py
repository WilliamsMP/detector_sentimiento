#from sklearn.feature_extraction.text import TfidfVectorizer
import joblib 


model = joblib.load('best_model_espanol')
vect_fit1 = joblib.load('vect_fit_espanol')
## positivo 1, negativo 0
prueba = ['hola estas bien']
prueba_transformado = vect_fit1.transform(prueba)

#model.predict(prueba_transformado)
resultado = model.predict(prueba_transformado)

if resultado == 1: 
    print('Positivo') 
else: print('Negativo') #resultado