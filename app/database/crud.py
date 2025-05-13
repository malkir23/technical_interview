from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Type, Any, List


class CRUDBase:
    def __init__(self, session: Session, model: Type):
        self.session = session
        self.model = model

    def create(self, request_data) -> Any:
        try:
            instance = self.model(**request_data)
            self.session.add(instance)
            self.session.commit()
            self.session.refresh(instance)
            return instance
        except SQLAlchemyError as e:
            self.session.rollback()
            raise RuntimeError(f"Create failed: {e}")

    def get(self, **kwargs) -> Any:

        result = self.session.query(self.model).filter_by(**kwargs).first()
        if not result:
            raise LookupError(f"{self.model.__name__} not found with {kwargs}")
        return result

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Any]:
        return self.session.query(self.model).offset(skip).limit(limit).all()

    def update(self, get_filter: dict, update_date: dict) -> Any:
        try:
            instance = self.session.query(self.model).get(get_filter)
            if not instance:
                raise LookupError(
                    f"{self.model.__name__} with data {get_filter} not found"
                )
            for key, value in update_date.items():
                setattr(instance, key, value)
            self.session.commit()
            self.session.refresh(instance)
            return instance
        except SQLAlchemyError as e:
            self.session.rollback()
            raise RuntimeError(f"Update failed: {e}") from e

    def delete(self, object_id: Any) -> None:
        try:
            instance = self.session.query(self.model).get(object_id)
            if not instance:
                raise LookupError(
                    f"{self.model.__name__} with id {object_id} not found"
                )
            self.session.delete(instance)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise RuntimeError(f"Delete failed: {str(e)}") from e
