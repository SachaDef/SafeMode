from pynput import keyboard
from win32gui import SetForegroundWindow, GetForegroundWindow, GetWindowText
from win32api import keybd_event


PANIC_KEY = keyboard.Key.ctrl_r
RESET_KEY = keyboard.Key.f9
EXIT_KEY = keyboard.Key.f10

CODE_HWND = GetForegroundWindow()
target_hwnd = None


def bring_window_to_front(hwnd):
    try:
        # Trick to allow SetForegroundWindow to work
        keybd_event(0x12, 0, 0, 0)
        keybd_event(0x12, 0, 2, 0)
        SetForegroundWindow(hwnd)
        print(f"Brought window {hwnd} to front.")
    except Exception as e:
        print(f"Error bringing window to front: {e}")


def on_press(key):
    global target_hwnd
    if key == PANIC_KEY:
        if target_hwnd:
            bring_window_to_front(target_hwnd)
        else:
            print("No target window set.")
            bring_window_to_front(CODE_HWND)
    if key == RESET_KEY:
        target_hwnd = GetForegroundWindow()
        print(f"New target window set to {target_hwnd} : {GetWindowText(target_hwnd)}")
        bring_window_to_front(CODE_HWND)
    if key == EXIT_KEY:
        print("Exiting program.")
        bring_window_to_front(CODE_HWND)
        return False


if __name__ == "__main__":
    print("Program started.")
    print("Press Ctrl_R to bring target window to front.")
    print("Press F9 to reselect target window.")
    print("Press F10 to exit.")
    k_listener = keyboard.Listener(on_press=on_press)
    k_listener.start()
    k_listener.join()

