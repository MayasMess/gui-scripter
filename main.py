from backend import BackEnd


class Main(BackEnd):
    def __init__(self):
        inputs = {"Quantity", "Salary", "Others"}
        super().__init__(inputs, self.main_script)

    def main_script(self):
        print('Starting the script')
        self.complete_progress_bar()
        print('Script done!')


if __name__ == '__main__':
    Main()
