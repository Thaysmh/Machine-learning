#Exercício 1: Previsão de Vendas por Investimento em Marketing (Regressão Linear Simples)
#Contexto: Você quer prever as vendas de um produto (em milhares de unidades) com base no valor investido em anúncios no Instagram (em milhares de reais).

#X (Input): Investimento em marketing (R$)

#Y (Output): Vendas feitas (Unidades)

#Desafio: Treine o modelo e preveja quantas vendas serão feitas com um investimento de R$ 45,00.

from sklearn.linear_model import LinearRegression

x = [
  [45],
  [45],
  [45],
  [35],
  [35],
  [42],
  [42],
  [45]
]

y = [
  1,
  1,
  2,
  0,
  1,
  1,
  2,
  3
]

model = LinearRegression() # Executa a instância da classe LinearRegression

model.fit(x, y)

print("Coeficiente angular da reta:", model.coef_[0]) # Coeficiente angular da reta
print("Coeficiente linear", model.intercept_) # Coeficiente linear da reta

previsao = model.predict([[45]])

print(previsao)