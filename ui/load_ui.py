from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from database import WorldDatabase

class LoadedSaveBtn(Button):

    def __init__(self, world, **kwargs):
        super(LoadedSaveBtn, self).__init__(**kwargs)
        self.world = world
        self.id = world.world_name
    
    def on_press(self):
        print(f"On_Press Parent {self.parent.parent.parent.parent.parent}")
        self.parent.parent.parent.parent.parent.loadSaveMenuCall(self.world)
        return super().on_press()

class TextworldLdSaveView(BoxLayout):

    db: WorldDatabase

    def __enter__(self):
        self.db = WorldDatabase()
        self.db.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()

    def updateWorldList(self):
        self.worlds = self.db.load_save_names()
        print(f"DB Saves: {self.worlds}")
        for i in range(len(self.worlds)):
            if self.children:
                if self.children[i].text == self.worlds[i].world_name:
                    continue
                else:
                    btn = LoadedSaveBtn(world=self.worlds[i], text=self.worlds[i].world_name)
                    self.ids[f'{self.worlds[i].world_name}'] = btn
                    self.add_widget(btn)
            else:
                btn = LoadedSaveBtn(world=self.worlds[i], text=self.worlds[i].world_name)
                self.ids[f'{self.worlds[i].world_name}'] = btn
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
    def on_pre_enter(self, *args):
        self.layout.left_panel.save_view.updateWorldList()
        return super().on_enter(*args)
