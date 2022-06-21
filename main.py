import plotly.graph_objs as go
from som_network import Som_network

from config import T, LAMBDA


som = Som_network()
som.run()

# Сгенерированная сетка
fig_1 = go.Figure(go.Image(z=som.network))
fig_1.update_layout(title=dict(text='Self-organizing map', font=dict(size=20)), margin=dict(l=0, t=30, b=0, r=0))

# Выходная карта цветов
fig_2 = go.Figure(go.Image(z=[som.clusters]))
fig_2.update_layout(title=dict(text='Self-organizing map', font=dict(size=20)), margin=dict(l=0, t=30, b=0, r=0))

# График изменения alpha - скорости обучения
x = []
def alpha():
    for i in range(T):
        x.append(pow(LAMBDA, i / T))
        
alpha()

fig_3 = go.Figure()
fig_3.update_layout(title=dict(text='График изменения скорости обучения', 
                               font=dict(size=20)), margin=dict(l=0, t=30, b=0, r=0))
fig_3.add_trace(go.Scatter(y=x, mode='lines', line=dict(width=3, color='red'), name='alpha'))

fig_1.show()
fig_2.show()
fig_3.show()