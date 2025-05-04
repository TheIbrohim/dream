def show_all_admins():
    print("--- Adminlar ro'yxati ---")
    with open("database/users.csv", 'r', encoding='utf-8') as file:
        for line in file:
            _, login, _, role, _ = line.strip().split(',')
            if role == "admin":
                print(f"Admin: {login}")

def create_admin():
    login = input("Yangi admin login: ")
    password = input("Parol: ")
    with open("database/users.csv", 'a', encoding='utf-8') as file:
        file.write(f"admin_{login},{login},{password},admin,0\n")
        print("Admin yaratildi.")

def delete_admin():
    login = input("O'chiriladigan admin login: ")
    lines = []
    with open("database/users.csv", 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open("database/users.csv", 'w', encoding='utf-8') as file:
        for line in lines:
            if not (line.strip().split(',')[1] == login and 'admin' in line):
                file.write(line)
    print("Admin o'chirildi.")

def show_statistics():
    users = open("database/users.csv", 'r', encoding='utf-8').readlines()
    groups = open("database/groups.csv", 'r', encoding='utf-8').readlines()
    print(f"Foydalanuvchilar soni: {len(users)}")
    print(f"Guruhlar soni: {len(groups)}")
