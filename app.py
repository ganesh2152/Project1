import streamlit as st
import pandas as pd
import requests

def fetch_users():
    response = requests.get('https://randomuser.me/api/?results=20')
    return response.json()['results']

def transform_users(data):
    users = []
    for user in data:
        users.append({
            'name': f"{user['name']['first']} {user['name']['last']}",
            'email': user['email'],
            'city': user['location']['city'],
            'country': user['location']['country']
        })
