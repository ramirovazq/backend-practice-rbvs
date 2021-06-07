from datetime import datetime

from django.core.exceptions import ValidationError
from options.models import validate_hour

greater = datetime(2021, 9, 8, 1, 0)
reference = datetime(2021, 9, 8, 0, 6)
minor = datetime(2021, 9, 8, 0, 1)


greater_time = greater.time()
reference_time = reference.time()
minor_time = minor.time()

assert not(greater_time < reference_time), "Something wrong"
assert minor_time < reference_time, "Something wrong"

'''
answer = validate_hour(minor)
assert answer == None, "Something wrong"

try:
    answer = validate_hour(greater)
except ValidationError:
    pass
'''