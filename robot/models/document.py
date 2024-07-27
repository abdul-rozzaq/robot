from typing import List, Dict



class Document:
    def __init__(self, doc_type: str, status: int, date_end: str, document: str, date_begin: str, doc_give_place: str, doc_give_place_id: int):
        self.type = doc_type
        self.status = status
        self.date_end = date_end
        self.document = document
        self.date_begin = date_begin
        self.doc_give_place = doc_give_place
        self.doc_give_place_id = doc_give_place_id

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            doc_type=data.get('type'),
            status=data.get('status'),
            date_end=data.get('dateend'),
            document=data.get('document'),
            date_begin=data.get('datebegin'),
            doc_give_place=data.get('docgiveplace'),
            doc_give_place_id=data.get('docgiveplaceid')
        )

    def __repr__(self):
        return (f"Document(type={self.type}, status={self.status}, date_end={self.date_end}, "
                f"document={self.document}, date_begin={self.date_begin}, "
                f"doc_give_place={self.doc_give_place}, doc_give_place_id={self.doc_give_place_id})")

