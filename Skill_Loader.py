


def load_skills(skills):
    from Skills import skill_registry

    skill_objects = []
    for skill in skills:
        if skill in skill_registry:
            skill_obj = skill_registry[skill]   # Gets a object
            skill_objects.append(skill_obj())
        else:
            print("skill name wrong")
    return skill_objects