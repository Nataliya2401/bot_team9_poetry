from abc import ABC, abstractmethod
from shutil import get_terminal_size


class UserInterface(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def output(self):
        pass


class PrintMessage(UserInterface):
    def output(self):
        print(self.value)


class PrintList(UserInterface):
    def output(self):
        for el in self.value:
            print(el)


def delimiter_text(text, length):
    idx_begin = 0
    idx_end = length
    lists = []
    while idx_begin <= len(text):
        lists.append(text[idx_begin:idx_end])
        idx_begin = idx_end
        idx_end += length
    return lists


class PrintNote(UserInterface):
    def output(self):
        table_width = get_terminal_size().columns - 2
        string = ""
        if not self.value or type(self.value[0]) == str:
            print("-" * table_width)
            string = "|{:^" + str(table_width - 2) + "}|"
            print(string.format("No notes"))
            print("-" * table_width)
            return True
        for note in self.value:
            if type(note) == tuple:
                titles = note[1].title.capitalize()
                tags = note[1].tags
                texts = note[1].text
            else:
                titles = note.title.capitalize()
                tags = note.tags
                texts = note.text
            print("-" * table_width)
            string = "|{:^" + str(table_width - 2) + "}|"
            print(string.format(titles))
            print("-" * table_width)
            string = "|{:^" + str(table_width - 2) + "}|"
            print(string.format(", ".join(tags)))
            print("-" * table_width)
            texts = delimiter_text(texts, table_width - 4)
            for text in texts:
                string = "| {:<" + str(table_width - 4) + "} |"
                print(string.format(text))
            print("-" * table_width, "\n\n")


class PrintTable(UserInterface):
    @staticmethod
    def table_header():
        columns = ["Name", "Address", "Email", "Birthday", "Phones"]
        table_width = get_terminal_size().columns - 3
        column_width = (get_terminal_size().columns - 2) // 5 - 1
        print("-" * table_width)
        print_string = "|"
        for _ in columns:
            print_string += " {:^" + str(column_width - 2) + "} |"
        print(print_string.format(*columns))
        print("-" * table_width)

    def print_contacts(self):
        columns = ["Name", "Address", "Email", "Birthday", "Phones"]
        table_width = get_terminal_size().columns - 3
        column_width = (get_terminal_size().columns - 2) // 5 - 1
        print_string = "|"
        for _ in columns:
            print_string += " {:^" + str(column_width - 2) + "} |"
        for contact in self.value:
            cnt_rows = 0
            name = delimiter_text(str(contact.name).capitalize(), column_width - 2)
            if len(name) > cnt_rows:
                cnt_rows = len(name)
            address = delimiter_text(contact.address, column_width - 2)
            if len(address) > cnt_rows:
                cnt_rows = len(address)
            email = delimiter_text(str(contact.email), column_width - 2)
            if len(email) > cnt_rows:
                cnt_rows = len(email)
            birthday = delimiter_text(str(contact.birthday), column_width - 2)
            if len(birthday) > cnt_rows:
                cnt_rows = len(birthday)
            phones = []
            for phone in contact.phones:
                if phone:
                    phones.append(phone.value)
            phones = phones if phones else [""]
            for i in range(cnt_rows):
                name_print = name[i] if i < len(name) else ""
                address_print = address[i] if i < len(address) else ""
                email_print = email[i] if i < len(email) else ""
                birthday_print = birthday[i] if i < len(birthday) else ""
                phones_print = phones[i] if i < len(phones) else ""
                print(
                    print_string.format(
                        name_print,
                        address_print,
                        email_print,
                        birthday_print,
                        phones_print,
                    )
                )
            print("-" * table_width)

    def output(self):

        self.table_header()
        self.print_contacts()
