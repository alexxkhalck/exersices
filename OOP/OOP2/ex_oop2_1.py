# Створіть клас Editor, який містить методи view_document та edit_document. Нехай метод
# edit_document виводить на екран інформацію про те, що редагування документів недоступне для
# безкоштовної версії. Створіть підклас ProEditor, у якому цей метод буде перевизначено.
# Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor,
# інакше Editor. Викликайте методи перегляду та редагування документів.
class Editor:
    def view_document(self):
        pass

    def edit_document(self):
        print('Редагування документів недоступне для безкоштовної версії.')

class ProEditor(Editor):
    lic_key = 'H4F9KJD6'

    def edit_document(self, ):
        print('Ви маєте ліцензію. Редагування документів дозволено.')

user_key = input('Введіть ліцензійний ключ: ')
if user_key == ProEditor.lic_key:
    editor = ProEditor()
    editor.view_document()
    editor.edit_document()
else:
    editor = Editor()
    editor.view_document()
    editor.edit_document()

