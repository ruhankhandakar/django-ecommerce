from django.shortcuts import render
import random


def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr[i] for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(length))


print(generate_session_token())
