import os

class Teaching:
    def __init__(self,
                 title,
                 teaching_type,
                 url_slug,
                 venue,
                 date,
                 location,
                 description):
        self.title = title;
        self.teaching_type = teaching_type;
        self.url_slug = url_slug;
        self.venue = venue;
        self.date = date;
        self.location = location;
        self.description = description;

math112_fall2019 = Teaching(title = "Math 112",
                            teaching_type = "Teaching Assistant",
                            url_slug = "112",
                            venue = "University of Arizona",
                            date = "2019-08-01",
                            location = "Tucson, Arizona",
                            description = "Assisted in development of course materials, leading lectures, and grading.")

math112_spring2019 = Teaching(title = "Math 112",
                              teaching_type = "Teaching Assistant",
                              url_slug = "112",
                              venue = "University of Arizona",
                              date = "2020-01-01",
                              location = "Hybrid online",
                              description = "Assisted in development of course materials, leading lectures, and grading.")

teaching = [math112_fall2019,
            math112_spring2019]

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    if type(text) is str:
        return "".join(html_escape_table.get(c,c) for c in text)
    else:
        return "False"


for item in teaching:

    if ((str.lower(item.date).find('spring') != -1) or
        (str.lower(item.date).find('fall') != -1)):
        yearInd = item.date.find('20');
        md_filename = item.date[yearInd:yearInd+4] + "-" + item.url_slug + ".md";
        html_filename = item.date[yearInd:yearInd+4] + "-" + item.url_slug;
    else:
        md_filename = str(item.date) + "-" + item.url_slug + ".md";
        html_filename = str(item.date) + "-" + item.url_slug;

    md = "---\ntitle: \""   + item.title + '"\n'
    md += "collection: teaching" + "\n"
    md += 'type: "' + item.teaching_type + '"\n'
    md += "permalink: /talks/" + html_filename + "\n"
    md += 'venue: "' + item.venue + '"\n'
    md += "date: " + str(item.date) + "\n"
    md += 'location: "' + str(item.location) + '"\n'
    md += "---\n"
    
    md += "\n" + html_escape(item.description) + "\n"
        
    md_filename = os.path.basename(md_filename)
    print(md)
    
    with open("../_teaching/" + md_filename, 'w') as f:
        f.write(md)

