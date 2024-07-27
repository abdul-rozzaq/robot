from robot.models.street import Street
from .family_house import FamilyHouse
from .mahalla import Mahalla
from .member import FamilyCitizen, Member

class Family:
    def __init__(self, allmembers: str, created_at: str, created_by: str, district_id: str, help: str, house: FamilyHouse, house_id: str, id: str, is_deleted: bool, mahalla: Mahalla, mahalla_id: str, members: list, name: str, owner: FamilyCitizen, owner_id: str, owner_type: int, region_id: str, registration_type: int, statuses: str, street: Street, street_id: str, total: str, troubles: str, with_many_children: str):
        self.allmembers = allmembers
        self.created_at = created_at
        self.created_by = created_by
        self.district_id = district_id
        self.help = help
        self.house = house
        self.house_id = house_id
        self.id = id
        self.is_deleted = is_deleted
        self.mahalla = mahalla
        self.mahalla_id = mahalla_id
        self.members = members
        self.name = name
        self.owner = owner
        self.owner_id = owner_id
        self.owner_type = owner_type
        self.region_id = region_id
        self.registration_type = registration_type
        self.statuses = statuses
        self.street = street
        self.street_id = street_id
        self.total = total
        self.troubles = troubles
        self.with_many_children = with_many_children

    @classmethod
    def from_dict(cls, data: dict):
        house = FamilyHouse.from_dict(data.get('house'))
        mahalla = Mahalla.from_dict(data.get('mahalla'))
        owner = FamilyCitizen.from_dict(data.get('owner'))
        street = Street.from_dict(data.get('street'))
        members = []
        return cls(
            allmembers=data.get('allmembers'),
            created_at=data.get('created_at'),
            created_by=data.get('created_by'),
            district_id=data.get('district_id'),
            help=data.get('help'),
            house=house,
            house_id=data.get('house_id'),
            id=data.get('id'),
            is_deleted=data.get('is_deleted'),
            mahalla=mahalla,
            mahalla_id=data.get('mahalla_id'),
            members=members,
            name=data.get('name'),
            owner=owner,
            owner_id=data.get('owner_id'),
            owner_type=data.get('owner_type'),
            region_id=data.get('region_id'),
            registration_type=data.get('registration_type'),
            statuses=data.get('statuses'),
            street=street,
            street_id=data.get('street_id'),
            total=data.get('total'),
            troubles=data.get('troubles'),
            with_many_children=data.get('with_many_children')
        )

    def __repr__(self):
        return (f"Family(allmembers={self.allmembers}, created_at={self.created_at}, created_by={self.created_by}, district_id={self.district_id}, help={self.help}, house={self.house}, "
                f"house_id={self.house_id}, id={self.id}, is_deleted={self.is_deleted}, mahalla={self.mahalla}, mahalla_id={self.mahalla_id}, members={self.members}, name={self.name}, "
                f"owner={self.owner}, owner_id={self.owner_id}, owner_type={self.owner_type}, region_id={self.region_id}, registration_type={self.registration_type}, statuses={self.statuses}, "
                f"street={self.street}, street_id={self.street_id}, total={self.total}, troubles={self.troubles}, with_many_children={self.with_many_children})")