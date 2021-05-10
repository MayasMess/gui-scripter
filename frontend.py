from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import ImageTk, Image
import tkinter as tk
import os


class FrontEnd:
    APP_WIDTH = 400
    APP_HEIGHT = 450
    PROJECT_PATH = os.getcwd()

    def __init__(self, inputs, main_script):
        self.root = ThemedTk(theme="equilux")
        self.root.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}")
        self.root.resizable(False, False)
        self.root.title('Gui Scripter')
        icon = ImageTk.PhotoImage(Image.open(os.path.join(self.PROJECT_PATH, 'static/rob_icon.png')))
        self.root.iconphoto(False, icon)

        self.app_frame = ttk.Frame(self.root, width=self.APP_WIDTH, height=self.APP_HEIGHT)
        self.app_frame.pack(expand=True, fill='both')

        main_image = ImageTk.PhotoImage(Image.open(os.path.join(self.PROJECT_PATH, 'static/rob.png')))
        panel = tk.Label(self.app_frame, image=main_image, bg='#464646')
        panel.pack()

        self.inputs_dict = {}
        for input_name in inputs:
            self.inputs_dict[input_name] = ttk.Entry(self.app_frame)
            self.inputs_dict[input_name].insert(0, input_name)
            self.inputs_dict[input_name].pack(anchor='center', pady=5)

        self.run_script_button = ttk.Button(self.app_frame, text="Run !", command=main_script, takefocus=0)
        self.run_script_button.pack(anchor='center', pady=15)

        self.progress_bar = ttk.Progressbar(self.app_frame, orient="horizontal", length=self.APP_WIDTH - 100,
                                            mode='determinate')
        self.progress_bar.pack(side='top', padx=0, pady=5, anchor='n')

        self.root.mainloop()
