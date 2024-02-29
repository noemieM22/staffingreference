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
            models.UniqueConstraint(fields=['asset_type_FR'], name='unique Asset_type')
        ]


class Asset(models.Model):

    asset_FR =  models.CharField("Libellé d'un actif",max_length=50)
    asset_category = models.ForeignKey(Asset_category, on_delete = models.CASCADE,related_name='Asset_category')
    asset_type = models.ForeignKey(Asset_type, on_delete = models.CASCADE,related_name='Asset_type')
    asset_loan = models.BooleanField(default ='False')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['asset_FR','asset_category'], name='unique Asset')
        ]


# class Asset_loan(models.Model):
#
#     asset = models.ForeignKey(Asset, on_delete = models.CASCADE,related_name='Asset_loan')
#     asset_loan = models.BooleanField(default ='False')
#
#
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['asset','asset_loan'], name='unique Asset_loan')
#         ]
