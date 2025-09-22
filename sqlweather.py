from sqlalchemy import Column, Integer, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class WeatherSummary(Base):
    __tablename__ = 'weather_summary'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)

    avg_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)

    avg_wind = Column(Float)
    min_wind = Column(Float)
    max_wind = Column(Float)

    sum_precip = Column(Float)
    min_precip = Column(Float)
    max_precip = Column(Float)


#Function to set up the database and return a session
def create_session(db_name='weather.db'):
    engine = create_engine(f'sqlite:///{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
