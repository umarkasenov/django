from django.db import models


class PhoneShop(models.Model):
    DISCOUNT_PERCENTAGE = (
        ("10", '10%'),
        ("20", '20%'),
        ("30", '30%'),
        ("40", '40%'),
        ("50", '50%'),
    )

    title = models.CharField(max_length=100, verbose_name="Укажите название телефона")
    description = models.TextField(verbose_name="Укажите описание телефона")
    image_1 = models.ImageField(upload_to="", verbose_name="Загрузите фото")
    image2 = models.URLField(verbose_name="Укажите ссылку на фото",
                             blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name="Укажите цену", )
    discount = models.CharField(max_length=100, choices=DISCOUNT_PERCENTAGE)
    gift = models.CharField(max_length=100, verbose_name="Укажите подарок к покупке",
                            blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}-{self.price}"

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"


class ReviewsPhones(models.Model):
    phone_review = models.ForeignKey(PhoneShop, on_delete=models.CASCADE,
                                     related_name="reviews_phones")
    text = models.TextField(verbose_name="Напишите комент")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_review}-{self.text}"
