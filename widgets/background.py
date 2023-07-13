background = """
#: import get_color_from_hex kivy.utils.get_color_from_hex
FloatLayout:
    BoxLayout:
        canvas.before:
            Color:
                rgba: get_color_from_hex("#00dcd2")
            Rectangle:
                pos: self.pos
                size: self.size

    FloatLayout:
        size_hint: 1, .6
        canvas.after:
            Color:
                rgba: get_color_from_hex("#12e1f1")
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [100, 0, 0, 0]

                
    FloatLayout:
        size_hint: 1, .2
        pos_hint: {"center_y": 0}
        canvas.after:
            Color:
                rgba: get_color_from_hex("#69f0ea")
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [0, 100, 0, 0]

                
"""