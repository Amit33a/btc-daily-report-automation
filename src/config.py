import os
from dataclasses import dataclass
from dotenv import load_dotenv

@dataclass(frozen=True)
class Settings:
    #Database
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    #Email (SMTP)
    email_from: str
    email_to: str 
    email_app_password:str
    smtp_host: str
    smtp_port: int


def get_settings() -> Settings:
    load_dotenv()

    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD") 
    db_name = os.getenv("DB_NAME")

    email_from = os.getenv("EMAIL_FROM")
    email_to = os.getenv("EMAIL_TO")
    email_app_password = os.getenv("EMAIL_APP_PASSWORD")
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = os.getenv("SMTP_PORT")

    missing = [k for k, v in {
        "DB_HOST": db_host,
        "DB_PORT": db_port,
        "DB_USER": db_user,
        "DB_PASSWORD": db_password,
        "DB_NAME": db_name,
        "EMAIL_FROM": email_from,
        "EMAIL_TO": email_to,
        "EMAIL_APP_PASSWORD": email_app_password,
        "SMTP_HOST": smtp_host,
        "SMTP_PORT": smtp_port,
    }.items() if not v]

    if missing:
        raise RuntimeError(f"Missing env var(s): {', '.join(missing)}. Check your .env file.")
    
    try: 
        db_port_int = int(db_port)
    except ValueError as e:
        raise RuntimeError(f"DB_PORT must be a number, got: {db_port}") from e

    try:
        smtp_host_int = int(smtp_port)
    except ValueError as e:
        raise RuntimeError(f"SMTP_PORT must be a number, got: {smtp_port}") from e

    
    return Settings(
        db_host=db_host.strip(),
        db_port=db_port_int,    
        db_user=db_user.strip(),
        db_password=db_password.strip(),
        db_name=db_name.strip(),
        email_from=email_from.strip(),
        email_to=email_to.strip(),
        email_app_password=email_app_password.strip(),
        smtp_host=smtp_host.strip(),
        smtp_port=smtp_host_int,
    )



     
    
 




