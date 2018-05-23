import re
import unicodedata

from django.utils import six
from django.utils.encoding import force_text
from django.utils.functional import lazy
from django.utils.safestring import SafeText, mark_safe


def slugify_unicode(value):
    value = force_text(value)
    value = unicodedata.normalize('NFKC', value)
    value = re.sub('[^\w\s-]', '', value, flags=re.U).strip().lower()
    return mark_safe(re.sub('[-\s]+', '-', value, flags=re.U))


slugify_unicode = lazy(slugify_unicode, six.text_type, SafeText)
