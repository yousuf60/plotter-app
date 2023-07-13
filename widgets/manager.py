from simplekivy import SimpleKivy 

s = SimpleKivy(make_app=False)

class PlotManager(s.ScreenManager):pass

class scr(s.Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.name)
