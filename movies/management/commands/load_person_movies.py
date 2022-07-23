import json
import os.path
from django.core.management.base import BaseCommand
from movies.models import Person, Movie, PersonMovie


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
                if not line.startswith("tt"):
                    continue
                data = line.split("\t")
                person = Person.objects.filter(imdb_id=data[2]).first()
                if not person:
                    continue
                movie = Movie.objects.filter(imdb_id=data[0]).first()
                if not movie:
                    continue
                job = data[4]
                if job == "\\N":
                    job = None
                characters = data[5]
                if "\\N" in characters:
                    characters = None
                else:
                    characters = json.loads(characters)
                pm_data = {
                    "order": int(data[1]),
                    "category": data[3],
                    "job": job,
                    "characters": characters,
                }
                pm, created = PersonMovie.objects.get_or_create(
                    movie=movie,
                    person=person,
                    defaults=pm_data
                )
                if created:
                    PersonMovie.objects.filter(id=pm.id).update(**pm_data)
                    count +=1
                progress_bar(int(count) + 1, file_len(file))
        print('')
        print('Data transfering completed')