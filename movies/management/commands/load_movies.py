import os.path
from django.core.management.base import BaseCommand
from movies.models import Movie


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
                if data[1] not in ("movie", "short"):
                    continue
                date = data[5]
                if date == "\\N":
                    date = None
                else:
                    date = f"{date}-01-01"
                adult = data[4]
                if adult == 0:
                    adult == False
                else:
                    adult == True
                genres = data[8]
                if "\\N" in genres:
                    genres = None
                else:
                    genres = genres.split(",")
                movie_data = {
                    "title_type": data[1],
                    "name": data[2],
                    "is_adult": adult,
                    "date": date,
                    "genres": genres,
                }
                movie, created = Movie.objects.get_or_create(
                    imdb_id=data[0], defaults=movie_data
                )

                if created:
                    Movie.objects.filter(id=movie.id).update(**movie_data)
                    count +=1
                progress_bar(int(count) + 1, file_len(file))
        print('')
        print('Data transfering completed')