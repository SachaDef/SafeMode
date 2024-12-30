import customtkinter as ctk
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")
from utils import retrieve_displays, get_active_windows

class MainInterface(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ==================== #
        # === Window Setup === #
        # ==================== #

        self.width = 800
        self.height = 500
        self.title('Safe Mode App')
        self.geometry(f'{self.width}x{self.height}+50+50')
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)
        self.after(1, lambda: self.focus_force())

        self.window_frame = ctk.CTkFrame(self)
        self.keybind_frame = ctk.CTkFrame(self)
        self.console_frame = ctk.CTkFrame(self)


        # ==================== #
        # === Window Frame === #
        # ==================== #

        # === Variables === #
        self.active_windows = get_active_windows()
        self.active_windows_titles = [title for (_, title) in self.active_windows]
        self.displays_coords = retrieve_displays()
        self.displays_selection = {} # TODO

        # === Functions === #
        # Update the displays and active windows data, adapt the frame to the new data
        def update_windows_frame():
            self.active_windows = get_active_windows()
            self.active_windows_titles = [title for (_, title) in self.active_windows]
            self.displays_coords = retrieve_displays()
            self.displays_selection = {}

            for widget in self.window_frame.winfo_children():
                widget.destroy()
            for i in range(self.window_frame.grid_size()[0]):
                self.window_frame.grid_columnconfigure(i, weight=0)
            
            draw_windows_frame()

        # Set the currently selected windows as safe windows TODO
        def select_windows():
            pass
        
        # Draw the window frame
        def draw_windows_frame():
            n_displays = len(self.displays_coords)
            self.window_frame.grid_rowconfigure(0, weight=1)
            for i in range(n_displays):
                self.window_frame.grid_columnconfigure(i, weight=2)
            self.window_frame.grid_columnconfigure(n_displays, weight=1)

            for i, (name, _) in enumerate(self.displays_coords):
                menu_frame = ctk.CTkFrame(self.window_frame)
                menu_frame.grid_columnconfigure(0, weight=1)
                menu_frame.grid_rowconfigure((0, 1), weight=1)

                pretty_name = name.replace('\\', '').replace('.', '').replace('/', '')
                label = ctk.CTkLabel(menu_frame, text=pretty_name)
                svar = ctk.StringVar(value=name)
                menu = ctk.CTkOptionMenu(menu_frame, values=self.active_windows_titles, variable=svar)
                self.displays_selection[name] = (svar, menu)

                label.grid(row=0, column=0, padx=5, pady=5)
                menu.grid(row=1, column=0, padx=5, pady=5)
                menu_frame.grid(row=0, column=i, sticky='nsew', padx=5, pady=5)

            button_frame = ctk.CTkFrame(self.window_frame)
            button_frame.grid_columnconfigure(0, weight=1)
            button_frame.grid_rowconfigure((0, 1), weight=1)
            update_button = ctk.CTkButton(button_frame, text='Clear & update', command=update_windows_frame)
            update_button.grid(row=0, column=0, padx=5, pady=5)
            select_button = ctk.CTkButton(button_frame, text='Select', command=select_windows)
            select_button.grid(row=1, column=0, padx=5, pady=5)
            button_frame.grid(row=0, column=n_displays, sticky='nsew', padx=5, pady=5)


        # ===================== #
        # === Keybind Frame === #
        # ===================== #

        # Variables
        self.previous_keybinds = {} # TODO
        self.keybind_selection = {} # TODO

        # Functions
        # Retrieve the previous user defined keybinds TODO
        def get_previous_keybinds():
            pass

        # Draw the keybind frame
        def draw_keybind_frame():
            self.keybind_frame.grid_rowconfigure(0, weight=1)
            self.keybind_frame.grid_columnconfigure(0, weight=2)
            self.keybind_frame.grid_columnconfigure(1, weight=1)

            menu_frame = ctk.CTkFrame(self.keybind_frame)
            menu_frame.grid_columnconfigure(0, weight=1)
            menu_frame.grid_rowconfigure((0, 1), weight=1)

            label = ctk.CTkLabel(menu_frame, text='KEYBIND')
            svar = ctk.StringVar(value='KEYBIND')


            button_frame = ctk.CTkFrame(self.keybind_frame)
            button_frame.grid_columnconfigure(0, weight=1)
            button_frame.grid_rowconfigure((0, 1), weight=1)


            


        # ===================== #
        # === Console Frame === #
        # ===================== #

        # Variables


        # Functions


        # =================== #
        # === Grid Layout === #
        # =================== #

        # Grid initialization
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        # Window Frame
        draw_windows_frame()
        self.window_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)


        # Keybind Frame
        self.keybind_frame.grid_rowconfigure(0, weight=1)
        self.keybind_frame.grid_columnconfigure(0, weight=2)
        self.keybind_frame.grid_columnconfigure(1, weight=1)

        button_frame = ctk.CTkFrame(self.keybind_frame)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_rowconfigure((0, 1), weight=1)



        






if __name__ == '__main__':
    interface = MainInterface()
    interface.mainloop()