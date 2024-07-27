from typing import List, Dict

from .document import Document


class UserInfo:
    def __init__(self, sex: int, pinpps: List[str], engname: str, namecyr: str, namelat: str, documents: List[Document], 
                 birth_date: str, birthplace: str, engsurname: str, livestatus: int, surnamecyr: str, surnamelat: str, 
                 citizenship: str, nationality: str, patronymcyr: str, patronymlat: str, birthcountry: str, 
                 citizenshipid: int, current_pinpp: str, nationalityid: int, birthcountryid: int, 
                 transaction_id: int, current_document: str):
        self.sex = sex
        self.pinpps = pinpps
        self.engname = engname
        self.namecyr = namecyr
        self.namelat = namelat
        self.documents = documents
        self.birth_date = birth_date
        self.birthplace = birthplace
        self.engsurname = engsurname
        self.livestatus = livestatus
        self.surnamecyr = surnamecyr
        self.surnamelat = surnamelat
        self.citizenship = citizenship
        self.nationality = nationality
        self.patronymcyr = patronymcyr
        self.patronymlat = patronymlat
        self.birthcountry = birthcountry
        self.citizenshipid = citizenshipid
        self.current_pinpp = current_pinpp
        self.nationalityid = nationalityid
        self.birthcountryid = birthcountryid
        self.transaction_id = transaction_id
        self.current_document = current_document

    @classmethod
    def from_dict(cls, data: Dict):
        documents = [Document.from_dict(doc) for doc in data.get('documents', [])]
        return cls(
            sex=data.get('sex'),
            pinpps=data.get('pinpps', []),
            engname=data.get('engname'),
            namecyr=data.get('namecyr'),
            namelat=data.get('namelat'),
            documents=documents,
            birth_date=data.get('birth_date'),
            birthplace=data.get('birthplace'),
            engsurname=data.get('engsurname'),
            livestatus=data.get('livestatus'),
            surnamecyr=data.get('surnamecyr'),
            surnamelat=data.get('surnamelat'),
            citizenship=data.get('citizenship'),
            nationality=data.get('nationality'),
            patronymcyr=data.get('patronymcyr'),
            patronymlat=data.get('patronymlat'),
            birthcountry=data.get('birthcountry'),
            citizenshipid=data.get('citizenshipid'),
            current_pinpp=data.get('current_pinpp'),
            nationalityid=data.get('nationalityid'),
            birthcountryid=data.get('birthcountryid'),
            transaction_id=data.get('transaction_id'),
            current_document=data.get('current_document')
        )

    def __repr__(self):
        return (f"UserInfo(sex={self.sex}, pinpps={self.pinpps}, engname={self.engname}, namecyr={self.namecyr}, "
                f"namelat={self.namelat}, documents={self.documents}, birth_date={self.birth_date}, "
                f"birthplace={self.birthplace}, engsurname={self.engsurname}, livestatus={self.livestatus}, "
                f"surnamecyr={self.surnamecyr}, surnamelat={self.surnamelat}, citizenship={self.citizenship}, "
                f"nationality={self.nationality}, patronymcyr={self.patronymcyr}, patronymlat={self.patronymlat}, "
                f"birthcountry={self.birthcountry}, citizenshipid={self.citizenshipid}, current_pinpp={self.current_pinpp}, "
                f"nationalityid={self.nationalityid}, birthcountryid={self.birthcountryid}, transaction_id={self.transaction_id}, "
                f"current_document={self.current_document})")

    
    @property
    def full_name(self) -> str:
        return "{} {} {}".format(self.surnamelat, self.namelat, self.patronymlat)  
   