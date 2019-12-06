from Workers.WorkerAndFired import Worker


class Administrator(Worker):
    chief = None
    duty_of_adm = None
    monitor_of_unit = None
    helper = None

    def __init__(self, last, first, father, sex, rate, type_work, position,insurance, military_ID):
        super().__init__(last, first, father, sex, rate, type_work,position, insurance, military_ID)

    def change_chief(self, new_chief):
        self.chief = new_chief
        return self.chief

    def clear_chief(self):
        self.chief = None
        return self.chief

    def add_duty_of_adm(self, new_duty):
        self.duty_of_adm = self.duty_of_adm + new_duty
        return self.duty_of_adm

    def change_duty_of_adm(self, new_duty):
        self.duty_of_adm = new_duty
        return self.duty_of_adm

    def add_monitor_of_unit(self, new_unit):
        self.monitor_of_unit = self.monitor_of_unit + new_unit
        return self.monitor_of_unit

    def change_monitor_of_unit(self, new_unit):
        self.monitor_of_unit = new_unit
        return self.monitor_of_unit

    def add_helper(self, new_helper):
        self.helper = self.helper + new_helper
        return self.helper

    def change_helper(self, new_helper):
        self.helper = new_helper
        return self.helper
