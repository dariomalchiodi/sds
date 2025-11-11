import graphviz
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

fig, axes = plt.subplots(3, 4, figsize=(9, 9))
plt.subplots_adjust(wspace=0, hspace=0)

cape_colors = ["pink", "green", "red", "brown"]
suit_colors = ["yellow", "blue", "black"]

heroes = [f'superhero-{suit}-{cape}.png' for suit in suit_colors 
                                         for cape in cape_colors]

for ax, hero in zip(axes.flatten(), heroes):
    ax.imshow(Image.open(hero))
    ax.axis('off')
fig.savefig('superhero-grid.png', dpi=300,
             bbox_inches='tight', transparent=True)


tree = 'digraph { layout="neato" bgcolor="#00000000"'
tree += f's[pos="0,0!" image="superhero.png"'
tree += f'shape=none label="",' +\
        f'width=.5 height=.5 fixedsize="true"]\n'

cape_rho = 1.3
cape_theta = np.linspace(0, np.pi, len(cape_colors))
cape_pos = np.array((cape_rho * np.cos(cape_theta),
                    cape_rho * np.sin(cape_theta))).T

suit_rho = 1
theta_diff = np.pi/2 /(len(suit_colors)+1)
theta_start = 0
theta_end = 2 * np.pi/6
theta_gap = (len(suit_colors) + 1) / len(suit_colors) * np.pi/6

for cape_color, (x, y) in zip(cape_colors, cape_pos):
    tree += f'cap_{cape_color}[pos="{x:.2f},{y:.2f}!" ' + \
            f'image="superhero_{cape_color}.png" label="", ' + \
            'style="invisible" ' +\
            'shape=none ' +\
            'width=.5 height=.5 fixedsize="true"]\n'
    tree += f's -> cap_{cape_color};'



    suit_theta = np.linspace(theta_start, theta_end, len(suit_colors))
    suit_pos = np.array((suit_rho * np.cos(suit_theta),
                            suit_rho * np.sin(suit_theta))).T
    theta_start += theta_gap
    theta_end += theta_gap

    for suit_color, (x_delta, y_delta) in zip(suit_colors, suit_pos):
        tree += f'cap_{cape_color}_costume_{suit_color}' +\
                f'[pos="{x+x_delta:.2f},{y+y_delta:.2f}!", ' +\
                f'image="superhero-{suit_color}-{cape_color}.png", ' + \
                'label="", ' + \
                'shape=none, width=.5 height=.5, fixedsize="true"]\n'
        tree += f'cap_{cape_color} -> cap_{cape_color}_costume_{suit_color};'


tree += '}'


graph = graphviz.Source(tree, format='png')
graph.render(filename='superhero-tree', format='png', cleanup=True)

