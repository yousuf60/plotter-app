from .inputs import data_inputs, ok_btn, data
from .outputs import output_data, plt, graph, fig
import numpy as np


ok_btn.plt = plt
ok_btn.graph = graph
ok_btn.fig = fig

fig.axes[0].plot(np.asarray(data["xlist"], float), data["ylist"], marker=".")
