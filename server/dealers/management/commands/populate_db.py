from django.core.management.base import BaseCommand
from dealers.models import Dealer
from reviews.models import Review
from cars.models import CarMake, CarModel

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        Dealer.objects.all().delete()
        Review.objects.all().delete()
        CarModel.objects.all().delete()
        CarMake.objects.all().delete()

        dealers = [
            Dealer(full_name='ABC Motors', city='Kansas City', address='123 Main St, Kansas City, KS', zip='64108', state='Kansas', lat=39.0997, long=-94.5786),
            Dealer(full_name='XYZ Auto Sales', city='Topeka', address='456 Oak Ave, Topeka, KS', zip='66603', state='Kansas', lat=39.0558, long=-95.6890),
            Dealer(full_name='Premium Cars', city='Wichita', address='789 Elm St, Wichita, KS', zip='67202', state='Kansas', lat=37.6872, long=-97.3301),
        ]
        Dealer.objects.bulk_create(dealers)

        car_makes = [
            CarMake(name='Toyota'),
            CarMake(name='Honda'),
            CarMake(name='Ford'),
            CarMake(name='Chevrolet'),
            CarMake(name='Nissan'),
        ]
        CarMake.objects.bulk_create(car_makes)

        makes = {make.name: make for make in CarMake.objects.all()}
        CarModel.objects.bulk_create([
            CarModel(make=makes['Toyota'], name='Camry'),
            CarModel(make=makes['Toyota'], name='Corolla'),
            CarModel(make=makes['Honda'], name='Civic'),
            CarModel(make=makes['Honda'], name='Accord'),
            CarModel(make=makes['Ford'], name='F-150'),
            CarModel(make=makes['Ford'], name='Mustang'),
            CarModel(make=makes['Chevrolet'], name='Silverado'),
            CarModel(make=makes['Chevrolet'], name='Malibu'),
            CarModel(make=makes['Nissan'], name='Altima'),
            CarModel(make=makes['Nissan'], name='Sentra'),
        ])

        dealers = {dealer.full_name: dealer for dealer in Dealer.objects.all()}

        Review.objects.bulk_create([
            Review(name='John Doe', dealership=dealers['ABC Motors'], review='Great service and friendly staff!', purchase=True, purchase_date='2024-01-15', car_make='Toyota', car_model='Camry', car_year=2022, sentiment='positive'),
            Review(name='Jane Smith', dealership=dealers['ABC Motors'], review='Excellent customer service', purchase=False, sentiment='positive'),
            Review(name='Bob Johnson', dealership=dealers['XYZ Auto Sales'], review='Fantastic services', purchase=True, purchase_date='2024-02-20', car_make='Honda', car_model='Civic', car_year=2023, sentiment='positive'),
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data'))