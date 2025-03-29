import yaml


class yamlHandler:
    def __init__(self):
        self.configFile = "reportConfig.yaml"

        with open(self.configFile, 'r') as file:
            self.data : dict = yaml.safe_load(file)

    def MaxNumberProjectAdmins(self):
        return self.data["MaxNumberProjectAdmins"]