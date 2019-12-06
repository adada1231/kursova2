from Workers.WorkerAndFired import Worker

class HR(Worker):
    positions = None
    for_whom = None
    duty_of_hr = None

    def __init__(self, last, first, father, sex, rate, type_work, position, insurance, military_ID):
        super().__init__(last, first, father, sex, rate,type_work, position, insurance, military_ID)

    def change_duty_of_hr(self, new_duty):
        self.duty_of_hr = new_duty

    def add_duty_of_hr(self, new_duty):
        self.duty_of_hr = self.duty_of_hr + new_duty
        return self.duty_of_hr


    def add_for_whom(self, new_whom):
        self.for_whom = self.for_whom + " " + new_whom
        return self.for_whom

    def add_positions(self, new_positions):
        self.positions = self.positions + new_positions
        return self.positions

    def change_for_whom(self, new):
        self.for_whom = new
        return self.for_whom