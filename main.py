import customtkinter as ctk
from login import LoginFrame

# Configuration du mode d'apparence
ctk.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

app = ctk.CTk()
app.geometry("800x700")
app.title("SeroTrack")

def show_homepage():
    login_frame.pack_forget()
    homepage_frame.pack(expand=True, fill="both")

login_frame = LoginFrame(
    master=app,
    on_login_success=show_homepage
)
login_frame.pack(expand=True)

#-----------------------------------------------------------------------------------#
class SeroBox:
    def __init__(self, max_tubes, nb_tubes=0):
        self.nb_tubes = nb_tubes
        self.max_tubes = max_tubes
    
    def ajouter_tubes(self, tubes_a_ajouter=0):
        if tubes_a_ajouter + self.nb_tubes <= self.max_tubes and tubes_a_ajouter >= 0:
            self.nb_tubes += tubes_a_ajouter

class HomeFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        
        self.fridge_rows = []
        self.sero_boxes = []
        self.sero_boxes_emplacement = [
            "A1", "A2", "A3", 
            "B1", "B2", "B3", 
            "C1", "C2", "C3", 
            "D1", "D2", "D3", 
            "E1", "E2", "E3", 
            "F1", "F2", "F3"
        ]
        self.boxes = {}

        self.welcome_label = ctk.CTkLabel(
            self,
            text="Bienvenue sur Serotrack"
        )
        self.welcome_label.pack(pady=10)
    
        self.fridge = ctk.CTkFrame(
            master=self, 
            width=300, 
            height=500, 
            fg_color="red"
        )
        self.fridge.pack_propagate(False) # Prevent Frame shrinking
        self.fridge.place(relx=0.5, rely=0.5, anchor="center")

        for i in range(6):
            self.fridge_row = ctk.CTkFrame(
                master=self.fridge, 
                width=285, 
                height=(500-60)/6, 
                fg_color="blue"
            )
            self.fridge_row.pack(pady=5, padx=10)
            self.fridge.pack_propagate(False)
            self.fridge_items = self.sero_boxes_emplacement[i * 3 : (i + 1) * 3]
            for item in self.fridge_items:
                self.sero_box = ctk.CTkButton(
                    master=self.fridge_row, 
                    text=item, 
                    width=(285-30)/3, 
                    height=(500-120)/6, 
                    fg_color="green",
                    cursor="hand2",
                    command=lambda location=item: self.show_box(location)
                )
                self.sero_box.pack(side="left", pady=5, padx=5)
                self.boxes[item] = self.sero_box
                self.sero_boxes.append(self.sero_box)
            self.fridge_rows.append(self.fridge_row)

        self.sero_box_frame = ctk.CTkFrame(
            master=self, 
            width=450, 
            height=300, 
            fg_color="purple"
        )

        self.box_title = ctk.CTkLabel(
            master=self.sero_box_frame,
            text=""
        )
        self.box_title.pack(pady=10)

        self.box_row_numbers = ctk.CTkLabel(
            master=self.sero_box_frame,
            text=""
        )
        self.box_row_numbers.pack(padx=15)

        for index in range(12):
            num = ctk.CTkLabel(
                self.box_row_numbers,
                text=index + 1,
                width=15,
                height=15,
            )
            num.grid(
                row=index // 12,
                column=index % 12,
                padx=7,
                pady=0  
            )

        self.wells_frame = ctk.CTkFrame(self.sero_box_frame)
        self.wells_frame.pack(padx=15, pady=10)

        for index in range(96):
            well = ctk.CTkLabel(
                self.wells_frame,
                text="",
                width=25,
                height=25,
                fg_color="gray30",
                corner_radius=50
            )
            well.grid(
                row=index // 12,
                column=index % 12,
                padx=2,
                pady=2
            )
    
    def show_box(self, location):
        self.box_title.configure(text=f"Boîte {location}")
        self.sero_box_frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
        )
        self.sero_box_frame.lift()
        self.sero_box_frame.pack_propagate(False)


homepage_frame = HomeFrame(master=app)

#-----------------------------------------------------------------------------------#

app.mainloop()