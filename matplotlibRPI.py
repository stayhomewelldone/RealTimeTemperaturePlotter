import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()
x = []
temp = []


style.use('fivethirtyeight')
fig = plt.figure(num='Temperature', figsize=[13,3])
ax1 = fig.add_subplot(1,1,1)

def get_sense_data():
    sense_data = []
    temp2 = sense.get_temperature()
    dt = datetime.now()

    temp.append(temp2)
    sense_data.append(temp2)
    x.append(dt)
    sense_data.append(dt)

    return sense_data

def animate(i):
    data = get_sense_data()
    ax1.clear()
    ax1.plot(x, temp)
    ax1.legend(['Temperature ' + chr(176)+ 'C', 'Humidity %'])
    print(data)

ani= animation.FuncAnimation(fig, animate, interval=10000)
plt.show()
