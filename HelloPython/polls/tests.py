# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionModelTest(TestCase):

	def test_was_published_recently_with_future_question(self):
		""" was_published_recently() returns false for any question from the future """
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		""" was_published_recently() returns false for any question posted 1 day before """
		time = timezone.now() - datetime.timedelta(days=1)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		""" was_published_recently() reutrn true for any quesstion posted within the last day """
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True)

