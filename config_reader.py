from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
import pathlib

class DotEnv(BaseSettings):
    bot_token: SecretStr
    maintenance_mode: bool
    admin_id: list
    support_id: str

    sqlalchemy_url: SecretStr

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=f"{pathlib.Path(__file__).resolve().parent}/.env",
        env_file_encoding="utf-8"
    )
config = DotEnv()
