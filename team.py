class Contributor:
    name = ""
    no_skills = 0
    skills = {}

class Project:
    name = ""
    no_days = ""
    score = 0
    deadline = 0
    no_roles = 0
    roles = {}

contributors = []
projects = []

in_file = "team_inputs/a_an_exapmle.in.txt"

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

