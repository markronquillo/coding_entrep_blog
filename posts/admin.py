from django.contrib import admin

# Register your models here.

from posts.models import Post


class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'content', 'timestamp']
	list_display_links = ['title', 'content']
	list_filter = ['timestamp', 'updated']
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)
