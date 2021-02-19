from django.shortcuts import render


import csv

def inflation_view(request):
    data_from_csv = []
    dfc = []
    new_dict = []
    with open('inflation_russia.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            dfc.append(row)
    for row in dfc:
        dict_keys = row.keys()
    for row in dfc:
        new_dict.append(row.items())
#    for rows in dfc:
#        dict_values.append(rows.values())
    context = {
        'd_f_c': dfc,
        'keys': dict_keys,
        'dict': new_dict,
    }
    return render(request, 'inflation.html', context)




