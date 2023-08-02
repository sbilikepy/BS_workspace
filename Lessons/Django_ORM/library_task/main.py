from models import LiteraryFormat
from managers import LiteraryFormatManager

if __name__ == '__main__':
    # initialisation
    LiteraryFormat.objects = LiteraryFormatManager()
    # execute commands where object is new custom obj name
    print(LiteraryFormat.objects.all())
