import win32gui
import ctypes, ctypes.wintypes

DWM_CLOAKED_ATTR = 14
MAX_TITLE_LENGTH = 35

def get_active_window_title(window_handle: int, active_windows: list[tuple[int, str]]) -> None:
    """
    Callback function to retrieve the title of active windows.
    Args:
        window_handle (int): Handle of the window.
        _: Unused parameter, required for the EnumWindows from win32gui.
    Returns:
        None
    """
    isCloacked = ctypes.c_int(0)
    window_manager_api = ctypes.WinDLL("dwmapi")

    if not win32gui.IsWindowVisible(window_handle) or win32gui.GetWindowText(window_handle) == '':
        return
    
    window_manager_api.DwmGetWindowAttribute(ctypes.wintypes.HWND(window_handle),
                                             ctypes.wintypes.DWORD(DWM_CLOAKED_ATTR),
                                             ctypes.byref(isCloacked),
                                             ctypes.sizeof(isCloacked))
    title = win32gui.GetWindowText(window_handle)
    if "Safe Mode App" in title or "Program Manager" in title:
        return
    if len(title) > MAX_TITLE_LENGTH:
        title = title[:MAX_TITLE_LENGTH] + "..."    
    if (isCloacked.value == 0):
        active_windows.append((window_handle, title))

def get_active_windows() -> list[tuple[int, str]]:
    """
    Retrieves the list of active windows and their titles.
    Returns:
        list: A list of tuples, each containing the window handle and its title.
    """
    active_windows = []
    win32gui.EnumWindows(lambda hwnd, _: get_active_window_title(hwnd, active_windows), None)
    return active_windows
