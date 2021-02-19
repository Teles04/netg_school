from django.shortcuts import render

import csv

from app.management.commands.add_color import add_color


def inflation_view(request):
    dict_from_file = []
    temp_list = []
    with open('inflation_russia.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            dict_from_file.append(row)

    for row in dict_from_file:
        dict_keys = row.keys()
        temp_list.append(row.items())

    list_with_color = add_color(temp_list)

    context = {
        'keys': dict_keys,
        'list': list_with_color,
    }
    return render(request, 'inflation.html', context)




