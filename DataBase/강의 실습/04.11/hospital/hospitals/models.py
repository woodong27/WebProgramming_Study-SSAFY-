from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.TextField()
    
    def __str__(self):
        return f'전문의 : {self.name}'

# ManyToManyField를 사용해서 M:N관계 형성
# through옵션을 사용해서 Django의 기본 중개 테이블 대신 직접 만든 중개 테이블 사용
class Patient(models.Model):
    doctors=models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
    name=models.TextField()
    
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
    
# 중개 테이블
class Reservation(models.Model):
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom=models.TextField()
    reserved_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
    
# 중개 모델 : ForeignKey로 예약을 관리하는 테이블을 새로 생성
# class Reservation(models.Model):
#     doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'