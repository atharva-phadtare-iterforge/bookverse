from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env"
    )

settings = Settings()

print(settings.database_url)
