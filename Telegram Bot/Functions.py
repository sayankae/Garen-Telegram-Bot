from ibm_watson import LanguageTranslatorV3, language_translator_v3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

URL_Name = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/bfc87c9c-ab72-4749-95de-76a9a24079e8"
apikey_it = "qi2KY22Wm8jKZXmmeeMAlA8cQdUmUmpYyFiyADoJOG-8"


authenticator = IAMAuthenticator(apikey_it)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL_Name)

def translating(input_text):
    translation_response = language_translator.translate(text = input_text ,model_id='en-bn')
    translation  = translation_response.get_result()
    language_translated = translation["translations"][0]["translation"]
    return language_translated
