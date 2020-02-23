from django.contrib import admin

# Register your models here.

from .models import Contact, Applying, AdminUpdate, SelectIntern1, SelectIntern2, SelectIntern3,Solution1,Solution2,Solution3

admin.site.register(Contact)

admin.site.register(Applying)
admin.site.register(AdminUpdate)

admin.site.register(SelectIntern1)
admin.site.register(SelectIntern2)
admin.site.register(SelectIntern3)

admin.site.register(Solution1)
admin.site.register(Solution2)
admin.site.register(Solution3)