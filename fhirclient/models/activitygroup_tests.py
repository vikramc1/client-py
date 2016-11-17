#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.7.0.10061 on 2016-10-24.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import activitygroup
from .fhirdate import FHIRDate


class ActivityGroupTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ActivityGroup", js["resourceType"])
        return activitygroup.ActivityGroup(js)
    
    def testActivityGroup1(self):
        inst = self.instantiate_from("activitygroup-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityGroup instance")
        self.implActivityGroup1(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityGroup", js["resourceType"])
        inst2 = activitygroup.ActivityGroup(js)
        self.implActivityGroup1(inst2)
    
    def implActivityGroup1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

