from .models import SMSVerificationCode


def send_sms_verification_code(number): 
    # TODO: нужен внешний sms шлюз
    print(f"Sending SMS code to {number}")
    return '0000'

def create_verification_code(number):
    code = send_sms_verification_code(number)
    SMSVerificationCode.objects.create(phone_number=number, code=code)

def verificate_code(number, code):
    sms_verification_code = SMSVerificationCode.objects.filter(phone_number=number).first()
    if not sms_verification_code:
        return False
    return sms_verification_code.code == code