from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import UserProfile

from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import (
    UserProfile,
    Hospital,
    Bed,
    BloodUnit,
    BloodBank,
)

from .serializers import (
    HospitalSerializer,
    BedSerializer,
    BloodUnitSerializer,
    BloodBankSerializer,
)

# -------------------------
# ROLE BASED REDIRECT
# -------------------------
def redirect_by_role(role):
    if role == "admin":
        return "/admin/"
    elif role == "hospital":
        return "/hospital/dashboard/"
    elif role == "bloodbank":
        return "/bloodbank/dashboard/"
    else:
        return "/search/"


# -------------------------
# API VIEWS (UNCHANGED)
# -------------------------
class HospitalCreateAPIView(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class HospitalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class BedListCreateView(generics.ListCreateAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer


class BedByHospitalListView(generics.ListCreateAPIView):
    serializer_class = BedSerializer

    def get_queryset(self):
        hospital_id = self.kwargs["hospital_id"]
        return Bed.objects.filter(hospital_id=hospital_id)

    def perform_create(self, serializer):
        hospital_id = self.kwargs["hospital_id"]
        serializer.save(hospital_id=hospital_id)


class BloodUnitListCreateView(ListCreateAPIView):
    queryset = BloodUnit.objects.all()
    serializer_class = BloodUnitSerializer


class BloodUnitRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = BloodUnit.objects.all()
    serializer_class = BloodUnitSerializer


class BloodBankListCreateView(generics.ListCreateAPIView):
    queryset = BloodBank.objects.all()
    serializer_class = BloodBankSerializer


# -------------------------
# PAGE VIEWS
# -------------------------
def home(request):
    return render(request, "index.html")


def search(request):
    return render(request, "search.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


# -------------------------
# REGISTER
# -------------------------
@csrf_protect
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if not all([username, email, password, role]):
            messages.error(request, "All fields are required.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        UserProfile.objects.create(
            user=user,
            role=role,
        )

        messages.success(request, "Registration successful. Please login.")
        return redirect("login")

    return render(request, "register.html")


# -------------------------
# LOGIN (ROLE FROM DB ONLY)
# -------------------------
@csrf_protect

def login_view(request):
    if request.method == "POST":
        identifier = request.POST.get("username")  # email OR username
        password = request.POST.get("password")

        if not identifier or not password:
            messages.error(request, "All fields are required.")
            return redirect("login")

        # 🔹 Find user by email OR username
        try:
            user_obj = User.objects.get(email=identifier)
            username = user_obj.username
        except User.DoesNotExist:
            username = identifier  # fallback to username login

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid credentials.")
            return redirect("login")

        try:
            profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            messages.error(request, "User role not found.")
            return redirect("login")

        login(request, user)
        return redirect(redirect_by_role(profile.role))

    return render(request, "login.html")

