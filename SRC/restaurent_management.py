from SRC.authentication import auth
from SRC.menumanagement import management

def run_restaurant_system():
    auth.main_menu()
    management.admin_panel()