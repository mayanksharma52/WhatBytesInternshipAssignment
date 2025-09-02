from django.urls import path
from .views import (
    PatientListCreateView,
    PatientRetrieveUpdateDeleteView,
    PatientDoctorMappingListCreateView,
    PatientDoctorMappingByPatientView,
    PatientDoctorMappingDeleteView
)

urlpatterns = [
    path('', PatientListCreateView.as_view(), name='patient-list-create'),
    path('<int:pk>/', PatientRetrieveUpdateDeleteView.as_view(), name='patient-detail'),
    path('mappings/', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:patient_id>/', PatientDoctorMappingByPatientView.as_view(), name='mapping-by-patient'),
    path('mappings/delete/<int:pk>/', PatientDoctorMappingDeleteView.as_view(), name='mapping-delete'),
]