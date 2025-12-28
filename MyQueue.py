from win32gui import GetWindowText

class HWNDQueue:
    def __init__(self, maxsize=0):
        self.hwnds = []
        self.maxsize = maxsize

    def __iter__(self):
        for hwnd in self.hwnds:
            yield hwnd

    def __str__(self):
        ret = ""
        for hwnd in self.hwnds:
            ret += f"{hwnd} : {GetWindowText(hwnd)}\n"
        return ret

    def is_empty(self):
        return len(self.hwnds) == 0

    def enqueue(self, item):
        self.hwnds.append(item)
        if self.maxsize > 0 and len(self.hwnds) > self.maxsize:
            self.hwnds.pop(0)

    def dequeue(self):
        if not self.is_empty():
            return self.hwnds.pop(0)
        else:
            return None

    def size(self):
        return len(self.hwnds)
    
    def max_size(self):
        return self.maxsize