def login():
    login = input("Login: ")
    password = input("Password: ")

    try:
        with open("database/users.csv", 'r', encoding='utf-8') as file:
            for line in file:
                user_id, u_login, u_pass, role, balance = line.strip().split(',')
                if login == u_login and password == u_pass:
                    return {"id": user_id, "role": role, "login": u_login, "balance": float(balance)}
        print("Login yoki parol xato.")
        return None
    except FileNotFoundError:
        print("users.csv fayli topilmadi.")
        return None