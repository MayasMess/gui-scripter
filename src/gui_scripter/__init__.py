import base64
import io
from abc import abstractmethod
from functools import partial
from pathlib import Path
from tkinter import ttk
from typing import Optional

from ttkthemes import ThemedTk
from PIL import ImageTk, Image
import tkinter as tk
from .images import rob, rob_icon


def entry(name: str) -> dict:
    return {
        'name': name,
        'class': ttk.Entry
    }


def drop_box(name: str, values: list) -> dict:
    return {
        'name': name,
        'class': ttk.Combobox,
        'values': values
    }


class Gui:
    _SRC_PATH = Path(__file__).resolve().parent.parent
    inputs: list = None
    title: str = None
    progress_bar: Optional[ttk.Progressbar] = True

    def __init__(self):

        if self.inputs is None:
            self.inputs = []

        self.root = ThemedTk(theme="equilux")
        self.app_width = 400
        if len(self.inputs) == 0:
            self.app_height = 450
        else:
            self.app_height = 450 + (30 * len(self.inputs))
        self.root.geometry(f"{self.app_width}x{self.app_height}")
        self.root.resizable(False, False)

        if self.title is None:
            self.root.title('Gui Scripter')
        else:
            self.root.title(self.title)

        self.icon = ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(rob_icon))))
        self.root.iconphoto(False, self.icon)

        self.app_frame = ttk.Frame(self.root, width=self.app_width, height=self.app_height)

        self.main_image = ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(rob))))
        self.panel = tk.Label(self.app_frame, image=self.main_image, bg='#464646')

        self.inputs_dict = {}
        self.label_dict = {}

        for input_name in self.inputs:
            if input_name.get('class') is ttk.Entry:
                self.inputs_dict[input_name.get('name')] = input_name.get('class')(self.app_frame)
            elif input_name.get('class') is ttk.Combobox:
                self.inputs_dict[input_name.get('name')] = input_name.get('class')(self.app_frame,
                                                                                   values=input_name.get('values'))
                self.inputs_dict[input_name.get('name')].current(0)
            self.label_dict[input_name.get('name')] = ttk.Label(self.app_frame, text=input_name.get('name'))

        self.run_script_button = ttk.Button(self.app_frame, text="Run !", command=self.script, takefocus=0)

        if self.progress_bar:
            self.progress_bar = ttk.Progressbar(self.app_frame, orient="horizontal", length=self.app_width - 100,
                                                mode='determinate')
        self.run()

    def run(self) -> None:
        self.app_frame.pack(expand=True, fill='both')
        self.panel.pack()
        for input_name in self.inputs:
            self.label_dict[input_name.get('name')].pack(anchor='center')
            self.inputs_dict[input_name.get('name')].pack(anchor='center', pady=2)
        self.run_script_button.pack(anchor='center', pady=15)
        if self.progress_bar:
            self.progress_bar.pack(side='top', padx=0, pady=self.app_width/15, anchor='n')
        self.root.mainloop()

    @abstractmethod
    def script(self):
        pass

    def set_progress_bar(self, value: int) -> None:
        self.progress_bar['value'] = value
        self.progress_bar.update()

    def __command(self) -> partial:
        return partial(self.script, *self.get_entries_as_args())()

    def get_entries_as_args(self) -> list:
        return [self.inputs_dict[input_name].get() for input_name in self.inputs]

    def get(self, entry):
        return self.inputs_dict[entry].get()


