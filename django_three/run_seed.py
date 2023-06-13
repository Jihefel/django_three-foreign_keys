import django
django.setup()

from core.seed import run

if __name__== '__main__':
    run()
