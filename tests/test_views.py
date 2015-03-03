# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
import pytest
from selenium.common.exceptions import NoSuchElementException

__author__ = 'johannes'


class ViewTestMixin(object):
    url = ''

    def test_get(self, client):
        response = client.get(self.url)
        assert response.status_code == 200


def test_single_value_model_field(db, client, driver):
    url = reverse('test_single_value_model_field')
    response = client.get(url)
    assert response.status_code == 200

    driver.get("%s%s" % ('http://localhost:8081', url))
    with pytest.raises(NoSuchElementException):
        driver.find_element_by_xpath('//body[@JSError]')
