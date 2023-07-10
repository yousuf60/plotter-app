from simplekivy import SimpleKivy 
import numpy as np

from data import DataManager

FIRST_DICT = {"size_hint":(1, .35), "orientation":"vertical"}
SECOND_DICT = {"size_hint":(1, None), "height":"70dp", "padding":[0,"4dp"]}
BTN_KWARGS = {"size_hint":(.4, None), "height":"50dp", "background_color":(.8, .8, .8, .7)}
INPUT_KWARGS = {"hint_text": "only numsbers", "multiline": False, "background_color": (1, 1, 1, .9)}
STEP = 1
DATA_FILE = "data.json"

s = SimpleKivy(make_app=False)
dataManager = DataManager(DATA_FILE)

def x_input_text():
    xlist = data["xlist"]
    if xlist and digit_render(xlist[-1]):
        return str(digit_render(xlist[-1])+STEP)
    else:
        return "0"
    
def digit_render(num):
    try:
        if str(num).isnumeric():
            return int(num)
        return float(num)
    except:
        return 0

def update_plot():
    ok_btn.plt.clf()
    ok_btn.plt.plot(np.asarray(data["xlist"], float), data["ylist"])
    ok_btn.graph.draw()

def ok(instance=None):
    global data
    s = SimpleKivy(make_app=False)
    xs = digit_render(x_input.text)
    if xs == 0:
        xs = "0"
    ys = digit_render(y_input.text)
    if all((xs, ys)):
        data["xlist"].append(xs)
        data["ylist"].append(ys)
        dataManager.write_data(data)
        x_input.text = str(digit_render(xs) + STEP)
        y_input.text = ""
        update_plot()
    y_input.focus = True
        

def clear_data():
    global data
    data = {"xlist":[], "ylist":[]}
    dataManager.write_data(data)
    update_plot()
    x_input.text = "0"
    y_input.text = ""

def pop_data():
    if data["xlist"] and data["ylist"]:
        del data["xlist"][-1], data["ylist"][-1]
        dataManager.write_data(data)
        update_plot()
        x_input.text = x_input_text()
 

data = {"xlist":[], "ylist":[]}

if not dataManager.file_exists(DATA_FILE):
    dataManager.write_data(data)

data = dataManager.read_file()
xlist = data["xlist"]



x_input = s.TextInput(text=x_input_text(), **INPUT_KWARGS)
y_input = s.TextInput(**INPUT_KWARGS, text_validate_unfocus = False,)

y_input.bind(on_text_validate=ok)


ok_btn = s.Button(text="ok", **BTN_KWARGS)
claer_btn = s.Button(text="clear", **BTN_KWARGS)
pop_btn = s.Button(text="pop", **BTN_KWARGS)

ok_btn.on_release = lambda:ok()
claer_btn.on_press = lambda:clear_data()
pop_btn.on_press = lambda:pop_data()


data_inputs = [FIRST_DICT,
        [SECOND_DICT,
            x_input, s.Label(text="x axis")
        ],
        [SECOND_DICT,
            y_input, s.Label(text="y axis")
        ],
        #{"size_hint":(1, 1)},
        ({"pos_hint":{"center_y":1}},
            [{"spacing":"20dp", "padding":["30dp", 0], "pos_hint":{"center_y":1}},
            ok_btn,
            pop_btn,

            claer_btn

        ]),    
    ]




del s, FIRST_DICT, SECOND_DICT, BTN_KWARGS, INPUT_KWARGS, xlist