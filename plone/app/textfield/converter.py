import zope.component

from plone.z3cform.converter import DefaultWidgetInputConverter

import z3c.form.interfaces

from plone.app.textfield.interfaces import IRichText
from plone.app.textfield.widget import IRichTextWidget


class RichTextWidgetInputConverter(DefaultWidgetInputConverter):
    """Converts rich text object into a suitable form input value"""

    zope.component.adapts(IRichText, IRichTextWidget)

    def toWidgetInputValue(self, value):
        """See plone.z3cform.interfaces.IWidgetInputConverter"""
        return z3c.form.interfaces.IDataConverter(self.widget).toFieldValue(value).raw
