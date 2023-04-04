from django.contrib.auth.models import User , Group

# exec(open(r'E:\vspython\B8_django\Libraryproject\firstapp\dbshell.py').read())

# to see the User
# print(User.objects.all())

## to creat the user 
# User.objects.create_user(username= 'admin'  , password='admin@123' , email='admin@gmail.com' )
# from django.utils.crypto import get_random_string
# print(get_random_string(10))