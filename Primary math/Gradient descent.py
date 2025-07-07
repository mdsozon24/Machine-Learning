import numpy as np

def gradient_descent(x,y):
    m_crr = b_crr = 0
    learning_rate = 0.01
    n = len(x)
    for i in range(1000):
        y_pred = m_crr * x + b_crr
        cost = (1/n) * sum([val**2 for val in (y - y_pred)])
        md = -(2/n) * sum(x * (y - y_pred))
        bd = -(2/n) * sum((y - y_pred))
        m_crr -= learning_rate * md
        b_crr -= learning_rate * bd
        print("m {}, b {}, cost {}".format(m_crr, b_crr, cost))

x = np.array([1,2,3,4,5])
y = [5,7,9,11,13]

gradient_descent(x,y)