from simplekivy import SimpleKivy 
from kivy_matplotlib_widget.graph_widget import MatplotFigure
import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax1= plt.subplots(1, 1)
s = SimpleKivy(make_app=False)

FIRST_DICT = {"size_hint":(.8, .4), "pos_hint":{"center_x":.5}}


graph = MatplotFigure(pos_hint={"center_x":.5})
graph.figure = fig
output_data = [FIRST_DICT,
    graph
]



del s, FIRST_DICT