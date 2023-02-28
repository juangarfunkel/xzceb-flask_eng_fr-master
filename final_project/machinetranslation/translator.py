"""
This module provides functions to translate text using IBM Watson Language Translator API.
"""
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(API_KEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)
LANGUAGE_TRANSLATOR.set_service_url(URL)

def english_to_french(english_text):
    """
    Translates English text to French using IBM Watson Language Translator API.
    """
    if not english_text:
        return None

    translation_response = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    french_text = translation_response.get('translations', [{}])[0].get('translation', '').strip()
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English using IBM Watson Language Translator API.
    """
    if not french_text:
        return None

    translation_response = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()

    english_text = translation_response.get('translations', [{}])[0].get('translation', '').strip()
    return english_text
