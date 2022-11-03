import re
import csv

def read_file(file_name):
    with open(file_name) as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def format_phone_number(contacts_list):
    number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    contacts_list_updated = list()
    for record in contacts_list:
        record_as_string = ','.join(record)
        formatted_record = re.sub(number_pattern_raw, number_pattern_new, record_as_string)
        record_as_list = formatted_record.split(',')
        contacts_list_updated.append(record_as_list)
    return contacts_list_updated


def format_names(contacts_list):
    name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'

    name_pattern_new = r'\1\3\9\4\6\9\7\8'
    contacts_list_updated = list()
    for record in contacts_list:
        record_as_string = ','.join(record)
        formatted_record = re.sub(name_pattern_raw, name_pattern_new, record_as_string)
        record_as_list = formatted_record.split(',')
        contacts_list_updated.append(record_as_list)
    return contacts_list_updated


def join_doubles(contacts_list):
    for x in contacts_list:
        for y in contacts_list:
            if x[0] == y[0] and x[1] == y[1] and x != y:
                if x[2] == '': x[2] = y[2]
                if x[3] == '': x[3] = y[3]
                if x[4] == '': x[4] = y[4]
                if x[5] == '': x[5] = y[5]
                if x[6] == '': x[6] = y[6]
    contacts_list_updated = list()
    for record in contacts_list:
        if record not in contacts_list_updated:
            contacts_list_updated.append(record)
    return contacts_list_updated


def write_file(contacts_list, file_name):
    with open(file_name, "w") as f:
        data_writer = csv.writer(f, delimiter=',')
        data_writer.writerows(contacts_list)


if __name__ == '__main__':
    contacts_list = read_file('phonebook_raw.csv')
    contacts_list = format_phone_number(contacts_list)
    contacts_list = format_names(contacts_list)
    contacts_list = join_doubles(contacts_list)
    write_file(contacts_list,'phonebook.csv')