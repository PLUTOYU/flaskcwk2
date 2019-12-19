from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=64)),
    Column('email', String(length=64)),
    Column('password_hash', String(length=64)),
    Column('location', String(length=64)),
    Column('gender', Integer),
    Column('about_me', String(length=150)),
    Column('created_on', DateTime, default=ColumnDefault(datetime.datetime(2019, 12, 18, 5, 34, 52, 40807))),
    Column('last_seen', DateTime, default=ColumnDefault(datetime.datetime(2019, 12, 18, 5, 34, 52, 40807))),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['location'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['location'].drop()
