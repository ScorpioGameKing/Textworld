from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from database import WorldDatabase

class LoadedSaveBtn(Button):

    def __init__(self, world, **kwargs):
        super(LoadedSaveBtn, self).__init__(**kwargs)
        self.id = world
    
    def on_press(self):
        print(f"On_Press Parent {self.parent.parent.parent.parent.parent}")
        self.parent.parent.parent.parent.parent.loadSaveMenuCall(self.id)
        return super().on_press()

class TextworldLdSaveView(BoxLayout):

    def updateWorldList(self, db):
        self.worlds = db.load_save_names()
        print(f"Children: {self.children} Count: {len(self.children)} db Count: {len(self.worlds)}")
        for i in range(len(self.worlds)):
            if len(self.children) > 0:
                if self.children[i - 1].text == self.worlds[i - 1]:
                    continue
                else:
                    btn = LoadedSaveBtn(world=self.worlds[i - 1], text=self.worlds[i - 1])
                    self.ids[f'{self.worlds[i - 1]}'] = btn
                    self.add_widget(btn)
            else:
                btn = LoadedSaveBtn(world=self.worlds[i - 1], text=self.worlds[i - 1])
                self.ids[f'{self.worlds[i - 1]}'] = btn
                self.add_widget(btn)
        print(f"Layout Children: {self.ids}")
        

class TextworldLdBackBtn(Button):
    pass

class TextworldLdLeftPanel(BoxLayout):
    save_view = ObjectProperty(None)
    back_btn = ObjectProperty(None)

class TextworldLdDeleteBtn(Button):
    pass

class TextworldLdLoadBtn(Button):
    pass

class TextworldLdOptions(BoxLayout):
    delete = ObjectProperty(None)
    load = ObjectProperty(None)

class TextworldLdInfoPanel(BoxLayout):
    pass

class TextworldLdRightPanel(BoxLayout):
    info_panel = ObjectProperty(None)
    options = ObjectProperty(None)

class TextworldLdMenuLayout(BoxLayout):
    left_panel = ObjectProperty(None)
    right_panel = ObjectProperty(None)

class TextworldLdScreen(Screen):
    layout = ObjectProperty(None)
    __db: WorldDatabase

    def __init__(self, **kw):
        super(TextworldLdScreen, self).__init__(**kw)
        self.__db = WorldDatabase()
        self.__db.open()

    def __del__(self, exc_type, exc_value, traceback):
        self.__db.close()

    def on_pre_enter(self, *args):
        self.layout.left_panel.save_view.updateWorldList(self.__db)
        return super().on_enter(*args)
