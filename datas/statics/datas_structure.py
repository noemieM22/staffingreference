
# Get the fields name of a table
def get_fields(tableSource):
        Fields = tableSource._meta.get_fields()
        fields =[]
        for field in Fields:
            if (field.name != 'id' and str(type(field)) != "<class 'django.db.models.fields.reverse_related.ManyToOneRel'>"):
                fields_name ={}
                fields_name[field.name]=field.verbose_name
                fields.append(fields_name)
        return fields
