from django.http import request
from django.shortcuts import render, redirect
from django.http.response import HttpResponse

def lead(requestm, key):
    
    return HttpResponse(key)