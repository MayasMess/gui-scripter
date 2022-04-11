Simple GUI for scripts 🤖 !
-
![image](img/app1.png)

Installation:
-
```shell script
  pip install gui-scripter
```
Example:
-
```python
from gui_scripter import Gui, entry, drop_box
```

```python
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
```
