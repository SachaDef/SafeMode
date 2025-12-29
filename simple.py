from pynput import keyboard
from time import sleep
from win32gui import SetForegroundWindow, GetForegroundWindow, GetWindowText, SetWindowPos
from win32api import keybd_event
from win32con import HWND_NOTOPMOST, SWP_NOSIZE, SWP_NOMOVE, SWP_NOACTIVATE
from MyQueue import HWNDQueue
from utils import retrieve_displays, get_active_windows


PANIC_KEY = keyboard.Key.ctrl_r
DEBUG_KEY = keyboard.Key.f7
RESET_KEY = keyboard.Key.f8
SET_KEY = keyboard.Key.f9
EXIT_KEY = keyboard.Key.f10


def bring_window_to_front(hwnd, verbose=True):
    try:
        # Trick to allow SetForegroundWindow to work
        keybd_event(0x12, 0, 0, 0)
        keybd_event(0x12, 0, 2, 0)
        SetForegroundWindow(hwnd)
        if verbose:
            print(f"Brought window {hwnd} to front.")
    except Exception as e:
        print(f"Error bringing window to front: {e}")


def on_press(key):
    global target_hwnds

    if key == DEBUG_KEY:
        print("Debug Info:")
        print(f"Current target windows in queue (size {target_hwnds.size()}/{target_hwnds.max_size()}):")
        print(target_hwnds)
        bring_window_to_front(CODE_HWND, verbose=False)
        print("")

    if key == PANIC_KEY:
        for hwnd in target_hwnds:
            bring_window_to_front(hwnd)
            sleep(0.01)
        print("")

    if key == RESET_KEY:
        displays = retrieve_displays()
        target_hwnds = HWNDQueue(len(displays))
        for _ in range(len(displays)):
            target_hwnds.enqueue(CODE_HWND)
        print("Reset target window(s) :")
        print(target_hwnds)

    if key == SET_KEY:
        hwnd = GetForegroundWindow()
        target_hwnds.enqueue(hwnd)
        print(target_hwnds)

    if key == EXIT_KEY:
        print("Exiting program.")
        bring_window_to_front(CODE_HWND)
        return False


if __name__ == "__main__":
    print("Program started.\n")
    print("Press Ctrl_R to bring target window to front.")
    print("Press F8 to reset target window(s).")
    print("Press F9 to reselect target window (FIFO queue if multiple displays).")
    print("Press F10 to exit.\n")

    user = input("Should Ganymede windows be unpinned from top-most? (y/n): ")
    if user.lower() == 'y':
        for hwnd, title in get_active_windows():
            if "ganymede" in title.lower().replace("è", "e"):
                # Remove top-most attribute
                flags = SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE
                SetWindowPos(hwnd, HWND_NOTOPMOST, 0, 0, 0, 0, flags)
                print(f"Removed top-most property from window: {title} ({hwnd})")
    print("")

    CODE_HWND = GetForegroundWindow()
    print(f"Default window : {GetWindowText(CODE_HWND)} ({CODE_HWND})\n")

    displays = retrieve_displays()
    print(f"Detected {len(displays)} display(s).")

    target_hwnds = HWNDQueue(len(displays))
    for _ in range(len(displays)):
        target_hwnds.enqueue(CODE_HWND)
    print(target_hwnds)
    
    k_listener = keyboard.Listener(on_press=on_press)
    k_listener.start()
    print("Initialization complete, listening for keyboard events\n")
    k_listener.join()
