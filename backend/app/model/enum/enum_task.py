from enum import Enum

class PriorityEnum(str, Enum):
    low = "Low"
    medium = "Medium"
    high = "High"

class TaskTypeEnum(str, Enum):
    normal = "Normal"
    recurring = "Recurring"
    daily_quest = "Daily Quest"
    project = "Project"
