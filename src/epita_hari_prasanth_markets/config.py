
import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


@dataclass(frozen=True)
class Settings:

    app_env: str = os.getenv(
        "APP_ENV", "development"
    )

    api_key: str = os.getenv(
        "FINNHUB_API_KEY", ""
    )

    debug: bool = os.getenv(
        "DEBUG", "False"
    ).lower() in ("true", "1", "yes")

    def validate(self):

        if not self.api_key or self.api_key.startswith("your_"):

            raise ValueError(
                "Finnhub API key is missing. "
                "Check your .env file."
            )


config = Settings()
