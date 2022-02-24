from mimetypes import init

class Contributor:
    def __init__(self):
        self.name = ""
        self.no_skills = 0
        self.skills = {}
        self.first_day_available = 0

class Project:
    def __init__(self, name, no_days, score, deadline, no_roles):
        self.name = name
        self.no_days = no_days
        self.score = score
        self.deadline = deadline
        self.no_roles = no_roles
        self.roles = {}
        self.assigned = False

class ProjectRole:
    def __init__(self, required_level, index):
        self.required_level = required_level
        self.index = index

contributors = []
projects = []

in_file = "team_inputs/a_an_example.in.txt"

with open(in_file, "r") as f:
    first_line = f.readline()
    no_contributors, no_projects = map(lambda x: int(x), first_line.split())
    for i in range(no_contributors):
        contributor = Contributor()
        name, no_skills = f.readline().split()
        contributor.no_skills = int(no_skills)
        contributor.name = name
        for j in range(contributor.no_skills):
            skill_name, skill_level = f.readline().split()
            contributor.skills[skill_name] = skill_level
        contributors.append(contributor)


    for i in range(no_projects):
        name, no_days, score, deadline, no_roles = f.readline().split()
        project = Project(name, int(no_days), int(score), int(deadline), int(no_roles))
        for j in range(project.no_roles):
            name, required_lvl = f.readline().split()
            project.roles[name] = ProjectRole(int(required_lvl),int(j))

        projects.append(project)


pass
