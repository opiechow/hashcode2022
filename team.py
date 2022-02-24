from mimetypes import init

class Contributor:
    def __init__(self):
        self.name = ""
        self.no_skills = 0
        self.skills = []
        self.first_day_available = 0

class Project:
    def __init__(self, name, no_days, score, deadline, no_roles):
        self.name = name
        self.no_days = no_days
        self.score = score
        self.deadline = deadline
        self.no_roles = no_roles
        self.roles = []
        self.mentored_roles = []
        self.assigned_roles = []
        self.assigned = False

class ProjectRole:
    def __init__(self, skill, index):
        self.skill = skill
        self.index = index

contributors = []
projects = []
skills = {}

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
            # skill is name + level
            skill = f.readline().rstrip()
            contributor.skills.append(skill)
            if skill in skills:
                skills[skill].append(contributor)
            else:
                skills[skill] = [contributor]
        contributors.append(contributor)


    for i in range(no_projects):
        name, no_days, score, deadline, no_roles = f.readline().split()
        project = Project(name, int(no_days), int(score), int(deadline), int(no_roles))
        for j in range(project.no_roles):
            skill = f.readline().rstrip()
            project.roles.append(ProjectRole(skill, int(j)))

        projects.append(project)

projects.sort(key = lambda x: x.score)
max_day = projects[-1].deadline + projects[-1].score
for day in range(max_day):
    for project in projects:
        if project.assigned:
            continue
        for role in project.roles:
            if role.skill in skills:
                avail_conts = list(filter(lambda x: x.first_day_available <= day and x not in map(lambda y: y[0],project.assigned_roles) , skills[role.skill]))
                if not avail_conts:
                    #TODO: mentor
                    break
                avail_conts.sort(key = lambda x: x.no_skills)
                the_chosen_one = avail_conts[-1]
                project.assigned_roles.append((the_chosen_one, role.index, role.skill))
        if len(project.assigned_roles) == len(project.roles):
            for asignee, idx, oldskill in project.assigned_roles:
                asignee.first_day_available = day + project.no_days
                #todo: higher levels
                name, lvl = skill.split()
                for i in range(int(lvl)+1):
                    skill = name + " " + str(i)
                    if skill in role.skill:
                        skill_name,level = oldskill.split()
                        newskill = skill_name + " " + str(int(level)+1)
                        asignee.skills = list(filter(lambda x: x != oldskill, asignee.skills))
                        asignee.skills.append(newskill)

                        skills[oldskill].remove(asignee)
                        if newskill in skills:
                            skills[newskill].append(asignee)
                        else:
                            skills[newskill] = [asignee]

            project.assigned = True


        """ for contributor in filter(lambda x: x.first_day_available <= day, contributors):
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
 """


pass
