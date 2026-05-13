from django.db import models

class AboutImage(models.Model):
    name = models.CharField(max_length=100)
    static_path = models.CharField(max_length=200)  # Stores path like 'images/1.png'
    alt_text = models.CharField(max_length=200, blank=True)
    class Meta:
        verbose_name = "About Image"
        verbose_name_plural = "About Image"
    def __str__(self):
        return self.name
    @property
    def static_url(self):
        """Returns the URL to use in templates with {% static %} tag"""
        return f"images/{self.static_path}"
    




class ServiceCard(models.Model):
    """
    Service card model using static paths like AboutImage
    """
    servicename = models.CharField(max_length=100)  # Card identifier name
    service_path = models.CharField(max_length=200)  # e.g. 'services/web-dev.jpg'
    alt_text = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=100)  # Display title (h3)
    description = models.TextField()          # Card paragraph text
    order = models.PositiveIntegerField(default=0)  # Display order
    link = models.CharField(max_length=100, default='#')  # Link to service details
    class Meta:
        verbose_name = "Service Card"
        verbose_name_plural = "Service Cards"
        ordering = ['order']
    def __str__(self):
        return self.servicename
    @property
    def static_url(self):
        """Returns the URL to use in templates with {% static %} tag"""
        return f"images/{self.service_path}"
    


class ProjectCard(models.Model):
    projectname = models.CharField(max_length=100)
    project_path = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    
    # Fix: add null=True and blank=True or a default value
    linkto = models.CharField(max_length=100, default='#')  # This is correct

    class Meta:
        verbose_name = "Project Card"
        verbose_name_plural = "Project Cards"

    def __str__(self):
        return self.projectname

    @property
    def static_url(self):
        return f"images/{self.project_path}"


class WebDevProjectCard(models.Model):
    projectname = models.CharField(max_length=100)
    project_path = models.CharField(max_length=200)
    link = models.CharField(max_length=200, default='#')
    title = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = "Web Dev Project Card"
        verbose_name_plural = "Web Dev Project Card"

    def __str__(self):
        return self.projectname

    @property
    def static_url(self):
        return f"images/{self.project_path}"


class AppDevProjectCard(models.Model):
    projectname = models.CharField(max_length=100)
    project_path = models.CharField(max_length=200)
    link = models.CharField(max_length=200, default='#')
    title = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = "App Dev Project Card"
        verbose_name_plural = "App Dev Project Card"

    def __str__(self):
        return self.projectname

    @property
    def static_url(self):
        return f"images/{self.project_path}"
    

class PythonDevProjectCard(models.Model):
    projectname = models.CharField(max_length=100)
    project_path = models.CharField(max_length=200)
    link = models.CharField(max_length=200, default='#')
    title = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = "Python Dev Project Card"
        verbose_name_plural = "Python Dev Project Card"

    def __str__(self):
        return self.projectname

    @property
    def static_url(self):
        return f"images/{self.project_path}"
    


class UIUXProjectCard(models.Model):
    projectname = models.CharField(max_length=100)
    project_path = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = "UI/UX Project Card"
        verbose_name_plural = "UI/UX Project Card"

    def __str__(self):
        return self.projectname

    @property
    def static_url(self):
        return f"images/{self.project_path}"


class AchivementCard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=200, default='#')
    
    class Meta:
        verbose_name = "Achievement Card"
        verbose_name_plural = "Achievement Cards"

    def __str__(self):
        return self.title

    @property
    def static_url(self):
        return f"images/{self.title.replace(' ', '-').lower()}.jpg"  # Example static URL generation
    


class AchivementCardModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=200, default='#')
    
    class Meta:
        verbose_name = "Achievement Card Model"
        verbose_name_plural = "Achievement Cards Model"

    def __str__(self):
        return self.title

    @property
    def static_url(self):
        return f"images/{self.title.replace(' ', '-').lower()}.jpg"  # Example static URL generation
    
class certificate(models.Model):
    name = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    date = models.DateField()
    cataegory = models.CharField(max_length=100)
    image= models.CharField(max_length=200)
    description = models.TextField()
    link = models.CharField(max_length=200, default='#')

    badge = models.CharField(max_length=200, default='#')
    badge2 = models.CharField(max_length=200, default='#')

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"

    def __str__(self):
        return self.name
    @property
    def static_url(self):
        """Returns the URL to use in templates with {% static %} tag"""
        return f"images/{self.image}"



class blog(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    cataegory = models.CharField(max_length=100)
    image= models.CharField(max_length=200)
    description = models.TextField()
    link = models.CharField(max_length=200, default='#')

    class Meta:
        verbose_name = "Blogs"
        verbose_name_plural = "Blogs Posts"

    def __str__(self):
        return self.name
    @property
    def static_url(self):
        """Returns the URL to use in templates with {% static %} tag"""
        return f"images/{self.image}"




class ServiceCategory(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Services'),
        ('seo', 'SEO'),
        ('photo', 'Photography'),
        ('app', 'App Development'),
    ]

    key = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=20)
    description = models.TextField()
    monthly_price = models.IntegerField()
    yearly_price = models.IntegerField()
    button_type = models.CharField(max_length=20, default="ghost")

    def __str__(self):
        return self.title


class ServicePlan(models.Model):
    TIER_CHOICES = [
        ('starter', 'Starter'),
        ('pro', 'Pro'),
        ('enterprise', 'Enterprise'),
    ]

    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='plans')

    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    tier = models.CharField(max_length=20, choices=TIER_CHOICES)
    tag = models.CharField(max_length=50)
    emoji = models.CharField(max_length=20)

    image = models.ImageField(upload_to='services/')
    
    perk1 = models.CharField(max_length=200)
    perk2 = models.CharField(max_length=200)
    perk3 = models.CharField(max_length=200)

    def __str__(self):
        return self.name