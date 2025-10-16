import matplotlib.pyplot as plt
import numpy as np

def plotVectors(v_1, v_2, limits=3):
    """Отрисовка наборов двумерных векторов v_1 и v_2"""
    fig, ax = plt.subplots(1, 2)
    fig.set_size_inches(11, 5)
    
    v_1T, v_2T = v_1.transpose(), v_2.transpose()
    size = v_1.shape[0]
    colors = np.array([i for i in range(size)])

    for axis in ax:
        axis.set_xticks([])     # убираются надписи на шкалах
        axis.set_yticks([])     # 
        axis.spines['bottom'].set_position('zero')  # центрирование осей
        axis.spines['left'].set_position('zero')    # в начало координат
        axis.spines['top'].set_visible(False)       # делаем боковые оси
        axis.spines['right'].set_visible(False)     # невидимыми
        axis.set_xlim(-limits, limits)          # область отображения x
        axis.set_ylim(-limits, limits)          # область отображения y

    # отрисовка наборов векторов
    ax[0].scatter(v_1T[0], v_1T[1], marker='.', c=colors, cmap='cividis')
    ax[1].scatter(v_2T[0], v_2T[1], marker='.', c=colors, cmap='cividis')