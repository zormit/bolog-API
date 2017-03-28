from bolog import create_app
# from shared.env import require_env

import pytest


class BaseFixtures:
    @pytest.fixture(scope='module')
    def app(self, request):
        app = create_app()
        ctx = app.app_context()
        ctx.push()
        request.addfinalizer(ctx.pop)
        return app

    @pytest.fixture(scope='module')
    def test_client(self, request, app):
        client = app.test_client()
        client.__enter__()
        request.addfinalizer(
            lambda: client.__exit__(None, None, None))
        return client
