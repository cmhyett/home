class Service:
    def __init__(self,
                 title,
                 dateStart,
                 dateEnd):
        self.title = title;
        self.dateStart = dateStart;
        self.dateEnd = dateEnd;

bbOrg_2021 = Service(title = "SIAM Brown Bag Student Colloquium Organizer",
                     dateStart = "2021-08-15",
                     dateEnd = "present");

services = [bbOrg_2021];
