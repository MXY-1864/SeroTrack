import customtkinter as ctk

MIN_PASSWORD_LENGTH = 6
ERROR_COLOR = ("#C62828", "#EF5350")  # (light mode, dark mode)
SUCCESS_COLOR = ("#2E7D32", "#66BB6A")
USERNAME_ID = "InoviaLab"
PASSWORD_ID = "Lab92100"

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, on_login_success):
        super().__init__(master)

        self.username_entry = ctk.CTkEntry(
            self,
            placeholder_text="Identifiant"
        )
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            self,
            placeholder_text="Mot de passe"
        )
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(
            self,
            text="Se connecter",
            command=self.login
        )
        self.login_button.pack(pady=10)

        self.on_login_success = on_login_success

    def login(self):
        user_id = self.username_entry.get().strip()
        password = self.password_entry.get()

        if user_id == USERNAME_ID and password == PASSWORD_ID:
            self.on_login_success()
        else:
            print("Error")

