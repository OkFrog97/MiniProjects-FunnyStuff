def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or  -1
    
'''
h - высота этажа с которого бросают мяч
bounce -  отскок до 2/3 от высоты этажа с которого бросают мяч
window - высота окна

пока высота больше окна
    счетчик +1
    уменьшаем высоту на отскок
    
'''