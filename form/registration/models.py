from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    school_id = models.CharField(max_length=20)
    skill = models.CharField(max_length=30)  # Ensure this matches the form's field
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# from django.db import models

# class Student(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()
#     school_id = models.CharField(max_length=20)
#     course_code = models.CharField(max_length=20)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
