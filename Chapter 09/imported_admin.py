import imported_admin_classes as iac

super_user = iac.Admin("Laura", "Veerkamp", "lveerkamp", 3)
super_user.privileges.show_privileges()