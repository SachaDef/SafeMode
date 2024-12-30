import win32api, win32gui
import ctypes, ctypes.wintypes


# Global variables
active_windows = []


# Retrieve the number and coordinates of the displays
def retrieve_displays():
    displays = []
    monitors = win32api.EnumDisplayMonitors()
    for monitor in monitors:
        info = win32api.GetMonitorInfo(monitor[0])
        name = info["Device"]
        coords = info["Work"]
        displays.append((name, coords))
    return displays

# Auxiliary function to retrieve title and handle from a window
def get_active_window_title(window_handle: int, _):
    global active_windows
    isCloacked = ctypes.c_int(0)
    if not win32gui.IsWindowVisible(window_handle) or win32gui.GetWindowText(window_handle) == '':
        return
    ctypes.WinDLL("dwmapi").DwmGetWindowAttribute(ctypes.wintypes.HWND(window_handle),
                                                    ctypes.wintypes.DWORD(14),
                                                    ctypes.byref(isCloacked),
                                                    ctypes.sizeof(isCloacked))
    title = win32gui.GetWindowText(window_handle)
    if "Safe Mode App" in title or "Program Manager" in title:
        return
    if len(title) > 35:
        title = title[:35] + "..."    
    if (isCloacked.value == 0):
        active_windows.append((window_handle, title))

# List all active windows
def get_active_windows():
    global active_windows
    active_windows = []
    win32gui.EnumWindows(get_active_window_title, None)
    return active_windows