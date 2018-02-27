import pickle
from time import sleep
from tkinter import *
from tkinter import ttk

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_SEARCH_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.txt"

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

def add_contacts(contacts, name, second_name, phone, adress, mail):

    contact = {
        "name": name,
        "second_name": second_name,
        "phone_number": phone,
        "adress": adress,
        "mail": mail
    }

    contacts.append(contact)
    save_contacts(contacts)
    return contact

def add_contacts_tk(contacts, name, second_name, phone, adress, mail, frame_contact_list):

    contact = add_contacts(contacts, name, second_name, phone, adress, mail)

    cols, rows = frame_contact_list.grid_size()

    ttk.Label(frame_contact_list, text=contact["name"]).grid(column=1, row=rows, sticky=W)
    ttk.Label(frame_contact_list, text=contact["second_name"]).grid(column=2, row=rows, sticky=W)
    ttk.Label(frame_contact_list, text=contact["phone_number"]).grid(column=3, row=rows, sticky=W)
    ttk.Label(frame_contact_list, text=contact["adress"]).grid(column=4, row=rows, sticky=W)
    ttk.Label(frame_contact_list, text=contact["mail"]).grid(column=5, row=rows, sticky=W)

def ask_new_contact(contacts):

    print("\nAñadir contacto\n")
    contact = add_contact(input("Nombre: "), input("Apellido: "), input("Numero de teléfono: "), input("Dirección: "), input("E-mail: "))

    contacts.append(contact)

def remove_contact(contacts):
    options = []
    print("\nQue contacto desea borrar?\n")
    i=0
    while i < len(contacts):
        options.append(i)
        print(str(i+1), contacts[i]["name"])
        i+=1
    numero = ask_until_correct_value(options)-1
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
        contact_index = ask_until_correct_value(contact_indexes)
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

def load_contact():
    try:
     contacts_loaded = pickle.load(open(SAVE_FILE_NAME, "rb"))

     return contacts_loaded
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente")

def show_loaded_contacts (contacts, frame_contact_list):
    index=0
    while index < len(contacts):
        cols, rows = frame_contact_list.grid_size()
        contact = contacts[index]
        ttk.Label(frame_contact_list, text=contact["name"]).grid(column=1, row=rows, sticky=W)
        ttk.Label(frame_contact_list, text=contact["second_name"]).grid(column=2, row=rows, sticky=W)
        ttk.Label(frame_contact_list, text=contact["phone_number"]).grid(column=3, row=rows, sticky=W)
        ttk.Label(frame_contact_list, text=contact["adress"]).grid(column=4, row=rows, sticky=W)
        ttk.Label(frame_contact_list, text=contact["mail"]).grid(column=5, row=rows, sticky=W)
        index +=1

def main():

    contacts = load_contact()

    #Editar contactos
    root = Tk()
    frame_add_contact = ttk.Frame(root, padding="50 50 50 50")
    frame_add_contact.grid()

    name = StringVar()
    second_name = StringVar()
    phone = StringVar()
    adress = StringVar()
    mail = StringVar()

    ttk.Label(frame_add_contact, text="Nombre").grid(column=1, row=1, sticky=W)
    ttk.Label(frame_add_contact, text="Apellido").grid(column=2, row=1, sticky=W)
    ttk.Label(frame_add_contact, text="Teléfono").grid(column=3, row=1, sticky=W)
    ttk.Label(frame_add_contact, text="Dirección").grid(column=4, row=1, sticky=W)
    ttk.Label(frame_add_contact, text="Correo").grid(column=5, row=1, sticky=W)

    ttk.Entry(frame_add_contact, width=20, textvariable=name).grid(column=1, row=2, sticky=W)
    ttk.Entry(frame_add_contact, width=20, textvariable=second_name).grid(column=2, row=2, sticky=W)
    ttk.Entry(frame_add_contact, width=20, textvariable=phone).grid(column=3, row=2, sticky=W)
    ttk.Entry(frame_add_contact, width=20, textvariable=adress).grid(column=4, row=2, sticky=W)
    ttk.Entry(frame_add_contact, width=20, textvariable=mail).grid(column=5, row=2, sticky=W)

    ttk.Button(frame_add_contact,
               text="Añadir",
               command=lambda: add_contacts_tk(contacts, name.get(), second_name.get(), phone.get(), adress.get(), mail.get(), frame_contact_list)).grid(column=5, row=4)

    #Lista de contactos

    frame_contact_list = ttk.Frame(root, padding="50 0 50 50")
    frame_contact_list.grid()

    ttk.Label(frame_contact_list, width=20, text="Nombre").grid(column=1, row=1, sticky=W)
    ttk.Label(frame_contact_list, width=20, text="Apellido").grid(column=2, row=1, sticky=W)
    ttk.Label(frame_contact_list, width=20, text="Teléfono").grid(column=3, row=1, sticky=W)
    ttk.Label(frame_contact_list, width=20, text="Dirección").grid(column=4, row=1, sticky=W)
    ttk.Label(frame_contact_list, width=20, text="Correo").grid(column=5, row=1, sticky=W)

    show_loaded_contacts(contacts, frame_contact_list)

    root.mainloop()

if __name__ == "__main__":
    main()