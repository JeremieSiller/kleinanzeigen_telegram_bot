from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_token: str
    kleinanzeigen_url: str | None
    wg_gesucht_url: str | None
    ids_file_name: str

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore[call-arg]
