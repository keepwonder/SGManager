from wtforms import Form, StringField, PasswordField
from  wtforms.validators import InputRequired, Length, Email, DataRequired, EqualTo


class LoginForm(Form):
    """
    登录验证表单
    """
    username = StringField(validators=[InputRequired(message='请输入用户名')])
    password = StringField(validators=[InputRequired(message='请输入密码'), Length(6, 20, message='密码长度不对')])
    remember = StringField()


class RegistrationForm(Form):
    """
    注册验证表单
    """
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm = PasswordField('confirm', validators=[DataRequired(), EqualTo('password', message='密码必须保持一致')])
    email = StringField('email', validators=[DataRequired(), Email()])
    phone = StringField('phone', validators=[DataRequired(), Length(min=11, max=11)])
