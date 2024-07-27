class FamilyHouse:
    def __init__(self, id: str, name_uz: str, type: int):
        self.id = id
        self.name_uz = name_uz
        self.type = type

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            name_uz=data.get('name_uz'),
            type=data.get('type')
        )

    def __repr__(self):
        return f"House(id={self.id}, name_uz={self.name_uz}, type={self.type})"
