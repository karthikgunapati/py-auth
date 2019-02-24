secretKey = "super-secret"
tokenExpirationTimeInHours = 1 

# Database
dataBaseName = "prims"
dataBaseHost = "127.0.0.1"
databasePort = 27017

# email
emailHost = "localhost"
emailPort = 1025
emailPassword = None
fromEmailForOTP = "karthik.g@tectoro.com"
subjectForOTPEmail = "prims verification"

# sms
twilioAccountSid = ""
twilioToken = ""
twilioFromNumber = ""

# templates
OTPTemplate = "OTP for prims account: {otp}"
LinkTemplate = "Link for the prims verification {domain}verify/{payload}"