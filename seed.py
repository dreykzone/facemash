from app.app import create_app
from app.seed import seed_database


app = create_app()


if __name__ == "__main__":
    with app.app_context():
        created = seed_database()
        print("Seed concluído." if created else "O banco já possui dados; nada foi alterado.")