from typing import List
from returns.maybe import Maybe
from sqlalchemy.orm import joinedload
from config.base import session_factory
from model.target import Target


def find_targets() -> List[Target]:
    with session_factory() as session:
        targets = (session.
                 query(Target).
                 options(joinedload(Target.country)).
                 options(joinedload(Target.city)).
                 options(joinedload(Target.location)).
                 options(joinedload(Target.target_type)).
                 all())
        return targets


def find_target_by_id(t_id: int) -> Maybe[Target]:
    with session_factory() as session:
        return Maybe.from_optional(
            session.query(Target).
            options(joinedload(Target.country)).
            options(joinedload(Target.city)).
            options(joinedload(Target.location)).
            options(joinedload(Target.target_type)).
            filter(Target.target_id == t_id)
            .first()
        )

