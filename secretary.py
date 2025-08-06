'''Каталог документов хранится в следующем виде:'''
DOCS = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

'''Перечень полок, на которых находятся документы:'''
DIRS = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name(doc_number):
    """
    Принимает номер документа и выводит имя человека, которому он принадлежит. 
    Если такого документа не существует, вывести “Документ не найден”.
    """
    doc_name = None
    for doc in DOCS:
        if doc['number'] == doc_number:
            doc_name = doc['name']
    if doc_name is None:
        doc_name = 'Документ не найден'
    return doc_name

def get_directory(doc_number):
    """
    Принимает номер документа и выводит номер полки, на которой он находится. 
    Если такой документ не найден, на полках вывести “Полки с таким документом не найдено”.
    """
    doc_shelf = None
    for key, val in DIRS.items():
        if doc_number in val:
            doc_shelf = key
    if doc_shelf is None:
        doc_shelf = 'Полки с таким документом не найдено'
    return doc_shelf
    
def add(document_type, number, name, shelf_number):
    """добавить новый документ в каталог и перечень полок"""
    new = {"type": document_type, 
           "number": number, 
           "name": name}
    DOCS.append(new)
    DIRS[str(shelf_number)].append(number)
    return

if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))