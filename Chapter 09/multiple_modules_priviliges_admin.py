import multiple_modules_user as mmu

class Admin(mmu.User):
    def __init__(self, first_name, last_name, username, active):
        super().__init__(first_name, last_name, username, active)
        self.privileges = Priviliges()


class Priviliges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)