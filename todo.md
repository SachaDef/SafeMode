# SafeMode Application

---

## Goals

- Allow the user to bind a key to make "safe" windows appear
- Should be quite customizable (which key bind, which windows, and some additional preferences)
- Should not be heavy listening, to avoid taking up performances

---

## Intended use

1. Launch app
2. Get app window with default or saved settings
   2.1. Window(s) selection
   2.2. Keybind selection
   2.3. Permanent or pop-up mode
   2.4. Start-stop button
3. Start a keyboard listener
   3.1. Should sleep to avoid over-listening
4. Keep app minimized/in background unless activated by the user

---

## Todo List

- [ ] Basic interface
- [ ] How to store and retrieve saved settings
- [ ] Window handles
- [ ] Retrieve number and coordinates of displays
- [ ] How to open specific windows
- [ ] How to let user specify windows of his choice
- [ ] How to retrive key from user selection
- [ ] Is kill-create listener good for start-stop ?
- [ ] Is sleep mechanic good enough ? tkinter bind instead ?
- [ ] How to keep app minimized ?

---
