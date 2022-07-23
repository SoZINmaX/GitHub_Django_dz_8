import os.path
from django.core.management.base import BaseCommand
from movies.models import Person


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file", type=str, required=True)
       
    def handle(self, *args, **options):
        print("Data transfering ...")
        file = options.get("file")

        def progress_bar(progress ,total):
            percent = 100 * (progress / float(total))
            bar = '#' * int(percent) + '-' *(100 - int(percent))
            print(f"\r|{bar}| {percent:.2f}%", end="\r")
    
        def file_len(filename):
            with open(filename) as f:
                for i, _ in enumerate(f):
                    pass
            return i + 1
    
        if not os.path.exists(file):
            print("No such file.")
            
        progress_bar(0, file_len(file))
        
        with open(file, encoding="utf-8") as f:
            count = 0
            for line in f.readlines():
                if not line:
                    continue
                if not line.startswith("nm"):
                    continue
                data = line.split("\t")
                birth_date = data[2]
                if birth_date == "\\N":
                    birth_date = None
                else:
                    birth_date = f"{birth_date}-01-01"
                death_date = data[3]
                if death_date == "\\N":
                    death_date = None
                else:
                    death_date = f"{death_date}-01-01"
                person_data = {
                    'name': data[1],
                    'birth_date': birth_date,
                    'death_date': death_date,
                }
                movie, created = Person.objects.get_or_create(
                    imdb_id=data[0], defaults=person_data
                )

                if created:
                    Person.objects.filter(id=movie.id).update(**person_data)
                    count +=1
                progress_bar(int(count) + 1, file_len(file))
        print('')
        print('Data transfering completed')