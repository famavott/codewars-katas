"""Format a string of names from list of dicts."""


def namelist(names):
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    elif len(names) == 2:
        return names[0]['name'] + ' & ' + names[1]['name']
    else:
        name_list = [x['name'] for x in names]
        names = ', '.join(name_list[:-1])
        return names + ' & ' + name_list[-1]
