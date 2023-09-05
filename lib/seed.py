#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Game).delete()
    session.commit()

    # Generate and add sample data to the "games" table
    print("Seeding games...")

    games = [
        Game(
            title=fake.unique.name(),  # Use unique names to avoid duplicates
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60)  # Random price between 0 and 60
        )
        for _ in range(50)  # Create 50 random game records
    ]

    session.bulk_save_objects(games)
    session.commit()

    print("Seeding completed.")