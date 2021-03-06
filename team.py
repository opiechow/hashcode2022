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
        self.start_day = 0

class ProjectRole:
    def __init__(self, skill, index):
        self.skill = skill
        self.index = index

contributors = []
projects = []
skills = {}

base_name = "c_collaboration"
in_file = f"team_inputs/{base_name}.in.txt"
out_file = f"team_outputs/{base_name}.out.txt"

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
            name, lvl = skill.split()
            for i in range(int(lvl)+1):
                skill = name + " " + str(i)
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
                skill_name,level = oldskill.split()
                newskill = skill_name + " " + str(int(level)+1)
                asignee.skills = list(filter(lambda x: x != oldskill, asignee.skills))
                asignee.skills.append(newskill)
                #skills[oldskill].remove(asignee)
                if newskill in skills:
                    skills[newskill].append(asignee)
                else:
                    skills[newskill] = [asignee]

            project.assigned = True
            project.start_day = day
        else:
            project.assigned_roles = []

done_projects = list(filter(lambda x: x.assigned, projects))
done_projects.sort(key = lambda x: x.start_day)

with open(out_file, "w") as f:
    f.write(str(len(done_projects)))
    f.write("\n")
    for project in done_projects:
        f.write(project.name)
        f.write("\n")
        project.assigned_roles.sort(key = lambda x: x[1])
        for asignee in map(lambda x: x[0], project.assigned_roles):
            f.write(asignee.name)
            f.write(" ")
        f.write("\n")
