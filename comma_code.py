def comma(items):
    if len(items)==0:
        return ""
    elif len(items)==1:
        return str(items[0])
    else:
        formatted_items = ', '.join(map(str,items[:-1]))
        return f"{formatted_items}, and {items[-1]}"

spam = ['apples', 'bananas', 'tofu', 'cats']
formatted_items = comma(spam)
print(formatted_items)
