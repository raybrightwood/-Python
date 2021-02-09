def user_data():
    name = input("Введите имя:")
    surname = input("Введите фамилию:")
    birth_year = input("Введите год рождения:")
    city = input("Введите город проживания:")
    email = input("Введите e-mail:")
    telephone = input("Введите телефон:")
    return (f"имя - {name}, фамилия - {surname}, год рождения - {birth_year}, город проживания - {birth_year}, " 
            f"email - {email},  telephone - {telephone}")
print(user_data())


