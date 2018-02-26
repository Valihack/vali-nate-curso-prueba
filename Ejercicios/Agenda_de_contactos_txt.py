import pickle
from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_SEARCH_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_SEARCH_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]

def show_menu():
    print("\n\nAcciones disponibles\n")
    print("  1 ~ Añadir contacto")
    print("  2 ~ Eliminar contacto")
    print("  3 ~ Buscar contacto")
    print("  4 ~ Exportar contactos a un CSV")
    print("  5 ~ Salir")

    return ask_until_correct_value(MENU_OPTIONS)

def ask_until_correct_value(options):
    selected_action = ""
    while not selected_action.isdigit() or selected_action.isdigit() and int(selected_action)not in options:
        selected_action = input("\nQue opcion deseas?: ")
    return int(selected_action)

def add_contact(contacts):

    print("\nAñadir contacto\n")

    contact = {
        "name" : input("Nombre: "),
        "second_name" : input("Apellido: "),
        "phone_number" : input("Numero de teléfono: "),
        "adress" : input("Dirección: "),
        "mail" : input("E-mail: ")
    }
    contacts.append(contact)
    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
    sleep(2)

def remove_contact(contacts):

    print("\nQue contacto desea borrar?\n")
    i=0
    while i < len(contacts):
        print(str(i+1), contacts[i]["name"])
        i+=1
    numero = int(input("\nQue contacto desea borrar?: ")) - 1
    if numero >= 0:
        contacts.remove(contacts[numero])
        print("\nSe ha borrado correctamente\n")
    else:
        print("\nQuieres o no borrar un contacto?")
        if input("Eleccion [s/n]") == "s":
            remove_contact(contacts)
        else:
            main()
    sleep(2)

def search_contact(contacts):

    print("\nBuscar contacto\n")
    search_term = input("Introduce un dato de tu contacto: ")
    found_contacts = []

    print("He encontrado las siguientes coincidencias: ")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1
        if contact["mail"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["mail"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1
        if contact["second_name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["second_name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1
        if contact["phone_number"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["phone_number"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1
        if contact["adress"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["adress"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        option = ask_until_correct_value(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se han encontrado, quieres volver a buscar?")
        if input("Eleccion [s/n]") == "s":
            search_contact(contacts)
        else:
            main()

    print("\nInformacion sobre {}\n". format(found_contacts[contact_index]["name"]))
    print("Nombre: {name}\nApellido: {second_name}\nTelefono: {phone_number}\nDireccion: {adress}\nEmail: {mail}\n".format(**found_contacts[contact_index]))
    sleep(2)

    return found_contacts

def load_contacts():
    try:
     return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente")

def main():
    contacts = load_contacts()

    action = show_menu()

    while action != ACTION_EXIT:

        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)
        elif action == ACTION_SEARCH_CONTACT:
            search_contact(contacts)
        elif action == ACTION_EXPORT_CONTACT:
            export_contacts(contacts)
        action = show_menu()

    #Exit the program
    save_contacts(contacts)

if __name__ == "__main__":
    main()