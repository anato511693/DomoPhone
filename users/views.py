from django.shortcuts import render
from django.http import HttpResponse
from users.models import *
from own.models import *
from users.settings import *
from settings.models import *
from users.templates.users.run_db import *
from modules.Finger.DB import * ###
import json

def index(request):
    if not request.GET:
        contact = Contact.objects.filter()
        rfid = Rfid.objects.filter()
        rf = RF.objects.filter()
        finger = Finger.objects.filter()
        return render(request, 'users/users.html', locals())

def user_owned(request):
    if request.GET and "user" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]
        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        return render(request, 'users/includes/own_user.html', locals())
    else:
        pass

def all_owned(request):
    if request.GET and "all" == request.GET["cmd"]:
        contact = Contact.objects.filter()
        rfid = Rfid.objects.filter()
        rf = RF.objects.filter()
        finger = Finger.objects.filter()

        return render(request, 'users/includes/info_all.html', locals())
    else:
        pass

def rfid_owned(request):

    if request.GET and "delete" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[5:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        del_rfid = Rfid.objects.get(id = index)
        del_rfid.delete()

        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "activ" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[11:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        rfid_id = Rfid.objects.get(id = index)
        if rfid_id.activ:
            rfid_id.activ = False
        else:
            rfid_id.activ = True
        rfid_id.save()

        return render(request, 'users/includes/own_user.html', locals())


    elif request.GET and "add_stop" == request.GET["cmd"]:
        status = My_variable.objects.get(name = "rfid_status")
        status.value = "no"
        status.save()

        return HttpResponse("Отменено")

    elif request.GET and "add_start" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]

        user_rfid = My_variable.objects.get(name = "rfid_user")
        user_rfid.value = user
        user_rfid.save()
        status = My_variable.objects.get(name = "rfid_status")
        status.value = "add"
        status.save()
        return HttpResponse("Поднесите RFID метку к считывателю")

    elif request.GET and "add_check" == request.GET["cmd"]:
        info = My_variable.objects.get(name = "rfid_print")
        status = My_variable.objects.get(name = "rfid_status")
        if status.value == "add":
            #return json.dumps({'cmd': "add"})
            return HttpResponse('{"cmd": "add"}')
            #return HttpResponse("add")
        elif status.value == "add_no":
            My_variable.objects.get(name = "rfid_print")
            #return json.dumps({'cmd': "add_no", 'data': info.value})
            #HttpResponse(My_variable.objects.get(name = "print"))
            return HttpResponse('{"cmd": "add_no", "data": "' + info.value + '"}')
        else:
            user = request.GET["user"]
            user = user[5:]

            contact = Contact.objects.get(id = user)
            rfid = Rfid.objects.filter(contact = user)
            rf = RF.objects.filter(contact = user)
            finger = Finger.objects.filter(contact = user)

            #return render(request, 'users/includes/own_user.html', locals())
            return HttpResponse('{"cmd": "add_off"}')

    else:
        pass

def rf_owned(request):
    if request.GET and "delete" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[3:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        del_rf = RF.objects.get(id = index)
        del_rf.delete()

        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "activ" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[9:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        rf_id = RF.objects.get(id = index)
        if rf_id.activ:
            rf_id.activ = False
        else:
            rf_id.activ = True
        rf_id.save()

        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "add" == request.GET["cmd"]:
        user = request.GET["user"]
        mom = request.session.get('num')
        return HttpResponse(mom)

    elif request.GET and "add_open" == request.GET["cmd"]:
        up = My_variable.objects.get(name = "rf_up")
        down = My_variable.objects.get(name = "rf_down")
        up.value = 0000000000
        down.value = 0000000000
        up.save()
        down.save()
        return HttpResponse("ok")

    elif request.GET and "add_cancel" == request.GET["cmd"]:
        status = My_variable.objects.get(name = "rf_status")
        status.value = "no"
        status.save()
        return HttpResponse("ok")

    elif request.GET and "rec_up" == request.GET["cmd"]:
        user = request.GET["user"]
        mom = request.session.get('num')

        status = My_variable.objects.get(name = "rf_status")
        status.value = "rec_up"
        status.save()

        return HttpResponse("Нажмите на кнопку брелка рядом с приемником")

    elif request.GET and "rec_down" == request.GET["cmd"]:
        user = request.GET["user"]
        mom = request.session.get('num')

        status = My_variable.objects.get(name = "rf_status")
        status.value = "rec_down"
        status.save()

        return HttpResponse("Нажмите на кнопку брелка рядом с приемником")

    elif request.GET and "rec_check" == request.GET["cmd"]:

        status = My_variable.objects.get(name = "rf_status")
        if status.value == "rec_up" or status.value == "rec_down":
            return HttpResponse('{"cmd": "rec"}')
        elif status.value == "rec_no":
            code = My_variable.objects.get(name = "rf_print")
            return HttpResponse('{"cmd": "rec_no", "data": "' + code.value + '"}')
        elif status.value == "rec_up_yes":
            code = My_variable.objects.get(name = "rf_up")
            return HttpResponse('{"cmd": "rec_up_yes", "data": "OK", "code": "' + code.value + '"}')
        elif status.value == "rec_down_yes":
            code = My_variable.objects.get(name = "rf_down")
            return HttpResponse('{"cmd": "rec_down_yes", "data": "OK", "code": "' + code.value + '"}')
        elif status.value == "add_yes":
            code = My_variable.objects.get(name = "rf_status")
            return HttpResponse('{"cmd": "add_yes", "data": "' + info.value + '"}')
        else:
            return HttpResponse('{"cmd": "no"}')

    else:
        pass

def finger_owned(request):
    if request.GET and "delete" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[7:]

        finger_position = My_variable.objects.get(name = "finger_position")
        finger_position.value = index
        finger_position.save()
        Save_status("delete")
        time.sleep(0.5)

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)
        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "activ" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[13:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        finger_id = Finger.objects.get(id = index)
        if finger_id.activ:
            finger_id.activ = False
        else:
            finger_id.activ = True
        finger_id.save()
        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "add_start" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]

        user_finger = My_variable.objects.get(name = "finger_user")
        user_finger.value = user
        user_finger.save()
        Save_status("add")
        Save_step("wait")


        return HttpResponse("Подождите...")

    elif request.GET and "add_check" == request.GET["cmd"]:
        #info = My_variable.objects.get(name = "finger_print")
        if Check_status("add"):
            if Check_step("wait"):
                return HttpResponse('{"cmd":"add", "step": "wait", "data": "Подождите..."}')
            elif Check_step("wait_1"):
                return HttpResponse('{"cmd":"add", "step": "wait_1", "data": "Прикладите палец"}')
            elif Check_step("remove"):
                return HttpResponse('{"cmd":"add", "step": "remove", "data": "Уберите палец"}')
            elif Check_step("wait_2"):
                return HttpResponse('{"cmd":"add", "step": "wait_2", "data": "Сново прикладите палец"}')
            else:
                step = My_variable.objects.get(name = "finger_step")
                status = My_variable.objects.get(name = "finger_status")
                return HttpResponse('{"cmd":"hz", "step": "' + step.value + '", "status": "' + status.value + '"}')
        elif Check_status("no"):
            if Check_step("exists"):
                return HttpResponse('{"cmd":"add", "step": "exists", "data": "Этот палец существует"}')
            elif Check_step("not_match"):
                return HttpResponse('{"cmd":"add", "step": "not_match", "data": "Пальци не совпадают"}')
            elif Check_step("add"):
                return HttpResponse('{"cmd":"add", "step": "not_match", "data": "Палец добавлен"}')
            elif Check_step("time"):
                return HttpResponse('{"cmd":"add", "step": "add", "data": "Время Вышло"}')
            elif Check_step("full"):
                return HttpResponse('{"cmd":"add", "step": "add", "data": "База заполнена"}')
            elif Check_step("error"):
                return HttpResponse('{"cmd":"add", "step": "add", "data": "Произошла ошибка"}')
            else:
                step = My_variable.objects.get(name = "finger_step")
                status = My_variable.objects.get(name = "finger_status")
                return HttpResponse('{"cmd":"hz", "step": "' + step.value + '", "status": "' + status.value + '"}')
        else:
            return HttpResponse('{"cmd": "add_off"}')


    elif request.GET and "add_cancel" == request.GET["cmd"]:
        status = My_variable.objects.get(name = "finger_status")
        step = My_variable.objects.get(name = "finger_step")
        Save_status("no")
        Save_step("cancel")
        user = request.GET["user"]
        user = user[5:]
        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        return render(request, 'users/includes/own_user.html', locals())


    else:
        pass


def Run_rfid(request):
    if request.GET and "start" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]
        RunStart(user, "rfid", "rec", "no")
        return HttpResponse("Поднесите RFID метку к считывателю")
    elif request.GET and "stop" == request.GET["cmd"]:
        RunStop()
        return HttpResponse("Отменено")

    elif request.GET and "delete" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[5:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        RunDelete("rfid", index)

        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "activ" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[11:]

        RunActiv("rfid", index)
        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "check" == request.GET["cmd"]:
        info = My_variable.objects.get(name = "rfid_print")
        status = My_variable.objects.get(name = "rfid_status")
        if status.value == "rec":
            return HttpResponse('{"cmd": "rec"}')
        elif status.value == "no":
            return HttpResponse('{"cmd": "no", "data": "' + RunRead() + '"}')
        elif status.value == "time":
            return HttpResponse('{"cmd": "time"}')
        elif status.value == "save":
            return HttpResponse('{"cmd": "save"}')
        else:
            return HttpResponse('{"cmd": "xxx"}')

def Run_rf(request):
    if request.GET and "open" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]
        RunStart(user, "rf", "open", "no")
        return HttpResponse("ok")
    elif request.GET and "stop" == request.GET["cmd"]:
        RunStop()
        return HttpResponse("Отменено")
    elif request.GET and "up" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]
        RunStart(user, "rf", "up", "no")
        return HttpResponse("Нажмите на кнопку брелка рядом с приемником")
    elif request.GET and "down" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]
        RunStart(user, "rf", "down", "no")
        return HttpResponse("Нажмите на кнопку брелка рядом с приемником")
    elif request.GET and "activ" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[11:]
        RunActiv("rf", index)
        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)
        return render(request, 'users/includes/own_user.html', locals())
    elif request.GET and "check" == request.GET["cmd"]:
        info = My_variable.objects.get(name = "rfid_print")
        status = My_variable.objects.get(name = "rfid_status")
        if status.value == "rec":
            return HttpResponse('{"cmd": "rec"}')
        elif status.value == "no":
            return HttpResponse('{"cmd": "no", "data": "' + RunRead() + '"}')
        elif status.value == "time":
            return HttpResponse('{"cmd": "time"}')
        elif status.value == "save":
            return HttpResponse('{"cmd": "save"}')
        else:
            return HttpResponse('{"cmd": "xxx"}')
