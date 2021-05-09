from tkinter import ttk, PhotoImage
from ttkthemes import ThemedTk
import os


class FrontEnd:
    APP_WIDTH = 400
    APP_HEIGHT = 400
    PROJECT_PATH = os.getcwd()

    def __init__(self, inputs, main_script):
        self.root = ThemedTk(theme="equilux")
        self.root.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}")
        self.root.resizable(False, False)

        self.app_frame = ttk.Frame(self.root, width=self.APP_WIDTH, height=self.APP_HEIGHT)
        self.app_frame.pack(expand=True, fill='both')

        #main_image = PhotoImage(os.path.join(self.PROJECT_PATH, 'robot.png'))
        #panel = ttk.Label(self.app_frame, image=main_image)
        #panel.pack()

        self.inputs_dict = {}
        for input_name in inputs:
            var_input = ttk.Entry(self.app_frame)
            var_input.insert(0, input_name)
            var_input.bind("<FocusIn>", lambda args: var_input.delete('0', 'end'))
            var_input.pack(anchor='center', pady=5)
            self.inputs_dict[input_name] = var_input
        self.run_script_button = ttk.Button(self.app_frame, text="Run !", command=main_script)
        self.run_script_button.pack(anchor='center', pady=15)

        self.progress_bar = ttk.Progressbar(self.app_frame, orient="horizontal", length=self.APP_WIDTH - 100,
                                            mode='determinate')
        self.progress_bar.pack(side='top', padx=0, pady=5, anchor='n')

        self.root.mainloop()
