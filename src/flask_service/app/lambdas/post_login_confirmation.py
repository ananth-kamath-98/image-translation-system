import time

from app.models.user_profile import UserProfileModel

user_profile = UserProfileModel()


def handler(event, context):
    if event["triggerSource"] == "PostConfirmation_ConfirmSignUp":
        user_attrs = event["request"]["userAttributes"]
        user_id = user_attrs["sub"]
        email = user_attrs.get("email", "")
        created = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        user_profile.upsert_profile(user_id, email, created)

    return event
