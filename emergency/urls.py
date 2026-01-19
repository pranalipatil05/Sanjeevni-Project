from django.urls import path
from .views import (
    home,
    search,
    about,
    contact,
    login_view,
    register_view,

    HospitalCreateAPIView,
    HospitalRetrieveUpdateDestroyAPIView,
    BedListCreateView,
    BedByHospitalListView,
    BloodUnitListCreateView,
    BloodUnitRetrieveUpdateView,
    BloodBankListCreateView,
)

urlpatterns = [
    # PAGES
    path("", home, name="home"),                 # /
    path("search/", search, name="search"),      # /search/
    path("about/", about, name="about"),         # /about/
    path("contact/", contact, name="contact"),   # /contact/
    path("login/", login_view, name="login"),    # /login/
    path("register/", register_view, name="register"),  # /register/

    # APIs
    path("hospitals/", HospitalCreateAPIView.as_view(), name="hospital-list"),
    path("hospitals/<int:pk>/", HospitalRetrieveUpdateDestroyAPIView.as_view(), name="hospital-detail"),

    path("beds/", BedListCreateView.as_view(), name="bed-list"),
    path("hospitals/<int:hospital_id>/beds/", BedByHospitalListView.as_view(), name="beds-by-hospital"),

    path("blood/", BloodUnitListCreateView.as_view(), name="blood-list-create"),
    path("blood/<int:pk>/", BloodUnitRetrieveUpdateView.as_view(), name="blood-detail"),

    path("bloodbanks/", BloodBankListCreateView.as_view(), name="bloodbank-list-create"),
]

