
list_with_color = []

def add_color(temp_list):
    for item in temp_list:
        list_year = []
        for i in item:
            i = list(i)
            if i[1] == '':
                i[1] = None
            if i[1] != None:
                if float(i[1]) < 0:
                    color = 'green'
                    i.append(color)
                elif i[0] == 'Год':
                    color = 'white'
                    i.append(color)
                elif 0 <= float(i[1]) <= 1 and i[0] != 'Суммарная':
                    color = 'white'
                    i.append(color)
                elif 1 < float(i[1]) <= 2 and i[0] != 'Суммарная':
                    color = '#F6CECE'
                    i.append(color)
                elif 2 < float(i[1]) <= 5 and i[0] != 'Суммарная':
                    color = '#FA5858'
                    i.append(color)
                elif i[0] != 'Суммарная' and 5 < float(i[1]):
                    color = '#DF0101'
                    i.append(color)
                elif i[0] == 'Суммарная':
                    color = 'grey'
                    i.append(color)
            else:
                color = 'white'
                i.append(color)

            list_year.append(i)

        list_with_color.append((list_year))
    return list_with_color