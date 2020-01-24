from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def index(request):
    context_dict = {}
    response = render(request, 'index.html', context_dict)
    return response


def signup_login(request):
    context_dict = {}
    if request.method == 'GET':
        pass
    else:
        user_data = request.POST
        username = user_data.get('username')
        email = user_data.get('email')
        password = user_data.get('password')

        # Signup handling goes here

        if user_data.get('submit') == 'signup':
            data = {
                'user_created': False
            }
            try:
                User.objects.create_user(username=username, email=email, password=password)
            except Exception as e:
                print(f'exception is {e}')
                return JsonResponse(data)
            else:
                data['user_created'] = True
                messages.success(request, f"User created successfully for '{username}'")
                return JsonResponse(data)

        # LOGIN handling

        elif user_data.get('submit') == 'login':
            user = authenticate(username=username, password=password)
            next_url = user_data.get('next')          # next_url gives the url to redirect to previous page after login
            print("next in post: {}".format(next_url))
            if user:
                login(request, user)
                return JsonResponse({'logged_in': True, 'next_url': next_url})
            else:
                print("Authentication failed")
                return JsonResponse({'logged_in': False})

        else:
            print("in no where")
            pass

    response = render(request, 'signup.html', context_dict)
    return response


def validate_username(request):
    username = request.GET.get('username')
    print(username)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['message'] = 'already taken!'
    else:
        data['message'] = 'available'
    return JsonResponse(data)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
