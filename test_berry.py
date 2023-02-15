from flask import session
from unittest import TestCase
# import berry
from berry import app


class ColorViewsTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        print('inside set up class')

    @classmethod
    def tearDownClass(cls):
        print('inside tear down class')

    def setUp(self):
        '''stuff to do before every test'''
        print('inside set up')

    def tearDown(self):
        '''stuff to do after each test'''
        print('inside tear down')

    def test_1(self):
        ...

    def test_2(self):
        ...

    def test_color_form(self):
        with app.test_client() as client:
            # import pdb
            # pdb.set_trace()
            res = client.get('/')
            html = res.get_date(as_text=True)  # gives us the html data

            # make sure the status code on our res = 200
            self.assertEqual(res.status_code, 200)
            # check if html contains this h1.  specify string/list/etc if it is in html
            self.assertIn('<h1>color form</h1>', html)

    def test_color_submit(self):
        with app.test_client() as client:
            # route we're sending the request to
            res = client.post('/fav-color', data={'color': 'orange'})
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h3>woah i like orange too</h3>', html)

    def test_redirection(self):
        with app.test_client() as client:
            # get request
            res = client.get('/redirect-me')
            # this res object has different header values from a res in http res
            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, 'http://localhost/')
            # actual location, instead of 'http://localhose:5000/' may be a quirk of how test_client works, but we have to check localhost in general

    def test_redirection_followed(self):
        with app.test_client() as client:
            res = client.get('/redirect-me', follow_redirects=True)
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>color form</h1>', html)

    def test_session_count(self):
        with app.test_client() as client:
            # any changes to session should go in here:
            with client.session_transaction() as change_session:
                change_session['count'] = 999
            # now those changes will be in flask's 'session'
            res = client.get('/')
            self.assertEqual(res.status_code, 200)
            self.assertEqual(session['count'], 1)

    def test_submit_taxes(self):
        with app.test_client() as client:
            res = client.get('/taxes', data={'income': '1000'})
            html = res.get_date(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>you owe $150</h1>', html)

    def test_calc_taxes(self):
        self.assertEqual(calc_taxes(100), 15)
        self.assertEqual(calc_taxes(10000), 15)
        self.assertEqual(calc_taxes(0), 15)
        self.assertEqual(calc_taxes(-21132), 15)
        self.assertEqual(calc_taxes('apple'), 15)

# class AlgorithmsTestCase(TestCase):
#     def test_reverse(self):
#         self.assertEqual(reverse_str('hello'), 'olleh')
#         self.assertEqual(reverse_str('Apple'), 'elppA')

#     def test_is_palindrome(self):
#         # self.assertEqual(is_palindrome('racecar'), True)
#         self.assertTrue(is_palindrome('racecar'))
#         # should ignore casing
#         self.assertTrue(is_palindrome('Racecar'))
#         self.assertTrue(is_palindrome('kayak'))
#         self.assertFalse(is_palindrome('taco'))

#     def test_factorial(self):
#         self.assertEqual(factorial(5), 120)
#         self.assertEqual(factorial(3), 6)
#         # self.assertRaises(ValueError, factorial(-5))
#         self.assertRaises(ValueError, factorial, -5)
#         self.assertRaises(ValueError, factorial, 4.3)

# class AdditionTestCase(TestCase):
#     '''example of unit tests'''

#     def test_adder(self):
#         assert berry.adder(2, 3) == 5

#     def test_adder_2(self):
#         self.assertEqual(berry.adder(2, 2), 4)
#         self.assertEqual(berry.adder(-2, -4), -6)
#         self.assertEqual(berry.adder(40, 50), 90)
