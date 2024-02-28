from django.db import models

# models linked with assets


class Asset_category(models.Model):

    asset_category_FR = models.CharField("Catégorie d'un actif",max_length=50)
    asset_category_level =  models.SmallIntegerField("Niveau d'un actif",null=True, blank = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['asset_category_FR'], name='unique Asset_category')
        ]

class Asset_type(models.Model):

    asset_type_FR = models.CharField("Type d'un actif",max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['asset_type_FR'], name='unique Asset_category')
        ]

class Asset(models.Model):

    asset_FR =  models.CharField("Libellé d'un actif",max_length=50)
    asset_category = ForeignKey(Asset_category, on_delete = models.CASCADE,related_name='Asset_category')
    asset_type = ForeignKey(Asset_type, on_delete = models.CASCADE,related_name='Asset_type')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['asset_FR','asset_category'], name='unique Asset')
        ]
