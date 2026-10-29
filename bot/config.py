from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    bot_token: str = Field(..., alias="BOT_TOKEN")
    admin_id: int = Field(..., alias="ADMIN_ID")
    spreadsheet_id: str = Field(..., alias="SPREADSHEET_ID")
    google_credentials_path: str = Field(
        default="credentials/service_account.json",
        alias="GOOGLE_CREDENTIALS_PATH"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
