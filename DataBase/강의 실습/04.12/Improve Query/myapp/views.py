from django.shortcuts import render
from .models import PetSitter, Pet
from django.db import connection, reset_queries 

# Create your views here.
# 데코레이터 작성
def get_sql_queries(origin_func):
    def wrapper(*args, **kwargs):
        reset_queries()
        
        origin_func()
        
        query_info=connection.queries
        for query in query_info:
            print(query['sql'])
    
    return wrapper

@get_sql_queries
def get_pet_data():
    # reset_queries()
    pets=Pet.objects.all().select_related('pet_sitter')
    for pet in pets:
        print(f'{pet.name} | 집사 : {pet.pet_sitter.first_name}')
    # query_info=connection.queries
    # for query in query_info:
    #     print(query['sql'])