import numpy as np
import matplotlib.pyplot as plt

# Make a list of adventures, with physical difficulty
#  and time required for adventure.
adventures = [{'name': 'Picnic Rock',
                   'phys': 7,
                   'time': 5},

                  {'name': 'Beaver Lake',
                   'phys': 4,
                   'time': 3},

                  {'name': 'Totem Park',
                   'phys': 1,
                   'time': 2},

                  {'name': 'Alpine Adventure Run',
                   'phys': 9,
                   'time': 2},

                  {'name': 'Shelikof',
                   'phys': 7,
                   'time': 8},

                  {'name': 'Sam Sing',
                   'phys': 2,
                   'time': 8},

              ]

y = [dict['phys'] for dict in adventures]
x = [dict['time'] for dict in adventures]
labels = [dict['name'] for dict in adventures]

fig, ax = plt.subplots()
fig.suptitle('PHS Adventure Matrix')
ax.set_xlabel('Time')
ax.set_ylabel('Physical Difficulty')

# Can just place labels, rather than plotting invisilbe points.
#  See: http://stackoverflow.com/questions/14827650/pyplot-scatter-plot-marker-size
ax.scatter(x,y, s=0)

for i, txt in enumerate(labels):
    ax.annotate(txt, (x[i], y[i]))


plt.show()
