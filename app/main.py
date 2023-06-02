import logging
import json
import uvicorn
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi_versioning import VersionedFastAPI, version
import infrastructure.services
from topics.topic_factory import topic_factory
from v1.contracts import *
import traceback

import logging
log = logging.getLogger()
log.setLevel(logging.INFO)

app = FastAPI(
        title="Bot Assistance API",
        description="Landbot API to notify systems when a customer requests assistance from a bot",
        version="1.0",
        docs_url='/docs',
        openapi_url='/openapi.json',
        redoc_url=None
    )

@app.post("/assist", status_code = status.HTTP_200_OK)
@version(1)
async def assist(assistance: Assistance):
    logging.info(f"Assistance request: {json.dumps(assistance.dict())}")
    topic = await topic_factory.create(assistance.topic)
    await topic.send(assistance.description)
    return Response(status_code=status.HTTP_200_OK)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Custom Swagger UI"
    )

@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return app.openapi()

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    error_traceback = traceback.format_exc()
    return JSONResponse(content={"error": error_traceback}, status_code=500)

app = VersionedFastAPI(app,version_format='{major}', prefix_format='/v{major}')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)