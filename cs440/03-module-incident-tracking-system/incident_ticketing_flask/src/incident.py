
import uuid
from datetime import datetime

class Incident:
    def __init__(self, title, reporter):
        self.id = str(uuid.uuid4())
        self.title = title
        self.reporter = reporter
        self.status = "New"
        self.assignee = None
        self.created_at = datetime.now()
        self.resolved_at = None

    def assign(self, user):
        self.assignee = user
        self.status = "In Progress"

    def resolve(self):
        self.status = "Resolved"
        self.resolved_at = datetime.now()

    def __str__(self):
        return f"[{self.status}] {self.title} (ID: {self.id})"
