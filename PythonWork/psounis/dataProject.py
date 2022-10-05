pupils = [
    {
        "id": 1001,
        "name": "John",
        "surname": "Doe",
        "father_name": "Michael",
        "age": 11,
        "class": 1,
        "id_number": "CLASS123"
    },
    {
        "id": 1002,
        "name": "Raf",
        "surname": "Bakoulis",
        "father_name": "Mitliadis",
        "age": 8,
        "class": 2,
        "id_number": "CLASS124"
    },
    {
        "id": 1003,
        "name": "Eleni",
        "surname": "Kotidou",
        "father_name": "Stamatis",
        "age": 12,
        "class": 3,
        "id_number": "CLASS125"
    },
]


# functions

def print_pupil(pupil):
    print(f"Name          : {pupil['name']}")
    print(f"Surname       : {pupil['surname']}")
    print(f"Father Name   : {pupil['father_name']}")
    print(f"Age           : {pupil['age']}")
    print(f"Class         : {pupil['class']}")
    if "id_number" in pupil:
        print(f"Id card number: {pupil['id_number']}")


def next_id():
    ids = []
    for p in pupils:
        ids.append(p["id"])
    return max(ids) + 1


def create_pupil():
    name = input("Give name: ")
    surname = input("Give surname: ")
    father_name = input("Give the father's name: ")

    stop = False
    for p in pupils:
        if name == p["name"] and surname == p["surname"] and father_name == p["father_name"]:
            print("The pupil already exists. ")
            ch = input("Do you want to continue? (y-yes, n-no)")
            if ch == "n":
                return None

    age = int(input("Give an age: "))
    pupil_class = int(input("Give the class: "))

    print("Does the student has an id card")
    id_card = input("? ")
    if id_card == "y":
        id_number = input("Give id card number")

    pupil = {"name": name, "surname": surname, "father_name": father_name, "age": age, "class": pupil_class}

    if id_card == "y":
        pupil["id_number"] = id_number

    pupil["id"] = next_id()

    pupils.append(pupil)
    return pupil


def search_pupil_by_id(pupil_id):
    for pupil in pupils:
        if pupil_id == pupil['id']:
            return pupil
    return None


def search_pupil_by_surname(surname):
    match_pupils = []
    for pupil in pupils:
        if surname == pupil['surname']:
            match_pupils.append(pupil)
    return match_pupils


def pupil_update(pupil):
    print_pupil(pupil)
    print("=" * 15)
    print("1 - name")
    print("2 - surname")
    print("3 - father's name")
    print("4 - age")
    print("5 - class")
    print("6 - id number")
    print("=" * 15)

    update_choice = int(input("Pick something to update: "))
    if update_choice == 1:
        pupil['name'] = input("Give new name: ")
    elif update_choice == 2:
        pupil['surname'] = input("Give new surname: ")
    elif update_choice == 3:
        pupil['father_name'] = input("Give new Father's Name: ")
    elif update_choice == 4:
        pupil['age'] = input("Give new age: ")
    elif update_choice == 5:
        pupil['class'] = input("Give new class: ")
    elif update_choice == 6:
        pupil['id_number'] = input("Give new id_number: ")


def delete_pupil_by_id(id):
    for i in range(len(pupils)):
        if id == pupils[i]['id']:
            pupils.pop(i)
            return


def print_pupils_details():
    for pupil in pupils:
        print("=" * 15)
        print_pupil(pupil)


def print_pupils_names():
    for pupil in pupils:
        print(f"{pupil['name']} {pupil['father_name'][0]}. {pupil['surname']}")


def main():
    while True:
        print("\n==============")
        print("    Menu")
        print("1 - Create Pupil")
        print("2 - Print")
        print("3 - Update Pupil")
        print("4 - Delete Pupil")
        print("5 - Exit")

        choice = int(input("Pick One: "))

        if choice == 1:
            print("New Pupil")
            print("===========")

            pupil = create_pupil()
            if pupil is None:
                continue
            else:
                print("New Pupil")
                print_pupil(pupil)
            print(pupils)

        elif choice == 2:
            print("\n==============")
            print("    Sub - Menu")
            print("1 - Print Pupil")
            print("2 - Print all Pupils (Details)")
            print("3 - Print all Pupils (just the names)")

            print_choice = input("Give you choice: ")

            if print_choice.strip().isdigit():
                print_choice = int(print_choice)
            else:
                print("Wrong Input! ")
                continue

            if print_choice == 1:
                pupil_id = int(input("Give id: "))
                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Pupil does not exist")
                else:
                    print("  Pupil   ")
                    print_pupil(pupil)
            elif print_choice == 2:
                print_pupils_details()
            elif print_choice == 3:
                print_pupils_names()
            else:
                print("Wrong Input! ")

        elif choice == 3:
            print("\n==============")
            print("    Sub - Menu")
            print("1 - Update Pupil (by id)")
            print("2 - Update (by surname)")
            update_choice = input("Give your choice: ")
            if update_choice.strip().isdigit():
                update_choice = int(update_choice)
            else:
                print("Wrong Input")
                continue

            if update_choice == 1:
                pupil_id = int(input("Give id: "))
                pupil = search_pupil_by_id(pupil_id)

                if pupil is None:
                    print("Error!! There is no pupili with this id!")
                    continue
            elif update_choice == 2:
                surname = input("Give surname")
                matching_pupils = search_pupil_by_surname(surname)
                if not matching_pupils:
                    print("No matching pupils with this surname")
                    continue
                elif len(matching_pupils) == 1:
                    pupil = matching_pupils[0]
                else:
                    for p in matching_pupils:
                        print_pupil(pupil)
                        print(f"id = {p['id']}")
                        print("=" * 15)
                    pupil_id = int(input("More that 1 pupils found, give the id: "))
                    pupil = search_pupil_by_id(pupil_id)

            # pupil update
            pupil_update(pupil)
            print("=" * 15)
            print_pupil(pupil)
            print("Pupil Updated")

        elif choice == 4:
            print("\n==============")
            print("    Sub - Menu")
            print("1 - Delete Pupil (by id)")
            print("2 - Delete (by surname)")
            delete_choice = input("Give your choice: ")
            if delete_choice.strip().isdigit():
                delete_choice = int(delete_choice)
            else:
                print("Wrong Input")
                continue

            if delete_choice == 1:
                pupil_id = int(input("Give id: "))
                pupil = search_pupil_by_id(pupil_id)

                if pupil is None:
                    print("Error!! There is no pupili with this id!")
                    continue
            elif delete_choice == 2:
                surname = input("Give surname")
                matching_pupils = search_pupil_by_surname(surname)
                if not matching_pupils:
                    print("No matching pupils with this surname")
                    continue
                elif len(matching_pupils) == 1:
                    pupil = matching_pupils[0]
                else:
                    for p in matching_pupils:
                        print_pupil(pupil)
                        print(f"id = {p['id']}")
                        print("=" * 15)
                    pupil_id = int(input("More that 1 pupils found, give the id: "))
                    pupil = search_pupil_by_id(pupil_id)

            # pupil delete
            delete_pupil_by_id(pupil['id'])

        elif choice == 5:
            print("You have exited the programm")
            break


main()
