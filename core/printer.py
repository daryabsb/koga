import brother_ql
import os
from django.conf import settings
from brother_ql.devicedependent import models, label_type_specs, label_sizes
from brother_ql.devicedependent import ENDLESS_LABEL, DIE_CUT_LABEL, ROUND_DIE_CUT_LABEL
from brother_ql import BrotherQLRaster, create_label
from brother_ql.backends import backend_factory, guess_backend



b = brother_ql.create_label(qlr=1,image='/media/user/01e6548e-c4e9-42a2-94f7-e0afb470b4cd.png',label_size=['17','52'])
# print(b)