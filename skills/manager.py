from skills.system import SystemSkills


class SkillManager:

    def __init__(self):

        self.system = SystemSkills()

    def execute(self, command):

        command = command.lower()

        if "open notepad" in command:
            return self.system.open_notepad()

        elif "time" in command:
            return self.system.get_time()

        elif "date" in command:
            return self.system.get_date()

        return None