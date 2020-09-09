from typing import Dict, List

from returns.maybe import Nothing, Maybe, Some
from toolz import pipe, curry

from model import Target


def create_target(target_dict: Dict[str, str]) -> Target:
    return Target(
        priority=target_dict["priority"],
        country_id=target_dict["country_id"],
        city_id=target_dict["city_id"],
        location_id=target_dict["location_id"],
        type_id=target_dict["type_id"],
        industry_id=target_dict["industry_id"]
    )

def convert_to_target(target_json: Dict[str, str]) -> Maybe[Target]:
    return pipe(
        target_json,
        has_all_keys(['priority','country_id', 'city_id', 'location_id', 'type_id', 'industry_id']),
        lambda is_valid: Nothing if not is_valid else Some(create_target(target_json))
    )
@curry
def has_all_keys(keys: List[str], d: Dict[str, str]) -> bool:
    return all(k in d for k in keys)