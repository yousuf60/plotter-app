from .inputs import data_inputs, ok_btn, data
from .outputs import output_data, plt, graph
import numpy as np
ok_btn.plt = plt
ok_btn.graph = graph
plt.plot(np.asarray(data["xlist"], float), data["ylist"])
