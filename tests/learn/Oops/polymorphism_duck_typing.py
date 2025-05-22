'''

Polymorphism mean - one thing different behaviours or forms
> duck typing
> method overlaodig
> method overiding

'''


class Pycharm:
    def execute(self):
        print("compiled")
        print("run")


class Myeditor:
    def execute(self):
        print("spellcheck")
        print("do more things")
        print("compilation")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = Pycharm()
ide2 = Myeditor()

lap1 = Laptop()
lap1.code(ide)
lap1.code(ide2)
