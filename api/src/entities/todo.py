from datetime import datetime
from jsonschema import validate

class Todo:
    def __init__(self, user_id: str, title: str = '', created_date: datetime = None, 
                 last_update_date: datetime = None, is_complete: bool = False, 
                 important: bool = False):
        self.user_id = user_id
        self.title = title
        self.created_date = datetime.fromisoformat(created_date) if created_date else datetime.now()
        self.last_update_date = datetime.fromisoformat(last_update_date) if last_update_date else datetime.now()
        self.is_complete = is_complete
        self.important = important

    def to_dict(self):
        # _id no se incluye ya que es manejado por MongoDB
        return {
            "user_id": self.user_id,
            "title": self.title,
            "created_date": self.created_date.isoformat(),
            "last_update_date": self.last_update_date.isoformat(),
            "is_complete": self.is_complete,
            "important": self.important
        }

    def validate(self):
        schema = {
            "type": "object",
            "properties": {
                "user_id": {"type": "string"},  
                "title": {"type": "string"},
                "created_date": {"type": "string", "format": "date-time"},
                "last_update_date": {"type": "string", "format": "date-time"},
                "is_complete": {"type": "boolean"},
                "important": {"type": "boolean"}
            },
            "required": ["user_id", "title", "created_date", "last_update_date", "is_complete", "important"]
        }

        # Validar la instancia con el esquema
        validate(instance=self.to_dict(), schema=schema)
