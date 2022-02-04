# flake8: noqa

"""
    Bundesagentur für Arbeit: Weiterbildungssuche API

    Eine der größten Weiterbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** 38053956-6618-4953-b670-b4ae7a2360b1  **ClientSecret:** c385073c-3b97-42a9-b916-08fd8a5d1795.   **Achtung**: der generierte Token muss bei folgenden GET-requests im header als 'OAuthAccessToken' inkludiert werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


__version__ = "0.1.0"

# import ApiClient
from deutschland.weiterbildungssuche.api_client import ApiClient

# import Configuration
from deutschland.weiterbildungssuche.configuration import Configuration

# import exceptions
from deutschland.weiterbildungssuche.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)
