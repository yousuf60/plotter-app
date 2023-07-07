from simplekivy import SimpleKivy 
from data import DataManager

DATA_FILE = "data.json"
dataManager = DataManager()
data = {"xlist":[], "ylist":[]}
if not dataManager.file_exists(DATA_FILE):
    dataManager.write_data(DATA_FILE, data)

data = dataManager.read_file(DATA_FILE)
print(data)
s = SimpleKivy(make_app=False)

FIRST_DICT = {"size_hint":(1, .35), "orientation":"vertical"}
SECOND_DICT = {"size_hint":(1, None), "height":"70dp", "padding":"4dp"}

axis_input = s.TextInput(hint_text="only numsbers", multiline=False)
yis_input = s.TextInput(hint_text="only numsbers", multiline=False)
ok_btn = s.Button(text="ok", size_hint=(.4, None), height="50dp", pos_hint={"center_x":.5, "center_y":.7})

ok_btn.on_press = lambda:ok()

data_inputs = [FIRST_DICT,
        [SECOND_DICT,
            axis_input, s.Label(text="axis")
        ],
        [SECOND_DICT,
            yis_input, s.Label(text="wyis")
        ],
        ({"size_hint":(1, 1)},
            ok_btn),    
    ]

def ok():
    s = SimpleKivy(make_app=False)
    xs = axis_input.text
    ys = yis_input.text
    if all((xs.isnumeric(), ys.isnumeric())):
        data["xlist"].append(xs)
        data["ylist"].append(ys)
        print(data)
        ok_btn.output.text = str(xs)


del s, FIRST_DICT, SECOND_DICT