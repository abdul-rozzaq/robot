class Mahalla:
    def __init__(self, id: str, stir: str, soato: str, name_en: str, name_ru: str, name_uz: str, region_id: str, district_id: str, region_json: dict, village_code: str, district_json: dict):
        self.id = id
        self.stir = stir
        self.soato = soato
        self.name_en = name_en
        self.name_ru = name_ru
        self.name_uz = name_uz
        self.region_id = region_id
        self.district_id = district_id
        self.region_json = region_json
        self.village_code = village_code
        self.district_json = district_json

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            stir=data.get('stir'),
            soato=data.get('soato'),
            name_en=data.get('name_en'),
            name_ru=data.get('name_ru'),
            name_uz=data.get('name_uz'),
            region_id=data.get('region_id'),
            district_id=data.get('district_id'),
            region_json=data.get('region_json'),
            village_code=data.get('village_code'),
            district_json=data.get('district_json')
        )

    def __repr__(self):
        return (f"Mahalla(id={self.id}, stir={self.stir}, soato={self.soato}, name_en={self.name_en}, name_ru={self.name_ru}, "
                f"name_uz={self.name_uz}, region_id={self.region_id}, district_id={self.district_id}, region_json={self.region_json}, "
                f"village_code={self.village_code}, district_json={self.district_json})")
