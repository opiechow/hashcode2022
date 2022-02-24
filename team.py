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
        self.roles = []
        self.assigned = False

class ProjectRole:
    def __init__(self, name, required_level, index):
        self.name = name
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
            project.roles.append(ProjectRole(name,int(required_lvl),int(j)))

        projects.append(project)

projects.sort(key = lambda x: x.score)
max_day = projects[-1].deadline + projects[-1].score
for day in range(max_day):
    for project in projects:
        if project.assigned:
            continue
        possible_assignments = {}
        for contributor in filter(lambda x: x.first_day_available <= day, contributors):
            role_set = project.roles.map(lambda x: x.name)
            skill_set = set(contributor.skills.keys())
            common_skills = skill_set.intersection(role_set)
            if len(common_skills) == 0:
                continue
            for common_skill in common_skills:
                if project.roles[common_skill].required_level >= contributor[common_skill]:
                    #contributor.first_day_available = day + project.no_days
                    possible_assignments[common_skill] = contributor.name
                    continue
        


pass
