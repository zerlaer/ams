# Create your views here.
from django.shortcuts import render, redirect

from assets.models import Computer, SipPhone, Telephone
from users.models import User


# 首页
def index(request):
    return render(request, 'index.html')


def dashboard(request):
    com_total = Computer.objects.count()
    com_upline = Computer.objects.filter(com_status=0).count()
    com_offline = Computer.objects.filter(com_status=1).count()
    com_backup = Computer.objects.filter(com_status=2).count()
    com_break = Computer.objects.filter(com_status=3).count()
    upline_rate = round(com_upline / com_total * 100)
    offline_rate = round(com_offline / com_total * 100)
    backup_rate = round(com_backup / com_total * 100)
    break_rate = round(com_break / com_total * 100)
    sip_total = SipPhone.objects.count()
    tel_total = Telephone.objects.count()
    return render(request, 'dashboard/dashboard.html')


def register(request):
    # 判断是否为GET
    if request.method == "GET":
        # 获取数据库数据

        return render(request, 'dashboard/dashboard.html', {"data": db})
    # 判断是否为POST
    elif request.method == "POST":
        # 接受参数
        username = request.POST.get("username")
        domain = request.POST.get("domain")
        mobile = request.POST.get("mobile")
        tel = request.POST.get("tel")
        headset = request.POST.get("headset")
        date = request.POST.get("date")
        # 判断参数是否为空
        if username != "" and domain != "" and mobile != "" and tel != "" and headset != "" and date != "":
            # 链接数据库
            db = User()
            db.username = username
            db.domain = domain
            db.mobile = mobile
            db.tel = tel
            db.headset = headset
            db.date = date
            db.save()
            return redirect("/register/")

        else:
            db = User.objects.all()
            return render(request, "register/register.html", {"error": "登记信息不能为空哦", "data": db})

    else:
        return redirect("/")


def getassets(request):
    # 判断是否为GET
    if request.method == "GET":
        # 获取数据库数据
        db = User.objects.all()
        return render(request, 'getassets/getassets.html', {"data": db})
    # 判断是否为POST
    elif request.method == "POST":
        # 接受参数
        username = request.POST.get("username")
        domain = request.POST.get("domain")
        mobile = request.POST.get("mobile")
        tel = request.POST.get("tel")
        headset = request.POST.get("headset")
        date = request.POST.get("date")
        # 判断参数是否为空
        if username != "" and domain != "" and mobile != "" and tel != "" and headset != "" and date != "":
            # 链接数据库
            db = User()
            db.username = username
            db.domain = domain
            db.mobile = mobile
            db.tel = tel
            db.headset = headset
            db.date = date
            db.save()
            return redirect("/getassets/")

        else:
            db = User.objects.all()
            return render(request, "getassets/getassets.html", {"error": "登记信息不能为空哦", "data": db})

    else:
        return redirect("/")
