from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # psycopg v3 driver:
    DATABASE_URL: str = "postgresql+psycopg://postgres:postgres@localhost:5432/appdb"
    DOCKER_IMAGE: str = "your-dockerhub-username/your-app"

    class Config:
        env_file = ".env"

settings = Settings()
