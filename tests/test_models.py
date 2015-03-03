# -*- coding:utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function
from django_select2.models import KeyMap

__author__ = 'johannes'


class TestKeyMap(object):
    def test_create(self):
        KeyMap.objects.create()
