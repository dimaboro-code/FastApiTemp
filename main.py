import uvicorn
from fastapi import FastAPI, BackgroundTasks
from models import APIClient
from database import add_client, get_client, db_model_to_api

app = FastAPI()


async def add_new_user(client: APIClient):
    add_client(client)
    return True

@app.post("/message")
async def post_message(client: APIClient, background_tasks: BackgroundTasks):
    background_tasks.add_task(add_new_user, client)
    return {"message": "Notification sent in the background"}


@app.get("/message/{message_id}")
async def get_message(message_id: int):
    client = get_client(message_id)
    if client:
        answer = db_model_to_api(client)
    else:
        answer = {"message_id": "not found"}
    return answer


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
