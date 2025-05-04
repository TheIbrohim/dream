from auth import login
import super_admin

while True:
    print("\n--- ERP SYSTEM ---")
    print("1. Login\n2. Exit")
    cmd = input(">>> ")

    if cmd == "1":
        user = login()
        if user:
            role = user['role']

            if role == "superadmin":
                while True:
                    print("\n--- SUPER ADMIN MENU ---")
                    print("1. Show all admins")
                    print("2. Create admin")
                    print("3. Delete admin")
                    print("4. Show statistics")
                    print("8. Logout")
                    ch = input(">>> ")

                    if ch == "1":
                        super_admin.show_all_admins()
                    elif ch == "2":
                        super_admin.create_admin()
                    elif ch == "3":
                        super_admin.delete_admin()
                    elif ch == "4":
                        super_admin.show_statistics()
                    elif ch == "8":
                        print("Logout qildingiz.")
                        break
                    else:
                        print("Noto'g'ri tanlov")

    elif cmd == "2":
        print("Dasturdan chiqildi.")
        break
