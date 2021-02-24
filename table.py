
def create_table(file):
    sql = open(file, "r")
    line = sql.readline().strip()
    while len(line) == 0:
        line = sql.readline().strip()
    check_first(line.split(" "))
    pass


# Problem: What if there is a space between the name and (
def check_first(line):
    if (len(line) != 3 and len(line) != 4) or line[0].upper() != 'CREATE':
        raise Exception



