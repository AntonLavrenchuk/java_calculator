import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django

django.setup()

import random
from first_app.models import *
from faker import Faker

fake = Faker()
topics = ['Search', 'Social', 'News', 'Games']


def add_topic():
    topic = Topic.objects.get_or_create(name=random.choice(topics))[0]
    topic.save()
    return topic


def populate(N=5):
    for entry in range(N):
        topic = add_topic()

        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        webpage = Webpage.objects.get_or_create(topic=topic, url=fake_url, name=fake_name)[0]

        accessRecord = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]


if __name__ == '__main__':
    print('population...')
    populate(20)
    print('complete!')
