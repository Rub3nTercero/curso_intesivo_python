# Autor Rubén Tercero - Fecha: 19/02/2025
# Este script asegura que cada usuario tenga un nombre único

current_users = ['arantxa', 'Ruben', 'roman', 'jaume', 'rodri']
new_users = ['emIl', 'adrian', 'gema', 'aRantxa', 'ruBen']

current_users_copy = [user.lower() for user in current_users]
    
for new_user in new_users:
    if new_user.lower() in current_users_copy:
        print(f"{new_user.title()} debes introducir otro nombre.")
    else:
        print(f"{new_user.title()} esta disponible.")