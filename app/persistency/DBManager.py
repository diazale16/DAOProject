from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class DBManager:
    _instance = None

    def __new__(cls, db_name='dev.db', db_folder='databases'):
        if cls._instance is None:
            cls._instance = super(DBManager, cls).__new__(cls)
            cls._instance.initialize(db_name, db_folder)
            cls._instance.create_tables()
        return cls._instance

    def initialize(self, db_name, db_folder):
        db_folder = Path(__file__).resolve().parent.parent.parent / db_folder
        db_folder.mkdir(parents=True, exist_ok=True)
        db_path = f'sqlite:///{db_folder / db_name}'
        self.engine = create_engine(db_path)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        import app.entities
        Base.metadata.create_all(self.engine)
    
    def get_session(self):
        return self.Session()

    # def create_tables(self):
    #     Base.metadata.create_all(self.engine)

    def register(self, entity):
        session = self.get_session()
        try:
            session.add(entity)
            session.commit()
            session.refresh(entity)
            print(f"Entidad guardada: {entity}")
        except Exception as e:
            session.rollback()
            print(f"Error al guardar la entidad: {e}")
        finally:
            session.close()

    def delete(self, entity):
        session = self.get_session()
        try:
            session.delete(entity)
            session.commit()
            # session.refresh(entity)
            print(f"Entidad eliminada: {entity}")
        except Exception as e:
            session.rollback()
            print(f"Error al eliminar la entidad: {e}")
        finally:
            session.close()
    
    def update(self, entity):
        session = self.get_session()
        try:
            # Asegurarse de que la entidad está en la sesión con merge
            merged_entity = session.merge(entity)
            session.commit()
            print(f"Entidad actualizada: {merged_entity}")
        except Exception as e:
            session.rollback()
            print(f"Error al actualizar la entidad: {e}")
        finally:
            session.close()

    def get_all(self, entity_class):
        session = self.get_session()
        try:
            return session.query(entity_class).all()
        finally:
                session.close()

    def get_by_id(self, entity_class, entity_id):
        session = self.get_session()
        try:
            return session.query(entity_class).get(entity_id)
        finally:
            session.close()
