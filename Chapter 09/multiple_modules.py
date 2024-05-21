import multiple_modules_priviliges_admin as mmpa

super_user = mmpa.Admin("Laura", "Veerkamp", "lveerkamp", 3)
super_user.privileges.show_privileges()