from django.contrib import admin

from .models import Topic

from django.contrib import admin

from .models import Topic, Comment

# class CommentInline(admin.StackedInline):
#     model = Comment
#     extra = 3

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3

class TopicAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "topic_text"]
    fieldsets = [
        (None, {"fields": ["topic_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [CommentInline]
    list_display = ["topic_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["topic_text"]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment)