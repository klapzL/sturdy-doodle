from fastapi import FastAPI
from fastapi_pagination import add_pagination

from debug_toolbar.middleware import DebugToolbarMiddleware

from src.eventic.api.router import router
from src.config.settings import settings


app = FastAPI(
    docs_url='/api/v1/docs',
    debug=settings.DEBUG,
    swagger_ui_parameters={
        'docExpansion': 'none',
        'tryItOutEnabled': True,
        'syntaxHighlight.theme': 'obsidian',
    },
)

if settings.DEBUG:
    app.add_middleware(
        DebugToolbarMiddleware,
        panels=['debug_toolbar.panels.sqlalchemy.SQLAlchemyPanel'],
    )

add_pagination(app)
app.include_router(router)
