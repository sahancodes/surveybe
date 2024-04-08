from django.http import JsonResponse
from django.urls import reverse
from django.core.mail import send_mail
from .models import Account
from .serializers import AccountSerializer, InsertSerializer, UserSerializer, GetUserSerializer, IsUserLoggedIn, ForgotPasswordSerializer, UpdateSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from django.http import HttpRequest
from rest_framework.request import Request


# # Create your views here.
@api_view(['GET'])                  #decorator to include many requests from single function
def accounts_list(request):                 #get all accs, serialize them and return json

    if request.method == 'GET':
        all_accs = Account.objects.all()
        serializer = AccountSerializer(all_accs, many=True)

        return JsonResponse({'all_profiles':serializer.data})


@api_view(['POST'])
def signup(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        u_serializer = UserSerializer(data=data)
        i_serializer = InsertSerializer(data=data)

        if u_serializer.is_valid() and i_serializer.is_valid():
            user = User.objects.create_user( data['username'], data['email'], data['password'])
            user.save()
            
            try:

                new_acc = Account.objects.get(userid=user.id)

                new_acc.username = user.username
                new_acc.email = data['email']                       #This can be done using serializers at once without going one by one
                new_acc.age = data['age']                           #Doing this with serializers only will give the correct Data types
                new_acc.gender = data['gender']
                new_acc.height = data['height']
                new_acc.weight = data['weight']
                new_acc.best_hours = data['best_hours']
                new_acc.worksstarttime = data['worksstarttime']
                new_acc.workendtime = data['workendtime']
                new_acc.selfstatement = data['selfstatement']

                new_acc.rank = 99
                new_acc.contribution = 25
                new_acc.level = 1

                new_acc.save()

            except Account.DoesNotExist:
                print("New user does not exist!")

            return Response( i_serializer.data, status=status.HTTP_201_CREATED)    #Return a response to the request eg: 200 OK


@api_view(['POST'])
def signupavailablity(request):

    # try:
    if request.method == 'POST':
        data = JSONParser().parse(request)
        snt_usrname = data['username']
        snt_email = data['email']

        print(snt_usrname, snt_email)

        if User.objects.filter(username=snt_usrname).exists() or User.objects.filter(email=snt_email).exists():
            return JsonResponse({'isAvailable': False})
        else:
            return JsonResponse({'isAvailable': True})
    # except Exception as e:
    #     return JsonResponse({'error': str(e)}, status=400)


@api_view(['POST'])
def getuser(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        find_acc = Account.objects.get(userid = int(data['userid']))
        get_acc = Account.objects.filter(userid = find_acc.userid)
        gu_serializer = GetUserSerializer(get_acc, many=True)

        return JsonResponse({'profile':gu_serializer.data})
    

@api_view(['GET'])
def isreg(request):

    if request.method == 'GET':
        data = JSONParser().parse(request)
        try:
            User.objects.get(id = int(data['userid']))
            return JsonResponse({'reg_status':'True'}, status = status.HTTP_200_OK)
        except:
            return JsonResponse({'reg_status':'False'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])        
def loginuser(request):

    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        _, token = AuthToken.objects.create(user)
        find_acc = Account.objects.filter(username=data['username'])
        user = User.objects.get(username=data['username'])
        updt_token = find_acc.update(authtoken = token)
        return Response({'token': token, 'user_id': user.pk}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# -------------  LOUGOUT CHECK AFTER DEPLOYMENT ----------------#
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    django_request = request._request
    assert isinstance(django_request, HttpRequest), "Invalid request type"
    logout(django_request)
    return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
    


@api_view(['GET'])
def isuser(request):
    data = JSONParser().parse(request)

    try:
        user_auth = Account.objects.get(userid=data['userid'])
        token = user_auth.authtoken
        if token:
            return Response({"user_status": "True", "auth_token": token}, status=status.HTTP_200_OK)
    except:
        return Response({"user_status": "False", "message": "User not logged in"}, status=status.HTTP_404_NOT_FOUND)
    


# ------------------- CHECK FORGOT PASSWORD FUNCTION AFTER HOSTING --------------------#

@api_view(['POST'])
@parser_classes([JSONParser])
def forgotpassword(request):
    data = JSONParser().parse(request)
    fp_serializer = ForgotPasswordSerializer(data=data)

    print(data)

    # if fp_serializer.is_valid():
    email = data['email']
    user = get_object_or_404(get_user_model(), email=email)
    
    token = AuthToken.objects.create(user)[1]

    # reset_url = reverse('reset-password', kwargs={'token' : token})
    # reset_url = request.build_absolute_uri(reset_url)

    reset_url = "{protocol}://{domain}{path}?token={token}".format(
        protocol = request.scheme,
        domain = request.META['HTTP_HOST'],
        path = '/accounts/resetpassword/',
        token=token
    )

    #Message for Email
    subject = 'Password Reset'
    message = f'Click the following link to reset your password: {reset_url}'

    send_mail(subject, message, 'sahannetherlands@gmail.com', [email])

    return Response({'detail': 'Password reset email is sent successfully'})
    # else:
    #     return Response(fp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------- CHECK RESET PASSWORD FUNCTION AFTER HOSTING --------------------#

@api_view(['POST'])
def resetpassword(request, token):
    user = get_object_or_404(get_user_model(), auth_token__exact=token)

    #Create new password for user
    new_password = request.data.get('new_password')
    user.password = make_password(new_password)
    user.save()

    AuthToken.objects.filter(key=token).delete()

    return Response({'details': 'Password reset successful'})



@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def changeuserdetails(request, token):
    print(request, token)
    user = get_object_or_404(Account, authtoken__exact=token)
    
    data = JSONParser().parse(request)

    u_serializer = UpdateSerializer(instance=user, data=data)

    if u_serializer.is_valid():
        u_serializer.save()
        return Response({"details": "Account details changed successfully"})
    else:
        return Response(u_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




