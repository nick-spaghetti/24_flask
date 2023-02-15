from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        '''stuff to do before every test'''
        self.client = app.test_client()
        app.testing = True
        print('running each test')

    def test_home(self):
        '''make sure info is in the session and html is displayed'''
        with self.client:
            res = self.client.get('/')
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            self.assertIn(b'<p>high score:', res.data)
            self.assertIn(b'<p>score:', res.data)
            self.assertIn(b'<p>seconds left:', res.data)

    def test_valid_word(self):
        '''test if word is valid by modifying the board in the session'''
        with self.session_transaction() as session:
            session['board'] = [
                ['C', 'A', 'T', 'T', 'T'],
                ['C', 'A', 'T', 'T', 'T'],
                ['C', 'A', 'T', 'T', 'T'],
                ['C', 'A', 'T', 'T', 'T'],
                ['C', 'A', 'T', 'T', 'T']
            ]
            res = self.client.get('/check-word?word=cat')
            self.assertEqual(res.json['result'], 'ok')

    def test_invalid_word(self):
        '''test if word is in the dictionary'''
        self.client.get('/')
        res = self.client.get('/check-word?word=impossible')
        self.assertEqual(res.json['result'], 'not-on-board')

    def non_english_word(self):
        '''test if word is on the board'''
        self.client.get('/')
        res = self.client.get('/check-word?word=fsjdakfkldsfjdslkfjdlksf')
        self.assertEqual(res.json['result'], 'not-word')
