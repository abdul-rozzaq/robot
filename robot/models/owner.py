class Owner:
    def __init__(self, photo_id: str, full_name: str, birth_date: str, phone_number: str, current_document: str, registration_type: int):
        self.photo_id = photo_id
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.current_document = current_document
        self.registration_type = registration_type

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            photo_id=data.get('photo_id'),
            full_name=data.get('full_name'),
            birth_date=data.get('birth_date'),
            phone_number=data.get('phone_number'),
            current_document=data.get('current_document'),
            registration_type=data.get('registration_type')
        )

    def __repr__(self):
        return (f"Owner(photo_id={self.photo_id}, full_name={self.full_name}, birth_date={self.birth_date}, "
                f"phone_number={self.phone_number}, current_document={self.current_document}, registration_type={self.registration_type})")
