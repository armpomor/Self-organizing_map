import numpy as np
from math import dist

from config import *


class Som_network:
    def __init__(self):
        self.network = np.random.randint(0, 256, (ROW, COL, 3), int)    # Генерируем клетки с colors
        self.clusters = np.asarray(LIST_CLUSTERS, int)                  # Массив кластеров
        self.t = 0                                                      # Счетчик итераций
        self.winner = None                                              # Кластер-победитель
        self.alpha = 0                                                  # Скорость обучения
    
    def learning_rate(self):
        """
        Alpha - скорость обучения
        """
        self.alpha = pow(LAMBDA, self.t / T) 
        return self.alpha
    
    def win_cluster(self, vector):
        """
        Определяем кластер-победитель и возвращаем его
        """
        f = lambda x: dist(x, vector)
        self.win_index = np.argmin(list(map(f, self.clusters)))
        return self.win_index
    
    def update_weight(self, vector):
        """
        Вычисляем новый кластер и возвращаем новый массив кластеров
        """
        self.win_cluster(vector)
        new = np.asarray(self.clusters[self.win_index] - self.alpha * (self.clusters[self.win_index] - vector), int)
        # Меняем старый кластер на новый
        self.clusters[self.win_index] = new
        return self.clusters
    
    
    def iter_network(self):
        """
        Цикл по сетке
        """
        for i in self.network:
            for j in i:
                self.learning_rate()
                self.update_weight(j)
                
    def run(self):
        for i in range(T):
            self.iter_network()
            self.t += 1
                   

if __name__ == '__main__':
    som = Som_network()
    som.run()
    print(som.clusters)