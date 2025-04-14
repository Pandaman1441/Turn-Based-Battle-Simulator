


def load_skills(skills):
    from Skills import skill_registry

    skill_obj = []
    for skill in skills:
        if skill in skill_registry:
            skill_class = skill_registry[skill]   # Gets the class
            skill_obj.append(skill_class())
        else:
            print("skill name wrong")
    return skill_obj