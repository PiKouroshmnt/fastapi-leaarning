import os

import pytest
from starlette.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import Settings, get_settings
from app.main import create_application
from app.db import Base

engine = create_async_engine(os.environ.get("DATABASE_TEST_URL"),echo=True)
local_test_session = sessionmaker(
    bind=engine, expire_on_commit=False
)

def get_settings_override():
    return Settings(
        testing=1,
        database_url=os.environ.get("DATABASE_TEST_URL"),
    )


@pytest.fixture(scope="module")
def test_app():
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
async def test_app_with_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override

    with TestClient(app) as test_client:
        yield test_client
