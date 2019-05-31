import os
from server import AppStarter, EnvironmentSettingsLoader

root_folder_path = os.path.dirname(os.path.abspath(__file__))
static_folder_root = os.path.join(root_folder_path, 'client')


print('starting server... top ten twitter is coming up....')

settings_loader = EnvironmentSettingsLoader(root_folder_path)

app = AppStarter(settings_loader)
app.register_routes_to(static_folder_root)
flash_runner = app.get_flask_runner()

def runserver():
    print('running!')
    app.run()

if __name__ == '__main__':
    runserver()