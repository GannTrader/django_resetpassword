from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
# app_name = 'account'

urlpatterns = [
    path('login/', views.loginUser),
    path('postloginUser/', views.postloginUser, name = 'postloginUser'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name = 'password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),

]

# - user nhập email để lấy lại mật khẩu
# - kiểm tra email có tồn tại trong hệ thống ?
# - nếu gmail tồn tại thì gửi 1 link có token vào gmail user
# - user click vào link đó
# - hệ thống kiểm tra xem link đó có đúng token trong hệ thống tạo ra ?
# - nếu đúng thì chuyển đến trang nhập lại mật khẩu
# - nếu mk trùng khớp thì update mới vào hệ thống
# - chuyển đến trang đăng nhập user

# from django.contrib.auth import views as auth_views
# ==================url==============name_url====
# password_reset/ [name='password_reset']
# password_reset/done/ [name='password_reset_done']
# reset/<uidb64>/<token>/ [name='password_reset_confirm']
# reset/done/ [name='password_reset_complete']

# --class and url name --
# PasswordResetView
# URL name: password_reset

# PasswordResetDoneView
# URL name: password_reset_done

# PasswordResetConfirmView
# URL name: password_reset_confirm

# PasswordResetCompleteView
# URL name: password_reset_complete