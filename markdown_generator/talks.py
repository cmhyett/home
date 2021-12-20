import os

class Talk:
    def __init__(self,
                 title,
                 talk_type,
                 url_slug,
                 venue,
                 date,
                 location,
                 talk_url,
                 description):
        self.title = title;
        self.talk_type = talk_type;
        self.url_slug = url_slug;
        self.venue = venue;
        self.date = date;
        self.location = location;
        self.talk_url = talk_url;
        self.description = description;

aps2020 = Talk(title = "Machine Learning Statistical Lagrangian Geometry of Turbulence",
               talk_type = "talk",
               url_slug = "aps2020",
               venue = "APS Division of Fluid Dynamics Meeting",
               date = "2020-11-21",
               location = "online",
               talk_url = "none",
               description = "Recently, there has been a lot of interest in applying machine learning techniques to capture Lagrangian dynamics of fluid particles in turbulent flows. We extend this work in search of Lagrangian dynamics of coarse-grained fluid volume/geometry and velocity gradient. Our work builds on the machine learning of Lagrangian dynamics, as well as the development of phenomenological reduced order models by approximating the closure of a physics-based model using neural networks to create a parameterized stochastic differential equation; coupling the evolution of the geometry to the evolution of the coarse-grained dynamical quantities; including deterministic and stochastic dynamics. Further, because the stochastic terms are themselves parameterized, we are able to target higher-order moments of dynamical quantities of interest. We train and evaluate the parameterized SDE against filtered Lagrangian DNS data to obtain a data-driven closure to the hypothesized model. We then evaluate the trained model to recover the learned insights to the phenomenological model.");

brownBag2020 = Talk(title = "Machine Learning Stochastic Differential Equations: Applications in Reduced Order Models of Turbulence",
               talk_type = "talk",
               url_slug = "bbSpring2021",
               venue = "University of Arizona, SIAM Student Brownbag Colloquium",
               date = "2021-03-26",
               location = "online",
               talk_url = "none",
               description = "The ubiquity of turbulence, as well as the importance and difficulty of its simulation are well-known. To combat the computational complexity, physically motivated phenomenological theories of reduced-order models have been hypothesized. While very interpretable, these theories struggle to match DNS results. We look to extend these phenomenological models, via neural networks. In this talk, I will focus mainly on our general training methodology to learn extensions to stochastic differential equations, and then touch on our applications to turbulence at the end.");

aps2021 = Talk(title = "Machine Learning Statistical Evolution of the Coarse-Grained Velocity Gradient Tensor",
               talk_type = "talk",
               url_slug = "aps2021",
               venue = "APS Division of Fluid Dynamics Meeting",
               date = "2021-11-20",
               location = "Phoenix, AZ",
               talk_url = "none",
               description = "We exploit recent advances in physics-informed machine learning and phenomenological theories of turbulence to develop parameterized stochastic differential equations (SDEs) coupling the Lagrangian evolution of a fluid volume to the coarse-grained velocity gradient tensor; resulting in a reduced order model for incompressible turbulence. Choosing minimal representations of fluid geometry and velocity gradient tensor, we search for local approximations to nonlinear (pressure and subgrid) terms. The goal is achieved by optimizing physics-informed neural networks - dependent on the coupled system of fluid geometry and velocity gradient tensor - over high fidelity Lagrangian direct numerical simulation data. We demonstrate the ability of the parameterized SDEs to reproduce the topological statistics of the coarse-grained velocity gradient tensor, as well as the shape distributions of the respective fluid elements.");


talks = [aps2020, 
         brownBag2020,
         aps2021];


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


for item in talks:
    
    md_filename = str(item.date) + "-" + item.url_slug + ".md"
    html_filename = str(item.date) + "-" + item.url_slug 
    year = item.date[:4]
    
    md = "---\ntitle: \""   + item.title + '"\n'
    md += "collection: talks" + "\n"
    
    if len(str(item.talk_type)) > 3:
        md += 'type: "' + item.talk_type + '"\n'
    else:
        md += 'type: "Talk"\n'
    
    md += "permalink: /talks/" + html_filename + "\n"
    
    if len(str(item.venue)) > 3:
        md += 'venue: "' + item.venue + '"\n'
        
    if len(str(item.location)) > 3:
        md += "date: " + str(item.date) + "\n"
    
    if len(str(item.location)) > 3:
        md += 'location: "' + str(item.location) + '"\n'
           
    md += "---\n"
    
    
    if len(str(item.talk_url)) > 3:
        md += "\n[More information here](" + item.talk_url + ")\n" 
        
    
    if len(str(item.description)) > 3:
        md += "\n" + html_escape(item.description) + "\n"
        
        
    md_filename = os.path.basename(md_filename)
    #print(md)
    
    with open("../_talks/" + md_filename, 'w') as f:
        f.write(md)

