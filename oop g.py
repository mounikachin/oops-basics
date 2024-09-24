class inst:
    clg = 'jsp'

    def __init__(self, name, mbno, course):
        self.name = name
        self.mbno = mbno
        self.course = course

    def display(self):
        print(f'name:{self.name}')
        print(f'mbno:{self.mbno}')
        print(f'corse:{self.course}')

print(inst.clg)
obj=inst('mouni',9392,'pyt')
obj.display()
print(obj.clg)




