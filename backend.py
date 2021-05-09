import time

from frontend import FrontEnd


class BackEnd(FrontEnd):
    def __init__(self, inputs, main_script):
        super().__init__(inputs, main_script)

    def complete_progress_bar(self):
        for x in range(1, 101):
            time.sleep(0.1)
            self.progress_bar['value'] = x
            self.progress_bar.update()
