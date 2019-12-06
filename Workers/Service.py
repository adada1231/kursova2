from Workers.WorkerAndFired import Worker


class Service(Worker):
    chief = None
    tools_of_service = None
    area = None

    def __init__(self, last, first, father, sex, rate, type_work,position,insurance, military_ID):
        super().__init__(last, first, father, sex, rate,type_work,position, insurance, military_ID)

    def change_chief(self, new_chief):
        self.chief = new_chief
        return self.chief

    def change_tools_of_service(self, new_tool):
        self.tools_of_service = new_tool
        return self.tools_of_service

    def change_area(self, new_area):
        self.area = new_area
        return self.area

    def add_tools_of_service(self,new_tools):
        self.tools_of_service = self.tools_of_service + new_tools
        return self.tools_of_service

    def add_area(self, new_area):
        self.area = self.area + new_area
        return self.area

