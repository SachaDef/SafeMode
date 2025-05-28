import win32api

type ScreenCoords = tuple[int, int, int, int]
type DisplayInfo = tuple[str, ScreenCoords]
def retrieve_displays() -> list[DisplayInfo]:
    """
    Retrieves the list of connected displays and their coordinates.
    Returns:
        list: A list of tuples, each containing the display name and its coordinates.
    """
    displays: list[DisplayInfo] = []
    monitors = win32api.EnumDisplayMonitors()
    for monitor in monitors:
        info = win32api.GetMonitorInfo(monitor[0])
        name = info["Device"]
        name = name.replace("\\", "").replace(".", "").replace("/", "")
        coords = info["Work"]
        displays.append((name, coords))
    return displays
