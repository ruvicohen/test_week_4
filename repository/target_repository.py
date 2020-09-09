from typing import List
from returns.maybe import Maybe, Nothing
from returns.result import Failure, Result, Success
from sqlalchemy.exc import SQLAlchemyError
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

def insert_target(target: Target) -> Result[Target, str]:
    with session_factory() as session:
        try:
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except SQLAlchemyError as e:
            return Failure(str(e))


def delete_target(u_id: int) -> Result[Target, str]:
    with session_factory() as session:
        try:
            maybe_target = find_target_by_id(u_id)
            if maybe_target is Nothing:
                return Failure(f"no target find by the id {u_id}")
            target_to_delete = maybe_target.unwrap()
            session.delete(target_to_delete)
            session.commit()
            return Success(target_to_delete)
        except SQLAlchemyError as e:
            return Failure(str(e))

def update_target(u_id: int, updated_target: Target) -> Result[Target, str]:
    with session_factory() as session:
        try:
            maybe_target = find_target_by_id(u_id)
            if maybe_target is Nothing:
                return Failure(f"no target find by the id {u_id}")
            target_to_update = session.merge(maybe_target.unwrap())
            target_to_update.first_name = updated_target.first_name
            target_to_update.last_name = updated_target.last_name
            target_to_update.email = updated_target.email
            target_to_update.phone = updated_target.phone
            target_to_update.phone = updated_target.phone
            target_to_update.phone = updated_target.phone
            session.commit()
            session.refresh(target_to_update)
            return Success(target_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))