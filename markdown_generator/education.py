

class Degree:
    def __init__(self,
                 title,
                 subject,
                 institution,
                 year):
        self.title = title;
        self.subject = subject;
        self.institution = institution;
        self.year = year;

bs = Degree(title = "B.S.",
            subject = "Mathematics & Physics",
            institution = "University of Arizona",
            year = 2016);

ms = Degree(title = "M.S.",
            subject = "Applied Mathematics",
            institution = "University of Arizona",
            year = 2021);

phd = Degree(title = "Ph.D.",
             subject = "Applied Mathematics",
             institution = "University of Arizona",
             year = 2024);

degrees = [phd, ms, bs];
