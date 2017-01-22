import json

from channels import Group
from channels.binding.base import UPDATE
from channels.tests import ChannelTestCase, HttpClient

from ..consumers import Demultiplexer
from .. import models

class HeroBindingTests(ChannelTestCase):

    def test_create_hero(self):
        Group("hero-updates").add("hero-reply")
        hero = models.Hero.objects.create(name='My hero')

        message = self.get_next_message('hero-reply', require=True)

        content = json.loads(message['text'])
        self.assertEqual(content['stream'], 'hero')

        payload = content['payload']
        self.assertEqual(payload['model'], 'hero_service.hero')
        self.assertEqual(payload['action'], 'create')
        self.assertEqual(payload['pk'], hero.pk)

        data = payload['data']
        self.assertEqual(data['name'], hero.name)

    def test_update_hero(self):
        hero = models.Hero.objects.create(name='My hero')

        payload = {
            'action': UPDATE,
            'pk': hero.pk,
            'data': {
                'name': 'Still my hero',
            },
        }

        client = HttpClient()
        client.send_and_consume('websocket.receive', path='/api/ws', text={
            'stream': 'hero',
            'payload': payload,
        })

        hero.refresh_from_db()
        self.assertEqual(hero.name, 'Still my hero')
