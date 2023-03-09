from django.db import models


class AuthorModels(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class PostModels(models.Model):
    title = models.CharField(max_length=512)
    author = models.ForeignKey(AuthorModels,
                               on_delete= models.PROTECT,
                               related_name='post')
    image = models.ImageField(upload_to='image')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # def get_prev(self):
    #     return self.get_previous_by_created_at()
    #
    # def get_next(self):
    #     return self.get_next_by_created_at()
    #
    # def get_comments(self):
    #     return self.comments.order_by('-created_at')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class CommentModels(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=30,  null=True, blank=True)
    comment = models.TextField()
    post = models.ForeignKey(PostModels,
                             on_delete= models.CASCADE,
                             related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
