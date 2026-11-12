import customtkinter as ctk

# Configuration du mode d'apparence
ctk.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

app = ctk.CTk()
app.geometry("800x700")
app.title("SeroTrack")

fridge = ctk.CTkFrame(master=app, width=300, height=500, fg_color="red")
fridge.pack(pady=5, padx=5)
fridge.pack_propagate(False) # Prevent Frame shrinking
fridge.place(relx=0.5, rely=0.5, anchor="center")

fridge_rows = []
sero_boxes = []
sero_boxes_emplacement = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2", "D3", "E1", "E2", "E3", "F1", "F2", "F3"]
boxes = {}

for i in range(6):
    fridge_row = ctk.CTkFrame(master=fridge, width=285, height=(500-60)/6, fg_color="blue")
    fridge_row.pack(pady=5, padx=10)
    fridge.pack_propagate(False)
    fridge_items = sero_boxes_emplacement[i * 3 : (i + 1) * 3]
    for item in fridge_items:
        sero_box = ctk.CTkButton(master=fridge_row, text=item, width=(285-30)/3, height=(500-120)/6, command=lambda name=item: print(f"Selected: {name}"), fg_color="green")
        sero_box.pack(side="left", pady=5, padx=5)
        boxes[item] = sero_box
        sero_boxes.append(sero_box)
    fridge_rows.append(fridge_row)

app.mainloop()
