from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, APIClient, DBClient, APIClientData


def db_model_to_api(client: DBClient) -> APIClient:
    return APIClient(
        client_id=client.client_id,
        message=client.message,
        time=client.time,
        additional_fields=APIClientData(
            name=client.name,
            phone=client.phone
        )
    )


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)


def add_client(client: APIClient):
    with Session(engine) as session:
        db_client = DBClient(
            client_id=client.client_id,
            message=client.message,
            time=client.time,
            name=client.additional_fields.name,
            phone=client.additional_fields.phone
        )
        session.add(db_client)
        session.commit()


def get_client(client_id: int) -> DBClient:
    with Session(engine) as session:
        return session.query(DBClient).filter(DBClient.id == client_id).first()