from unittest import TestCase
from src.gui_scripter import Gui, entry, drop_box


class MyFirstApplication(Gui):

    inputs = [
        entry('name'),
        entry('age'),
    ]
    title = 'My First Application'

    def script(self):
        for x in range(1, 51):
            self.set_progress_bar(x*2)
        print(f"Yo, my name is {self.get('name')} and i'm {self.get('age')} years old")


class MySecondApplication(Gui):

    inputs = [
        drop_box('year', values=[2010, 2020, 2030])
    ]
    title = 'My Second Application'

    def script(self):
        for x in range(1, 51):
            self.set_progress_bar(x*2)
        print(f"this is {self.get('year')}!")


class TestGuiScripter(TestCase):

    def test_app_is_running(self):
        MyFirstApplication()

    def test_second_app_is_running(self):
        MySecondApplication()
