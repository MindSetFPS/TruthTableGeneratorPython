import math

# TODO TIENE QUE SER VERDADERO
def And(a, b):
    # print(a and b)
    return a and b


# AL MENOS UNO TIENE QUE SER VERDADERO
def Or(a, b):
    # print(a or b)
    return a or b

# SE INVIERTE LA SENAL
def Not(a):
    return not a

def CIRCUIT1(row):
    a = row[0]
    c = row[1]
    d = row[2]

    ac = And(a,c)
    dc = And(d, c)
    ac_or_dc = Or(ac, dc)
    not_ac_or_dc = Not(ac_or_dc)
    ac_or_not_ac_or_dc = Or(ac, not_ac_or_dc)
    ac_or_not_ac_or_dc = int(ac_or_not_ac_or_dc)
    return ac_or_not_ac_or_dc
# AC(0, 0, 0)
def CIRCUIT2(row):
    a = row[0]
    c = row[1]
    d = row[2]
    e = row[3]

    a_or_c = Or(a, c)
    not_a_or_c = Not(a_or_c)
    not_a_or_c_and_d = And(not_a_or_c, d)
    not_a_or_c_and_d_or_e = Or(not_a_or_c_and_d, e)
    return not_a_or_c_and_d_or_e

def CIRCUIT3(row):
    a = row[0]
    c = row[1]
    d = row[2]
    b = row[3]
    e = row[4]

    a_and_c = And(a, c)
    a_and_c_and_d = And(a_and_c, d)
    not_a_and_c_and_d = Not(a_and_c_and_d)
    c_and_d = And(c, d)
    not_acd_and_cd = And(not_a_and_c_and_d, c_and_d)
    be = And(b, e)
    not_acd_and_cd_or_be = Or(not_acd_and_cd, be)
    return not_acd_and_cd_or_be

def CIRCUIT4(row):
    a = row[0]
    d = row[1]
    c = row[2]
    b = row[3]

    ad = And(a, d)
    cd = And(c, d)
    ad_or_cd = Or(ad, cd)
    ab = And(a, b)
    abc = And(ab, c)
    not_abc = Not(abc)
    ad_or_cd_and_not_abc = And(ad_or_cd, not_abc)
    return ad_or_cd_and_not_abc

def TruthTable(inputs):
    columns = []
    column_length = int(math.pow(2, inputs))
    for fcolumn in range(1, inputs + 1):
        column_pattern_length = int(math.pow(2, fcolumn))

        rows = []
        column_pattern = []
        for position in range(0, column_pattern_length):
            if(position < column_pattern_length / 2):
                column_pattern.append(0)
            else:
                column_pattern.append(1)

        column_pattern_to_fill_column = int(column_length / column_pattern_length)
        final_column = column_pattern_to_fill_column * column_pattern
        columns.append(final_column)
        columns.reverse()
    for vertical in range(0, column_length):
        row = []
        for horizontal in range(0, len(columns)):
            # print(columns[horizontal][vertical], end="")
            row.append(columns[horizontal][vertical])
        row.append(CIRCUIT4(row))
        print(*row, end="", sep=",")
        print()

# TruthTable(1)
# TruthTable(2)
# TruthTable(3)
TruthTable(4)
# TruthTable(5)
# TruthTable(6)
