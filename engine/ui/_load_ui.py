from kivymd.uix.button import MDButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.transition.transition import MDSlideTransition
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from engine.database import WorldDatabase
import logging

class LoadedSaveBtn(MDButton):
    txt = ObjectProperty(None)

    def __init__(self, world, **kwargs):
        super(LoadedSaveBtn, self).__init__(**kwargs)
        self.id = world
        self.txt.text = world
    
    def on_press(self):
        self.parent.parent.parent.right_panel.update_panel(self.id)
        return super().on_press()

class TextworldLdSaveView(MDBoxLayout):
    def updateWorldList(self, save_names):
        self.worlds = save_names
        logging.debug(f"Children: {self.children} Count: {len(self.children)} db Count: {len(self.worlds)}")
        self.clear_widgets()
        for i in range(len(self.worlds)):
                btn = LoadedSaveBtn(world=self.worlds[i - 1])
                self.ids[f'{self.worlds[i - 1]}'] = btn
                self.add_widget(btn)
        logging.debug(f"Layout Children: {self.ids} Count: {len(self.children)}")

class TextworldLdBackBtn(MDButton):
    def on_press(self):
        MDApp.get_running_app().game.transition = MDSlideTransition(direction='down')
        MDApp.get_running_app().game.current = 'main_menu_ui'

class TextworldLdLeftPanel(MDBoxLayout):
    save_view = ObjectProperty(None)
    back_btn = ObjectProperty(None)

class TextworldLdDeleteBtn(MDButton):
    world_id:str
    db:WorldDatabase
    def on_press(self):
        self.db.delete_world_from_db(self.world_id)
        self.parent.parent.info_panel.world_name.text = "Click Save to load Info"
        self.parent.parent.parent.left_panel.save_view.updateWorldList(self.db.load_save_names())
        return super().on_press()

class TextworldLdLoadBtn(MDButton):
    world_id:str
    db:WorldDatabase
    def on_press(self):
        world_data = self.db.load_world_from_db(self.world_id)
        MDApp.get_running_app().game.loadSaveMenuCall(world_data, self.world_id)
        return super().on_press()

class TextworldLdOptions(MDBoxLayout):
    delete = ObjectProperty(None)
    load = ObjectProperty(None)

class TextworldLdInfoPanel(MDBoxLayout):
    pass

class TextworldLdRightPanel(MDBoxLayout):
    info_panel = ObjectProperty(None)
    options = ObjectProperty(None)

    def update_panel(self, world_id):
        self.info_panel.world_name.text = world_id
        self.options.load.world_id = world_id
        self.options.delete.world_id = world_id

class TextworldLdMenuLayout(MDBoxLayout):
    left_panel = ObjectProperty(None)
    right_panel = ObjectProperty(None)

class TextworldLdScreen(MDScreen):
    layout = ObjectProperty(None)
    __db: WorldDatabase

    def __init__(self, **kw):
        super(TextworldLdScreen, self).__init__(**kw)
        self.__db = WorldDatabase()
        self.__db.open()

    def __del__(self, exc_type, exc_value, traceback):
        self.__db.close()

    def on_pre_enter(self, *args):
        self.layout.left_panel.save_view.updateWorldList(self.__db.load_save_names())
        self.layout.right_panel.options.load.db = self.__db
        self.layout.right_panel.options.delete.db = self.__db
        return super().on_enter(*args)
