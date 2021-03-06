from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase
import shortuuid
# Create your models here.


class MoodTag(TagBase):
    # name and slug will inherit
    pass

    class Meta:
        verbose_name = "Mood Tag"
        verbose_name_plural = "Mood Tags"


class LangTag(TagBase):
    # name and slug will inherit
    pass

    class Meta:
        verbose_name = "Lang Tag"
        verbose_name_plural = "Lang Tags"


class MoodTaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(MoodTag,
                            related_name="%(app_label)s_%(class)s_items")


class LangTaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(LangTag,
                            related_name="%(app_label)s_%(class)s_items")


def user_directory_path(instance, filename):
    # file will be uploaded to
    uid = shortuuid.uuid()
    return '{0}/{1}.png'.format(instance.collection.id, uid)


class ComicCollection(models.Model):
    name = models.CharField(max_length=100, default='Collection with No Name')
    lang_tags = TaggableManager(through=LangTaggedItem)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class ComicImage(models.Model):
    collection = models.ForeignKey(ComicCollection, related_name='cimages')
    name = models.CharField(max_length=100, default='Image with No Name')
    image = models.ImageField(upload_to=user_directory_path)
    mood_tags = TaggableManager(through=MoodTaggedItem)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class ComicStrip(models.Model):
    name = models.CharField(max_length=100, default='Comic with No Name')
    image = models.ImageField(upload_to="strips")
    featured = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
