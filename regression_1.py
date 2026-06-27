from sklearn.linear_model import LinearRegression

# Prever o preço de uma casa

x = [
  [34],
  [42],
  [50],
  [80],
  [100],
  [120],
  [110],
  [125]
]

y = [
  160000,
  170000,
  250000, 
  420000, 
  500000,
  700000,
  800000,
  850000
]

model = LinearRegression() # Executa instância da classe LinearRegression
model.fit(x, y) # Treina o model com os dados x e y

print("Coeficiente angular da reta:", model.coef_[0]) # Coeficiente angular da reta
print("Coeficiente linear", model.intercept_) # Coeficiente linear da reta

# O método predict() retorna uma array, mesmo que seja solicitado a previsão
# de apenas um valor.
preco = model.predict([[35]])

valor = f"R$ {preco[0]:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
print(valor)