from simplekivy import SimpleKivy 
import numpy as np

import os.path

from data import DataManager

STEP = 1


class inputs:
    def __init__(self, file_name):
        s = SimpleKivy(make_app=False)
        self.dataManager = DataManager(file_name)
        self.data = {"xlist":[], "ylist":[]}
        if not self.dataManager.file_exists(file_name):
            self.dataManager.write_data(file_name)

        self.data = self.get_data()
        self.xlist = self.data["xlist"]
        self.title_label = s.Label(text=os.path.splitext(file_name)[0], pos_hint={"center_y":.1}, font_size="19dp")
    def get_data(self):
        return self.dataManager.read_file()

    def x_input_text(self):
        xlist = self.data["xlist"]
        if xlist and self.digit_render(xlist[-1]):
            return str(self.digit_render(xlist[-1])+STEP)
        else:
            return "0"
        
    def digit_render(self, num):
        try:
            if str(num).isnumeric():
                return int(num)
            return float(num)
        except:
            return 0

    def update_plot(self):
        graph = self.ok_btn.graph
        fig = self.ok_btn.fig
        xlist = np.asarray(self.data["xlist"], float)
        if fig.axes[0].lines:
            fig.axes[0].lines[0].set_data(xlist, self.data["ylist"])
        else:
            fig.axes[0].plot(xlist, self.data["ylist"])
        if self.data["xlist"]:
            graph.xmin = min(xlist)
            graph.xmax = max(xlist)
            graph.ymin = min(self.data["ylist"])
            graph.ymax = max(self.data["ylist"]) 
        else:
            graph.xmin = graph.ymin = 0
            graph.xmax = graph.ymax = 1
            
        graph.home()

        
    def ok(self, instance=None):
        s = SimpleKivy(make_app=False)
        xs = self.digit_render(self.x_input.text)
        if xs == 0:
            xs = "0"
        ys = self.digit_render(self.y_input.text)
        if all((xs, ys)):
            self.data["xlist"].append(xs)
            self.data["ylist"].append(ys)
            self.dataManager.write_data(self.data)
            self.x_input.text = str(self.digit_render(xs) + STEP)
            self.y_input.text = ""
            self.update_plot()
        self.y_input.focus = True
            

    def clear_data(self):
        
        self.data = {"xlist":[], "ylist":[]}
        self.dataManager.write_data(self.data)
        self.update_plot()
        self.x_input.text = "0"
        self.y_input.text = ""
        self.y_input.focus = True

    def pop_data(self):
        if self.data["xlist"] and self.data["ylist"]:
            del self.data["xlist"][-1], self.data["ylist"][-1]
            self.dataManager.write_data(self.data)
            self.update_plot()
            self.x_input.text = self.x_input_text()
        self.y_input.text = ""

    def start(self):
        s = SimpleKivy(make_app=False)
        FIRST_DICT = {"size_hint":(1, .35), "orientation":"vertical"}
        SECOND_DICT = {"size_hint":(1, None), "height":"70dp", "padding":[0,"4dp"]}
        BTN_KWARGS = {"size_hint":(.4, None), "height":"50dp", "background_color":(.8, .8, .8, .7)}
        INPUT_KWARGS = {"hint_text": "only numsbers", "multiline": False, "background_color": (1, 1, 1, .9)}

        self.x_input = s.TextInput(text=self.x_input_text(), **INPUT_KWARGS)
        self.y_input = s.TextInput(**INPUT_KWARGS, text_validate_unfocus = False,)

        self.y_input.bind(on_text_validate=self.ok)
        self.y_input.focus = True

        self.ok_btn = s.Button(text="ok", **BTN_KWARGS)
        self.clear_btn = s.Button(text="clear", **BTN_KWARGS)
        self.pop_btn = s.Button(text="pop", **BTN_KWARGS)
        self.swich_btn = s.Button(text="switch", background_color=(1, 1, 1, .7), size_hint=(.3, None), height="50dp")

        self.ok_btn.on_release = lambda:self.ok()
        self.clear_btn.on_release = lambda:self.clear_data()
        self.pop_btn.on_press = lambda:self.pop_data()


        data_inputs = [FIRST_DICT,
                [SECOND_DICT,
                    self.x_input, s.Label(text="x axis")
                ],
                [SECOND_DICT,
                    self.y_input, s.Label(text="y axis")
                ],
                #{"size_hint":(1, 1)},
                ({"pos_hint":{"center_y":1}},
                    [{"spacing":"20dp", "padding":["30dp", 0], "pos_hint":{"center_y":1}},
                    self.ok_btn,
                    self.pop_btn,
                    self.clear_btn,
                    self.swich_btn

                ],
                self.title_label),
                    
            ]
        return data_inputs


