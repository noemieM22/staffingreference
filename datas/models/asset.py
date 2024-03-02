from django.db import models

# models linked with assets

# catégory :
class Asset_category(models.Model):

    asset_category_FR = models.CharField("Catégorie d'un actif",max_length=50)
    asset_category_parent =  models.ForeignKey('self', on_delete=models.CASCADE,verbose_name='Catégorie parent')
    # asset_category_level =  models.SmallIntegerField("Niveau d'un actif",null=True, blank = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['asset_category_FR','asset_category_parent'], name='unique Asset_category')
        ]
    def __str__(self):
        return self.asset_category_FR

# type : opérationnel/ administratif?
class Asset_type(models.Model):

    asset_type_FR = models.CharField("Type d'un actif",max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['asset_type_FR'], name='unique Asset_type')
        ]
    def __str__(self):
        return self.asset_type_FR

class Asset(models.Model):

    asset_FR =  models.CharField("Libellé d'un actif",max_length=50)
    asset_category = models.ForeignKey(Asset_category, on_delete = models.CASCADE,related_name='Asset_category',verbose_name='Catégorie')
    asset_type = models.ForeignKey(Asset_type, on_delete = models.CASCADE,related_name='Asset_type',verbose_name='Type')
    asset_loan = models.BooleanField(default ='False',verbose_name='Prêt possible')


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['asset_FR'], name='unique Asset')
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
