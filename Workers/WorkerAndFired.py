class Worker:
    num = 0
    status = "Працює"

    def __init__(self, last, first, father, sex, rate, position, type_work, insurance, military_ID, ID = num):
        self.last = last
        self.first = first
        self.father = father
        self.sex = sex
        self.rate = rate
        self.type_work = type_work
        self.position = position
        self.insurance = insurance
        self.military_ID = military_ID
        Worker.num += 1
        self.ID = Worker.num

    @property
    def main_data(self):
        return [self.ID, self.fullname, self.sex, self.rate, self.position, self.type_work, self.insurance,self.military_ID]

    @property
    def fullname(self):
        return str("{} {} {}".format(self.last, self.first, self.father))

    @classmethod
    def new_worker(cls, str):
        last, first, father, sex, rate, position, type_work, insurance, military_ID = str.split(".")
        return cls(last, first, father, sex, rate, position, type_work,  insurance, military_ID)

    def change_last(self, new_last):
        self.last = new_last
        return self.last

    def change_rate(self, new_rate):
        self.rate = new_rate
        return self.rate

    def change_type_work(self, new_type_w):
        self.type_work = new_type_w
        return self.type_work

    def change_position(self, new_position):
        self.position = new_position
        return self.position

    def change_military_ID(self, new_mil_ID):
        self.military_ID = new_mil_ID
        return self.military_ID

    def change_insurance(self, new_insurance):
        self.insurance = new_insurance
        return self.insurance

    def zvilniti(self):
        self.status = "звільнено"

    def change_typework(self, type):
        self.__class__ = type






