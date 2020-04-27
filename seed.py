"""Seed file for blogly"""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add users
blues = Pet(name="Blues", species="Dog", photo_url="https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12212924/Samoyed-slide-5.jpg", age="3", notes="A good boy", available=True)
jerry = Pet(name="Jerry", species="Cat", photo_url="https://upload.wikimedia.org/wikipedia/commons/2/25/Siam_lilacpoint.jpg", age="5", notes="michevious", available=True)
katie = Pet(name="Katie", species="Dog", photo_url="https://vetstreet.brightspotcdn.com/dims4/default/1180a4f/2147483647/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F55%2Ff22c50a7f711e0a0d50050568d634f%2Ffile%2FPomeranian-5-645mk062811.jpg", age="1", notes="excited", available=True)
travis = Pet(name="travis", species="Cat", photo_url="https://vetstreet.brightspotcdn.com/dims4/default/241bcba/2147483647/crop/622x366%2B0%2B99/resize/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F27%2F53%2F640393fc4768b2bb0c664ac76ebb%2Fmaine-coon-ap-yurcwf.jpg", age="6", notes="shy", available=True)
ellie = Pet(name="ellie", species="Dog", photo_url="https://www.insidedogsworld.com/wp-content/uploads/2016/12/husky10.jpg", age="4", notes="super sweet", available=True)
sarah = Pet(name="sarah", species="Cat", photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Blackcat-Lilith.jpg/225px-Blackcat-Lilith.jpg", age="3", notes="Small but fierce", available=False)

db.session.add(blues)
db.session.add(jerry)
db.session.add(katie)
db.session.add(travis)
db.session.add(ellie)
db.session.add(sarah)


db.session.commit()