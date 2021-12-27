
class Work:
    def __init__(self,
                 position,
                 institution,
                 dateStart,
                 dateEnd,
                 responsibilities):
        self.position = position;
        self.institution = institution;
        self.dateStart = dateStart;
        self.dateEnd = dateEnd;

gra_ua_2021 = Work(position = "Graduate Research Assitant",
                   institution = "University of Arizona",
                   dateStart = "2021-08-15",
                   dateEnd = "present",
                   responsibilities = "Applied physics-informed machine learning to extend phenomenological models of turbulence");

gra_lanl_2021 = Work(position = "Graduate Student Researcher",
                     institution = "Los Alamos National Laboratory",
                     dateStart = "2021-05-13",
                     dateEnd = "2021-08-15",
                     responsibilities = "");

gra_ua_2020 = Work(position = "Graduate Research Assistant",
                   institution = "University of Arizona",
                   dateStart = "2020-08-15",
                   dateEnd = "2021-05-13",
                   responsibilities = "");

gra_lanl_2020 = Work(position = "Graduate Student Researcher",
                     institution = "Los Alamos National Laboratory",
                     dateStart = "2020-05-13",
                     dateEnd = "2020-08-15",
                     responsibilities = "");

gta_ua_2019 = Work(position = "Graduate Teaching Assistant",
                   institution = "University of Arizona",
                   dateStart = "2019-08-15",
                   dateEnd = "2020-05-13",
                   responsibilities = "");

swe_rms_2016 = Work(position = "Software Engineer II",
                    institution = "Raytheon Missile Systems",
                    dateStart = "2016-05-13",
                    dateEnd = "2019-08-15",
                    responsibilities = "");

workExperience = [gra_ua_2021,
                  gra_lanl_2021,
                  gra_ua_2020,
                  gra_lanl_2020,
                  gta_ua_2019,
                  swe_rms_2016];
