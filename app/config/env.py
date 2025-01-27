from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "api-py"
    host: str
    port: int
    hot_reload_enabled: bool
    postgres_url: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
