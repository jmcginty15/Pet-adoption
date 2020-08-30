from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

greg = Pet(name='Greg', species='dog', photo_url='https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg', age=2, notes='The goodest boi')
steven = Pet(name='Steven', species='horse', photo_url='https://cdn.sanity.io/images/0vv8moc6/dvm360/775ce164e49c8c454937d002306a18a4f8663dd4-450x350.jpg', age=6, notes='Just horsing around')
goldie = Pet(name='Goldie', species='fish', age=1, notes='Fishy boi')
billiam = Pet(name='Billiam', species='hedgehog', photo_url='https://cf.ltkcdn.net/small-pets/images/orig/262186-1600x1030-pet-hedgehog-costs.jpg', age=1, notes='Spikey boi')
wilford = Pet(name='Wilford', species='dog', age=5, notes='Invisible boi')
reggie = Pet(name='Reggie', species='cat', photo_url='https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/cat_relaxing_on_patio_other/1800x1200_cat_relaxing_on_patio_other.jpg', age=10, notes='Lazy boi', available=True)

db.session.add(greg)
db.session.add(steven)
db.session.add(goldie)
db.session.add(billiam)
db.session.add(wilford)
db.session.add(reggie)

db.session.commit()