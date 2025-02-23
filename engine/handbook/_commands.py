from kivy.app import App

class SystemCommands:
    
    def _exit_game():
        App.get_running_app().game.current = 'main_menu_ui'

    COMMANDS:dict[tuple[str,str], callable] = {
        ("EXIT", "SYS") : _exit_game
    }