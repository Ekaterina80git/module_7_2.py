

def custom_write(file_name,strings):
    # strings список строк для записи
    # записывает в file_name все строки из списка strings,каждая с новой строки
    strings_position = {}
    file = open(file_name,'a',encoding= 'utf-8')
    for i,v in enumerate(strings):
        key = (i+1,file.tell())
        strings_position[key] = v
        file.write(v + '\n')
    file.close()
    return strings_position # возвращает словарь где ключ кортеж номер строки и байт
    # начала строки а значение записываемая строка
def main():
    info = [
        'Text for tell.',
         'Используйте кодировку utf-8',
         'Because ther are 2 languages!',
         'Спасибо!'
    ]

    result = custom_write('test.txt',info)
    for elem in result.items():
        print(elem)
if __name__== '__main__':
     main()














