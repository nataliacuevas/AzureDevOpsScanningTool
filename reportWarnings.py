
class reportWarning:
    def __init__(self, name: str, id: int, category: str, severity: str, recommendation: str, project: str):
        self.name = name
        self.id = id
        self.category = category
        self.severity = severity
        self.recommendation = recommendation
        self.project = project

    def toDict(self):
        return {"name": self.name,
                "id": self.id,
                "category": self.category,
                "severity": self.severity,
                "recommendation": self.recommendation,
                "project": self.project
                }
    