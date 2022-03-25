from django.db import models
from django.utils import timezone
import datetime

class Article(models.Model):
    """Database reference to each article.

    The article content themselves should exist as HTML files under templates/blog_app/content.
    """
    published_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(default=timezone.now)  # Use default over auto_add to keep it editable.
    title = models.CharField(max_length=160, help_text="The article's title, as displayed in the article and in list views.")
    slug = models.SlugField(unique=True, help_text="The article's URL slug.")
    summary = models.TextField(max_length=255, help_text="A summary of the content of the article, displayed only in the list view.")
    template_filename = models.CharField(max_length=255, help_text="The path to this article's template relative to templates/blog_app/content.")

    MODIFICATION_LEEWAY = datetime.timedelta(minutes=30)
    #TODO when do we no longer care that it was edited?

    def __str__(self):
        return self.slug

    def is_modified_time_significant(self) -> bool:
        is_difference_significant = self.modified_datetime > self.published_datetime + Article.MODIFICATION_LEEWAY
        was_it_ages_ago = datetime.datetime.now()
        return 