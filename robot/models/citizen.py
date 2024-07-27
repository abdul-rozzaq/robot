from typing import List, Dict

from .user_info import UserInfo


class Citizen:
    def __init__(self, id: str, pinpp: str, user_info: UserInfo, region_id: str, district_id: str, mahalla_id: str, photo_id: str):
        self.id = id
        self.pinpp = pinpp
        self.user_info = user_info
        self.region_id = region_id
        self.district_id = district_id
        self.mahalla_id = mahalla_id
        self.photo_id = photo_id

    @classmethod
    def from_dict(cls, data: Dict):
        user_info = UserInfo.from_dict(data.get('user_info'))
        return cls(
            id=data.get('id'),
            pinpp=data.get('pinpp'),
            user_info=user_info,
            region_id=data.get('region_id'),
            district_id=data.get('district_id'),
            mahalla_id=data.get('mahalla_id'),
            photo_id=data.get('photo_id')
        )

    def __repr__(self):
        return (f"User(id={self.id}, pinpp={self.pinpp}, user_info={self.user_info}, region_id={self.region_id}, "
                f"district_id={self.district_id}, mahalla_id={self.mahalla_id}, photo_id={self.photo_id})")
