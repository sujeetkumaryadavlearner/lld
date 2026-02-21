
import copy


class Emailtemplate:
    def clone(self):
        return copy.deepcopy(self)
    
    def set_content(self,content):
        self.content=content    
    
    def set_subject(self,subject):
        self.subject=subject


class WelcomeEmail(Emailtemplate):
    def __init__(self):
        self.subject="Welcome to our service!"
        self.content="Dear user, thank you for joining our service. We are excited to have you on board."
    def set_content(self,content):
        self.content=content+" Please let us know if you have any questions."
    def set_subject(self,subject):
        self.subject=subject+" - Welcome"


    
class PasswordResetEmail(Emailtemplate):
    def __init__(self):
        self.subject="Password Reset Request"
        self.content="Dear user, we received a request to reset your password. Please click the link below to proceed."
    def set_content(self,content):
        self.content=content+" If you did not request a password reset, please ignore this email."
    def set_subject(self,subject):
        self.subject=subject+" - Password Reset"

class email_registry:
    templates={"welcome":WelcomeEmail(),"password_reset":PasswordResetEmail()}
    @staticmethod
    def get_template(template_name):
        template=email_registry.templates.get(template_name)
        if template:
            return template.clone()
        else:
            raise ValueError(f"Template '{template_name}' not found in registry.")