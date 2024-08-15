from fastapi_users.authentication import BearerTransport

bearer_transport = BearerTransport(
    # TODO: update url
    token_url="auth/jwt/login",
)