from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
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

model = LinearRegression()
model.fit(x, y) 

print("Coeficiente angular da reta:", model.coef_[0])
print("Coeficiente linear", model.intercept_) 


preco = model.predict([[35]])

valor = f"R$ {preco[0]:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
print(valor)