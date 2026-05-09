from fastapi import FastAPI


def init_middlewares(app: FastAPI) -> None:
    pass


def init_routers(app: FastAPI) -> None:
    pass


def server() -> FastAPI:
    app_ = FastAPI(
        title="CommerceFlow",
    )
    init_routers(app_)
    init_middlewares(app_)
    return app_
