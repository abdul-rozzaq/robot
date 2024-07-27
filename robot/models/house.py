from .owner import Owner
from .region import Region
from .district import District
from .mahalla import Mahalla
from .street import Street

class House:
    def __init__(self, total: str, id: str, name: str, street_id: str, mahalla_id: str, district_id: str, region_id: str, created_at: str, created_by: str, is_deleted: bool, house_number: str, type: int, last_check_date: str, owner_id: str, owner_type: int, registration_type: int, cadastre: str, owner_pinpp: str, owner: Owner, region: Region, district: District, mahalla: Mahalla, street: Street, clinic_number: str, house_phone: str, lifestyle: str, phone: str, apartment_id: str, apartment: str, hospital_id: str, patronaj_employer_id: str, registered_count: str, is_member_exists: bool, is_animal_exists: bool, status: str):
        self.total = total
        self.id = id
        self.name = name
        self.street_id = street_id
        self.mahalla_id = mahalla_id
        self.district_id = district_id
        self.region_id = region_id
        self.created_at = created_at
        self.created_by = created_by
        self.is_deleted = is_deleted
        self.house_number = house_number
        self.type = type
        self.last_check_date = last_check_date
        self.owner_id = owner_id
        self.owner_type = owner_type
        self.registration_type = registration_type
        self.cadastre = cadastre
        self.owner_pinpp = owner_pinpp
        self.owner = owner
        self.region = region
        self.district = district
        self.mahalla = mahalla
        self.street = street
        self.clinic_number = clinic_number
        self.house_phone = house_phone
        self.lifestyle = lifestyle
        self.phone = phone
        self.apartment_id = apartment_id
        self.apartment = apartment
        self.hospital_id = hospital_id
        self.patronaj_employer_id = patronaj_employer_id
        self.registered_count = registered_count
        self.is_member_exists = is_member_exists
        self.is_animal_exists = is_animal_exists
        self.status = status

    @classmethod
    def from_dict(cls, data: dict):
        owner = Owner.from_dict(data.get('owner'))
        region = Region.from_dict(data.get('region'))
        district = District.from_dict(data.get('district'))
        mahalla = Mahalla.from_dict(data.get('mahalla'))
        street = Street.from_dict(data.get('street'))
        return cls(
            total=data.get('total'),
            id=data.get('id'),
            name=data.get('name'),
            street_id=data.get('street_id'),
            mahalla_id=data.get('mahalla_id'),
            district_id=data.get('district_id'),
            region_id=data.get('region_id'),
            created_at=data.get('created_at'),
            created_by=data.get('created_by'),
            is_deleted=data.get('is_deleted'),
            house_number=data.get('house_number'),
            type=data.get('type'),
            last_check_date=data.get('last_check_date'),
            owner_id=data.get('owner_id'),
            owner_type=data.get('owner_type'),
            registration_type=data.get('registration_type'),
            cadastre=data.get('cadastre'),
            owner_pinpp=data.get('owner_pinpp'),
            owner=owner,
            region=region,
            district=district,
            mahalla=mahalla,
            street=street,
            clinic_number=data.get('clinic_number'),
            house_phone=data.get('house_phone'),
            lifestyle=data.get('lifestyle'),
            phone=data.get('phone'),
            apartment_id=data.get('apartment_id'),
            apartment=data.get('apartment'),
            hospital_id=data.get('hospital_id'),
            patronaj_employer_id=data.get('patronaj_employer_id'),
            registered_count=data.get('registered_count'),
            is_member_exists=data.get('is_member_exists'),
            is_animal_exists=data.get('is_animal_exists'),
            status=data.get('status')
        )

    def __repr__(self):
        return (f"User(total={self.total}, id={self.id}, name={self.name}, street_id={self.street_id}, mahalla_id={self.mahalla_id}, "
                f"district_id={self.district_id}, region_id={self.region_id}, created_at={self.created_at}, created_by={self.created_by}, "
                f"is_deleted={self.is_deleted}, house_number={self.house_number}, type={self.type}, last_check_date={self.last_check_date}, "
                f"owner_id={self.owner_id}, owner_type={self.owner_type}, registration_type={self.registration_type}, cadastre={self.cadastre}, "
                f"owner_pinpp={self.owner_pinpp}, owner={self.owner}, region={self.region}, district={self.district}, mahalla={self.mahalla}, "
                f"street={self.street}, clinic_number={self.clinic_number}, house_phone={self.house_phone}, lifestyle={self.lifestyle}, phone={self.phone}, "
                f"apartment_id={self.apartment_id}, apartment={self.apartment}, hospital_id={self.hospital_id}, patronaj_employer_id={self.patronaj_employer_id}, "
                f"registered_count={self.registered_count}, is_member_exists={self.is_member_exists}, is_animal_exists={self.is_animal_exists}, status={self.status})")
