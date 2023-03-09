from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BrandModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class ColorModel(models.Model):
    title = models.CharField(max_length=15, null=True, blank=True,)
    code = models.CharField(max_length=15,)
    created_at = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class PhoneModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='phones')
    short_description = models.CharField(max_length=555)
    long_description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.PROTECT,
                                 related_name='phones',
                                 verbose_name='category'
                                 )
    brand = models.ForeignKey(BrandModel,
                              on_delete=models.PROTECT,
                              related_name='phones')
    colors = models.ManyToManyField(ColorModel, related_name='phones')
    processor = models.CharField(max_length=255)
    GPU = models.CharField(max_length=255)
    RAM = models.CharField(max_length=255)
    built_in_memory = models.CharField(max_length=255)
    number_of_processor_cores = models.CharField(max_length=255)
    main_lens = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'phone'
        verbose_name_plural = 'phones'


class AccessoriesModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='accessories')
    short_description = models.CharField(max_length=555)
    long_description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.PROTECT,
                                 related_name='accessories',
                                 verbose_name='category'
                                 )
    brand = models.ForeignKey(BrandModel,
                              on_delete=models.PROTECT,
                              related_name='accessories')
    colors = models.ManyToManyField(ColorModel, related_name='accessories')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'accessor'
        verbose_name_plural = 'accessories'
