
register_args = [
            {
                "name": "first_name",
                "type": str,
                "required": True,
                "location": "json"
            },
            {
                "name": "last_name",
                "type": str,
                "required": True,
                "location": "json"
            },
            {
                "name": "email_id",
                "type": str,
                "required": True,
                "location": "json"
            },
            {
                "name": "password",
                "type": str,
                "required": True,
                "location": "json"
            },
            {
                "name": "phone_num",
                "type": str,
                "location": "json"
            },
            {
                "name": "company_name",
                "type": str,
                "location": "json"
            },
            {
                "name": "trail",
                "type": bool,
                "location": "json"
            },
            {
                "name": "valid_until",
                "type": str,
                "default": None,
                "location": "json"
            }
        ]

link_generate_args = [
    {
        "name": "user_id",
        "type": str,
        "required": True,
        "location": "json"
    }
]

otp_generate_args = [
    {
        "name": "user_id",
        "type": str,
        "required": True,
        "location": "json"
    }
]

otp_verify_args = [
    {
        "name": "user_id",
        "type": str,
        "required": True,
        "location": "json"
    },
    {
        "name": "otp",
        "type": str,
        "required": True,
        "location": "json"
    }
]