

class FamilyCitizen:
    def __init__(self, birth_date: str, full_name: str, current_document: str = None, phone_number: str = None, photo_id: str = None, registration_type: int = None):
        self.birth_date = birth_date
        self.full_name = full_name
        self.current_document = current_document
        self.phone_number = phone_number
        self.photo_id = photo_id
        self.registration_type = registration_type

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            birth_date=data.get('birth_date', '1974-09-02'),
            full_name=data.get('full_name'),
            current_document=data.get('current_document'),
            phone_number=data.get('phone_number'),
            photo_id=data.get('photo_id'),
            registration_type=data.get('registration_type')
        )

    def __repr__(self):
        return (f"Citizen(birth_date={self.birth_date}, full_name={self.full_name}, current_document={self.current_document}, "
                f"phone_number={self.phone_number}, photo_id={self.photo_id}, registration_type={self.registration_type})")


class Member:
    def __init__(self, citizen: FamilyCitizen, citizen_id: str, id: str, phone_number: str = None, type: int = None):
        self.citizen = citizen
        self.citizen_id = citizen_id
        self.id = id
        self.phone_number = phone_number
        self.type = type

    @classmethod
    def from_dict(cls, data: dict):
        citizen = FamilyCitizen.from_dict(data.get('citizen'))
        
        return cls(
            citizen=citizen,
            citizen_id=data.get('citizen_id'),
            id=data.get('id'),
            phone_number=data.get('phone_number'),
            type=data.get('type')
        )

    def __repr__(self):
        return (f"Member(citizen={self.citizen}, citizen_id={self.citizen_id}, id={self.id}, phone_number={self.phone_number}, type={self.type})")



