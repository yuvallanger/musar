from django.test import TestCase
from django.contrib.auth.models import User#, UserProfile
from datetime import date, timedelta #time, date
from payments.models import (
    Corporation, Payment,
)
from payments.utils import lateness_days


# Create your tests here.

#class CompanyTest(TestCase):
#
#    def test_create_company(self):
#        Company.objects.create(
#            cid='123',
#            name="Hasadna",
#            url="http://www.hasadna.org.il/",
#            email="info@hasadna.org.il",
#
#        )
#
#        self.assertEqual(1, Company.objects.count())
#
#        Company.objects.create(
#            cid='abc',
#            name="Avi",
#            url="http://www.avi.co.il/",
#            email="info@avi.co.il",
#        )
#        self.assertEqual(
#            2, Company.objects.count()
#        )
#
#        # Test retrieve companies by name
#        self.assertEqual(1, Company.objects.filter(name='Hasadna').count())
#        self.assertEqual(1, Company.objects.filter(name='Avi').count())
#        self.assertEqual(0, Company.objects.filter(name='Moshe').count())
#        # TODO: how do I retrieve the preferences for company2
#
#
#class PaymentTest(TestCase):
#
#    def setUp(self):
#        self.company1 = Company.objects.create(
#            cid='sc1',
#            name="FSF",
#            url="http://www.fsf.org/",
#            email="info@fsf.org",
#        )
#        self.company2 = Company.objects.create(
#            cid='sc2',
#            name="Yossi",
#            url="http://www.yossi.co.il/",
#            email="info@yossi.co.il",
#        )
#
#    def test_create_payment(self):
#        Payment.objects.create(
#            buyer=self.company1,
#            seller=self.company2,
#            dueDate=datetime.now(),
#            orderdate=datetime.now(),
#            input_user=self.company1,
#        )
#        self.assertEqual(1, Payment.objects.count())
#
#    #       Test in and out payments counts before and after creating a
#    #       payment
#    def test_company_payements_associations(self):
#
#        self.assertEqual(
#            0, self.company1.out_payments.count(),
#        )
#        self.assertEqual(
#            0, self.company2.out_payments.count(),
#        )
#        self.assertEqual(
#            0, self.company1.in_payments.count(),
#        )
#        self.assertEqual(
#            0, self.company2.in_payments.count(),
#        )
#
#        self.assertEqual(0, Payment.objects.count())
#
#        Payment.objects.create(
#            buyer=self.company1,
#            seller=self.company2,
#            dueDate=datetime.now(),
#            orderdate=datetime.now(),
#            input_user=self.company1,
#        )
#        self.assertEqual(
#            1, Payment.objects.count())
#
#        self.assertEqual(
#            1, self.company1.out_payments.count(),
#        )
#
#        self.assertEqual(
#            0, self.company2.out_payments.count(),
#        )
#
#        self.assertEqual(
#            0, self.company1.in_payments.count(),
#        )
#
#        self.assertEqual(
#            1, self.company2.in_payments.count(),
#        )
#
#

class UtilsTest(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(username='user1')
        #self.up1 = UserProfile.objects.create(user=self.u1)

        """
        supply: time of goods delivery-
        due: agreed time of payment
        pay: actual time of payment
        credit = pay - supply
        late = max(pay - due, 0)
        """

        credit_days = 100
        late_days = 84
        supply_date = date(2008, 8, 18)
        due_date = supply_date + timedelta(days=credit_days)
        late_date = supply_date + timedelta(days=late_days)

        self.days = (due_date - late_date).days

        print self.delta.days

        #http://stackoverflow.com/questions/151199/how-do-i-calculate-number-of-days-betwen-two-dates-using-python
        #http://docs.python.org/2/library/datetime.html

        self.c1 = Corporation.objects.create(
            cid="fsf"
        )

        self.p1 = Payment.objects.create(
            corporation=self.c1,
            owner=self.u1,
            #amount=csv_model.amount,
            #title=csv_model.title,
            due_date=due_date,
            supply_date=due_date,
            #order_date=d1,
            pay_date=pay_date
        )

    def tearDown(self):
        self.p1.delete()
        self.c1.delete()

    def test_create_lateness_delta(self):

        print 'delta', self.delta
        print 'lateness_delta', lateness_delta(self.p1)
        assert lateness_delta(self.p1) == -8


#        from django.test import TestCase
#        from myapp.models import Animal
#
#        class AnimalTestCase(TestCase):
#            def setUp(self):
#                Animal.objects.create(name="lion", sound="roar")
#                Animal.objects.create(name="cat", sound="meow")
#
#            def test_animals_can_speak(self):
#                """Animals that can speak are correctly identified"""
#                lion = Animal.objects.get(name="lion")
#                cat = Animal.objects.get(name="cat")
#                self.assertEqual(lion.speak(), 'The lion says "roar"')
#                self.assertEqual(cat.speak(), 'The cat says "meow"')
