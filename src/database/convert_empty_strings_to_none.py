
def convert_empty_strings_to_none(rows, structure):
    new_rows = []
    for row in rows:
        new_row = []
        for idx, value in enumerate(row):
            if value == "" and structure[idx][2].upper() == "INTEGER":
                new_row.append(None)
            else:
                new_row.append(value)
        new_rows.append(tuple(new_row))
    return new_rows