# Опишіть два класи Base та його спадкоємця Child з методами method(), який виводить на консоль
# фрази відповідно "Hello from Base" та "Hello from Child", using classmethod (@classmethod) decorator.
class Base:
    @classmethod
    def method(cls):
        print('Hello from Base')

class Child(Base):
    @classmethod
    def method(cls):
        super().method()
        print('Hello from Child')

child = Child()
child.method()