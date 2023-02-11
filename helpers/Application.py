from Setting import driver
import os, sys
current_directory = os.getcwd()
sys.path.append(current_directory)

class Application:
    def close_current_app(self):
        driver.close_app()

    def reopen_application(self):
        driver.reset()