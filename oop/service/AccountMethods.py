
def get_last_id():
    try:
        with open("../../utils/accounts-data.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                return None
            last_line = lines[-1]

            id_part = last_line.split("\t")[0][0]
            return int(id_part)
    except FileNotFoundError:
        pass
