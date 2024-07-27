class Region:
    def __init__(self, id: str, names: dict, soato: str, name_ru: str, name_uz: str):
        self.id = id
        self.names = names
        self.soato = soato
        self.name_ru = name_ru
        self.name_uz = name_uz

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            names=data.get('names'),
            soato=data.get('soato'),
            name_ru=data.get('name_ru'),
            name_uz=data.get('name_uz')
        )

    def __repr__(self):
        return (f"Region(id={self.id}, names={self.names}, soato={self.soato}, name_ru={self.name_ru}, name_uz={self.name_uz})")
