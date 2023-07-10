from simplekivy import SimpleKivy 
from kivy_garden_matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

plt.style.use('dark_background')
s = SimpleKivy(make_app=False)

FIRST_DICT = {"size_hint":(.8, .4), "pos_hint":{"center_x":.5}}


graph = FigureCanvasKivyAgg(plt.gcf(), pos_hint={"center_x":.5})
output_data = [FIRST_DICT,
    graph
]



del s, FIRST_DICT