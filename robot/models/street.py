class Street:
    def __init__(self, id: str, street_type: int, name_uz: str):
        self.id = id
        self.street_type = street_type
        self.name_uz = name_uz

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            street_type=data.get('type'),
            name_uz=data.get('name_uz')
        )

    def __repr__(self):
        return f"Street(id={self.id}, street_type={self.street_type}, name_uz={self.name_uz})"
