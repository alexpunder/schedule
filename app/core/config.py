from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = 'APP_TITLE'
    description: str = 'DESCRIPTION'
    database_url: str = 'DATABASE_URL'
    secret: str = 'SECRET'

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
