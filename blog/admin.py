from django.contrib import admin
from blog.models import Post

admin.site.register(Post) #to  make model visible on admin page

#class PostAdmin(ImportExportModelAdmin, admin.PostAdmin):
	#pass

#admin.site.register(Post, PostAdmin)

