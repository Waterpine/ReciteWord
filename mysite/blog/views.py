from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.utils import timezone
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from .models import Post
from .models import User
from .models import Four
from .models import Six
from .models import Toefl
from .models import Vocabularysnote
import random


class UserForm(forms.Form):
     username = forms.CharField(label='用户', min_length=6, max_length=50)
     email = forms.EmailField(label='邮箱')
     password = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput())


class WordForm(forms.Form):
    last_id = forms.IntegerField(label='last_id')
    now_id = forms.IntegerField(label='now_id')
    next_id = forms.IntegerField(label='next_id')


class WordNote(forms.Form):
    save_id = forms.IntegerField(label='save_id')


class WordReview(forms.Form):
    start_id = forms.IntegerField(label='start_id')


class WordStart(forms.Form):
    start_id = forms.IntegerField(label='start_id')


class WordDelete(forms.Form):
    delete_id = forms.IntegerField(label='delete_id')


class AnsTrue(forms.Form):
    ans_true = forms.CharField(max_length=10)


class AnsFalse(forms.Form):
    ans_false = forms.CharField(max_length=10)


class StartTest(forms.Form):
    start = forms.CharField(max_length=10)


def test_toefl(request):
    if request.method == 'POST':
        anstrue = AnsTrue(request.POST)
        ansfalse = AnsFalse(request.POST)
        starttest = StartTest(request.POST)
        if starttest.is_valid():
            user = User.objects.filter(already_in=1)[0]
            user.test_toefl = 0
            user.test_number = 0
            user.save()
            testword = Toefl.objects.all()[random.randint(0, Toefl.objects.count())]
        else:
            pass

        if anstrue.is_valid():
            user = User.objects.filter(already_in=1)[0]
            user.test_toefl = user.test_toefl + 10
            user.test_number = user.test_number + 1
            user.save()
            testword = Toefl.objects.all()[random.randint(0, Toefl.objects.count())]
            if user.test_number == 10:
                return render(request, 'blog/pricing.html', {'user': user})
            else:
                pass
        else:
            pass

        if ansfalse.is_valid():
            user = User.objects.filter(already_in=1)[0]
            user.test_toefl = user.test_toefl + 0
            user.test_number = user.test_number + 1
            user.save()
            testword = Toefl.objects.all()[random.randint(0, Toefl.objects.count())]
            if user.test_number == 10:
                return render(request, 'blog/pricing.html', {'user': user})
            else:
                pass
        else:
            pass
    else:
        pass
    return render(request, 'blog/test_toefl.html', {'user': user, 'testword': testword})


def test_six(request):
    if request.method == 'POST':
        anstrue = AnsTrue(request.POST)
        ansfalse = AnsFalse(request.POST)
        starttest = StartTest(request.POST)
        if starttest.is_valid():
            user = User.objects.filter(already_in=1)[0]
            user.test_six = 0
            user.test_number = 0
            user.save()
            testword = Six.objects.all()[random.randint(0, Six.objects.count())]
        else:
            pass

        if anstrue.is_valid():
            user = User.objects.filter(already_in=1)[0]
            user.test_six = user.test_six + 10
            user.test_number = user.test_number + 1
            user.save()
            testword = Six.objects.all()[random.randint(0, Six.objects.count())]
            if user.test_number == 10:
                return render(request, 'blog/pricing.html', {'user': user})
            else:
                pass
        else:
            pass

        if ansfalse.is_valid():
            user = User.objects.filter(already_in=1)[0]
            user.test_six = user.test_six + 0
            user.test_number = user.test_number + 1
            user.save()
            testword = Six.objects.all()[random.randint(0, Six.objects.count())]
            if user.test_number == 10:
                return render(request, 'blog/pricing.html', {'user': user})
            else:
                pass
        else:
            pass
    else:
        pass
    return render(request, 'blog/test_six.html', {'user': user, 'testword': testword})


def test_four(request):
    if request.method == 'POST':
        anstrue = AnsTrue(request.POST)
        ansfalse = AnsFalse(request.POST)
        starttest = StartTest(request.POST)
        if starttest.is_valid():
            user = User.objects.filter(already_in=1)[0]
            user.test_four = 0
            user.test_number = 0
            user.save()
            testword = Four.objects.all()[random.randint(0, Four.objects.count())]
        else:
            pass

        if anstrue.is_valid():
            user = User.objects.filter(already_in=1)[0]
            user.test_four = user.test_four + 10
            user.test_number = user.test_number + 1
            user.save()
            testword = Four.objects.all()[random.randint(0, Four.objects.count())]
            if user.test_number == 10:
                return render(request, 'blog/pricing.html', {'user': user})
            else:
                pass
        else:
            pass

        if ansfalse.is_valid():
            user = User.objects.filter(already_in=1)[0]
            user.test_four = user.test_four + 0
            user.test_number = user.test_number + 1
            user.save()
            testword = Four.objects.all()[random.randint(0, Four.objects.count())]
            if user.test_number == 10:
                return render(request, 'blog/pricing.html', {'user': user})
            else:
                pass
        else:
            pass
    else:
        pass
    return render(request, 'blog/test_four.html', {'user': user, 'testword': testword})


def review_four(request):
    if request.method == 'POST':
        wordform = WordForm(request.POST)
        wordnote = WordNote(request.POST)
        wordreview = WordReview(request.POST)
        if wordform.is_valid():
            user = User.objects.filter(already_in=1)[0]
            if user.number_four == user.review_four:
                return HttpResponse('<script>alert("完成复习");location.href="/review/";</script>')
            user.review_four = user.review_four + 1
            user.save()
            last_id = wordform.cleaned_data["last_id"]
            now_id = wordform.cleaned_data["now_id"] + 1
            next_id = wordform.cleaned_data["next_id"] + 2
            last = Four.objects.filter(id_num=last_id)[0]
            now = Four.objects.filter(id_num=now_id)[0]
            next = Four.objects.filter(id_num=next_id)[0]
            return render(request, 'blog/review_four.html', {'last': last, 'now': now, 'next': next, 'user': user})
        else:
            pass

        if wordnote.is_valid():
            user = User.objects.filter(already_in=1)[0]
            save_id = wordnote.cleaned_data["save_id"]
            save = Four.objects.filter(id_num=save_id)[0]
            live = Vocabularysnote.objects.filter(username=user.username, vocabularys=save.vocabularys)
            if live:
                pass
            else:
                Vocabularysnote.objects.create(username=user.username,\
                                           vocabularys=save.vocabularys,\
                                           paraphrases=save.paraphrases)
                user.note_number = user.note_number + 1
                user.save()
            last = Four.objects.filter(id_num=save_id-1)[0]
            now = Four.objects.filter(id_num=save_id)[0]
            next = Four.objects.filter(id_num=save_id+1)[0]
            return render(request, 'blog/review_four.html', {'last': last, 'now': now, 'next': next, 'user': user})
        else:
            pass

        if wordreview.is_valid():
            user = User.objects.filter(already_in=1)[0]
            if user.number_four == user.review_four:
                return HttpResponse('<script>alert("完成复习");location.href="/review/";</script>')
            start_id = wordreview.cleaned_data["start_id"]
            if start_id >= 1:
                last = Four.objects.filter(id_num=start_id-1)[0]
                now = Four.objects.filter(id_num=start_id)[0]
                next = Four.objects.filter(id_num=start_id+1)[0]
                return render(request, 'blog/review_four.html', {'last': last, 'now': now, 'next': next, 'user': user})
            elif start_id == Four.objects.count():
                last = Four.objects.filter(id_num=start_id - 1)[0]
                now = Four.objects.filter(id_num=start_id)[0]
                return render(request, 'blog/review_four.html', {'last': last, 'now': now, 'user': user})
            else:
                now = Four.objects.filter(id_num=start_id)[0]
                next = Four.objects.filter(id_num=start_id + 1)[0]
                return render(request, 'blog/review_four.html', {'now': now, 'next': next, 'user': user})
        else:
            pass
    else:
        wordform = WordForm()
    return render(request, 'blog/review_four.html', {'wordform': wordform})


def review_six(request):
    if request.method == 'POST':
        wordform = WordForm(request.POST)
        wordnote = WordNote(request.POST)
        wordreview = WordReview(request.POST)
        if wordform.is_valid():
            user = User.objects.filter(already_in=1)[0]
            if user.number_six == user.review_six:
                return HttpResponse('<script>alert("完成复习");location.href="/review/";</script>')
            user.review_six = user.review_six + 1
            user.save()
            last_id = wordform.cleaned_data["last_id"]
            now_id = wordform.cleaned_data["now_id"] + 1
            next_id = wordform.cleaned_data["next_id"] + 2
            last = Six.objects.filter(id_num=last_id)[0]
            now = Six.objects.filter(id_num=now_id)[0]
            next = Six.objects.filter(id_num=next_id)[0]
            return render(request, 'blog/review_six.html', {'last': last, 'now': now, 'next': next, 'user': user})
        else:
            pass

        if wordnote.is_valid():
            user = User.objects.filter(already_in=1)[0]
            save_id = wordnote.cleaned_data["save_id"]
            save = Six.objects.filter(id_num=save_id)[0]
            live = Vocabularysnote.objects.filter(username=user.username, vocabularys=save.vocabularys)
            if live:
                pass
            else:
                Vocabularysnote.objects.create(username=user.username,\
                                           vocabularys=save.vocabularys,\
                                           paraphrases=save.paraphrases)
                user.note_number = user.note_number + 1
                user.save()
            last = Six.objects.filter(id_num=save_id-1)[0]
            now = Six.objects.filter(id_num=save_id)[0]
            next = Six.objects.filter(id_num=save_id+1)[0]
            return render(request, 'blog/review_six.html', {'last': last, 'now': now, 'next': next, 'user': user})
        else:
            pass

        if wordreview.is_valid():
            user = User.objects.filter(already_in=1)[0]
            if user.number_six == user.review_six:
                return HttpResponse('<script>alert("完成复习");location.href="/review/";</script>')
            start_id = wordreview.cleaned_data["start_id"]
            if start_id >= 1:
                last = Six.objects.filter(id_num=start_id-1)[0]
                now = Six.objects.filter(id_num=start_id)[0]
                next = Six.objects.filter(id_num=start_id+1)[0]
                return render(request, 'blog/review_six.html', {'last': last, 'now': now, 'next': next, 'user': user})
            elif start_id == Six.objects.count():
                last = Six.objects.filter(id_num=start_id - 1)[0]
                now = Six.objects.filter(id_num=start_id)[0]
                return render(request, 'blog/review_six.html', {'last': last, 'now': now, 'user': user})
            else:
                now = Six.objects.filter(id_num=start_id)[0]
                next = Six.objects.filter(id_num=start_id + 1)[0]
                return render(request, 'blog/review_six.html', {'now': now, 'next': next, 'user': user})
        else:
            pass
    else:
        wordform = WordForm()
    return render(request, 'blog/review_six.html', {'wordform': wordform})


def review_toefl(request):
    if request.method == 'POST':
        wordform = WordForm(request.POST)
        wordnote = WordNote(request.POST)
        wordreview = WordReview(request.POST)
        if wordform.is_valid():
            user = User.objects.filter(already_in=1)[0]
            if user.number_toefl == user.review_toefl:
                return HttpResponse('<script>alert("完成复习");location.href="/review/";</script>')
            user.review_toefl = user.review_toefl + 1
            user.save()
            last_id = wordform.cleaned_data["last_id"]
            now_id = wordform.cleaned_data["now_id"] + 1
            next_id = wordform.cleaned_data["next_id"] + 2
            last = Toefl.objects.filter(id_num=last_id)[0]
            now = Toefl.objects.filter(id_num=now_id)[0]
            next = Toefl.objects.filter(id_num=next_id)[0]
            return render(request, 'blog/review_toefl.html', {'last': last, 'now': now, 'next': next, 'user': user})
        else:
            pass

        if wordnote.is_valid():
            user = User.objects.filter(already_in=1)[0]
            save_id = wordnote.cleaned_data["save_id"]
            save = Toefl.objects.filter(id_num=save_id)[0]
            live = Vocabularysnote.objects.filter(username=user.username, vocabularys=save.vocabularys)
            if live:
                pass
            else:
                Vocabularysnote.objects.create(username=user.username,\
                                           vocabularys=save.vocabularys,\
                                           paraphrases=save.paraphrases)
                user.note_number = user.note_number + 1
                user.save()
            last = Toefl.objects.filter(id_num=save_id-1)[0]
            now = Toefl.objects.filter(id_num=save_id)[0]
            next = Toefl.objects.filter(id_num=save_id+1)[0]
            return render(request, 'blog/review_toefl.html', {'last': last, 'now': now, 'next': next, 'user': user})
        else:
            pass

        if wordreview.is_valid():
            user = User.objects.filter(already_in=1)[0]
            if user.number_toefl == user.review_toefl:
                return HttpResponse('<script>alert("完成复习");location.href="/review/";</script>')
            start_id = wordreview.cleaned_data["start_id"]
            if start_id >= 1:
                last = Toefl.objects.filter(id_num=start_id-1)[0]
                now = Toefl.objects.filter(id_num=start_id)[0]
                next = Toefl.objects.filter(id_num=start_id+1)[0]
                return render(request, 'blog/review_toefl.html', {'last': last, 'now': now, 'next': next, 'user': user})
            elif start_id == Toefl.objects.count():
                last = Toefl.objects.filter(id_num=start_id - 1)[0]
                now = Toefl.objects.filter(id_num=start_id)[0]
                return render(request, 'blog/review_toefl.html', {'last': last, 'now': now, 'user': user})
            else:
                now = Toefl.objects.filter(id_num=start_id)[0]
                next = Toefl.objects.filter(id_num=start_id + 1)[0]
                return render(request, 'blog/review_toefl.html', {'now': now, 'next': next, 'user': user})
        else:
            pass
    else:
        wordform = WordForm()
    return render(request, 'blog/review_toefl.html', {'wordform': wordform})


def note(request):
    user = User.objects.filter(already_in=1)[0]
    words = Vocabularysnote.objects.filter(username=user.username)
    if request.method == 'POST':
        worddelete = WordDelete(request.POST)
        wordstart = WordStart(request.POST)
        if worddelete.is_valid():
            user.note_number = user.note_number - 1
            now = Vocabularysnote.objects.filter(username=user.username)[user.note_now]
            Vocabularysnote.objects.filter(vocabularys=now.vocabularys).delete()
            user.save()
            if user.note_number == 0:
                return render(request, 'blog/index_after.html', {})
            else:
                if user.note_now >= user.note_number - 1:
                    user.note_now = 0
                    user.save()
                else:
                    user.note_now = user.note_now + 1
                    user.save()
        else:
            pass
        if wordstart.is_valid():
            if user.note_number == 0:
                return render(request, 'blog/index_after.html', {})
            else:
                if user.note_now >= user.note_number - 1:
                    user.note_now = 0
                    user.save()
                else:
                    user.note_now = user.note_now + 1
                    user.save()
        else:
            pass
        now = Vocabularysnote.objects.filter(username=user.username)[user.note_now]
    elif request.method == 'GET':
        if user.note_number == 0:
            return render(request, 'blog/index_after.html', {})
        else:
            user.note_now = 0
            user.save()
            now = Vocabularysnote.objects.filter(username=user.username)[user.note_now]
    return render(request, 'blog/note.html', {'user': user, 'now': now})


def study_toefl(request):
    if request.method == 'POST':
        wordform = WordForm(request.POST)
        wordnote = WordNote(request.POST)
        wordstart = WordStart(request.POST)
        if wordform.is_valid():
            user = User.objects.filter(already_in=1)[0]
            user.number_toefl = user.number_toefl + 1
            user.save()
            last_id = wordform.cleaned_data["last_id"]
            now_id = wordform.cleaned_data["now_id"] + 1
            next_id = wordform.cleaned_data["next_id"] + 2
            last = Toefl.objects.filter(id_num=last_id)[0]
            now = Toefl.objects.filter(id_num=now_id)[0]
            next = Toefl.objects.filter(id_num=next_id)[0]
            return render(request, 'blog/study_toefl.html', {'last': last, 'now': now, 'next': next, 'user': user})
        else:
            pass

        if wordnote.is_valid():
            user = User.objects.filter(already_in=1)[0]
            save_id = wordnote.cleaned_data["save_id"]
            save = Toefl.objects.filter(id_num=save_id)[0]
            live = Vocabularysnote.objects.filter(username=user.username, vocabularys=save.vocabularys)
            if live:
                pass
            else:
                Vocabularysnote.objects.create(username=user.username,\
                                           vocabularys=save.vocabularys,\
                                           paraphrases=save.paraphrases)
                user.note_number = user.note_number + 1
                user.save()
            last = Toefl.objects.filter(id_num=save_id-1)[0]
            now = Toefl.objects.filter(id_num=save_id)[0]
            next = Toefl.objects.filter(id_num=save_id+1)[0]
            return render(request, 'blog/study_toefl.html', {'last': last, 'now': now, 'next': next, 'user': user})
        else:
            pass

        if wordstart.is_valid():
            user = User.objects.filter(already_in=1)[0]
            start_id = wordstart.cleaned_data["start_id"]
            if start_id >= 1:
                last = Toefl.objects.filter(id_num=start_id-1)[0]
                now = Toefl.objects.filter(id_num=start_id)[0]
                next = Toefl.objects.filter(id_num=start_id+1)[0]
                return render(request, 'blog/study_toefl.html', {'last': last, 'now': now, 'next': next, 'user': user})
            elif start_id == Four.objects.count():
                last = Toefl.objects.filter(id_num=start_id - 1)[0]
                now = Toefl.objects.filter(id_num=start_id)[0]
                return render(request, 'blog/study_toefl.html', {'last': last, 'now': now, 'user': user})
            else:
                now = Toefl.objects.filter(id_num=start_id)[0]
                next = Toefl.objects.filter(id_num=start_id + 1)[0]
                return render(request, 'blog/study_toefl.html', {'now': now, 'next': next, 'user': user})
        else:
            pass
    else:
        wordform = WordForm()
    return render(request, 'blog/study_toefl.html', {'wordform': wordform})


def study_six(request):
    if request.method == 'POST':
        wordform = WordForm(request.POST)
        wordnote = WordNote(request.POST)
        wordstart = WordStart(request.POST)
        if wordform.is_valid():
            user = User.objects.filter(already_in=1)[0]
            user.number_six = user.number_six + 1
            user.save()
            last_id = wordform.cleaned_data["last_id"]
            now_id = wordform.cleaned_data["now_id"] + 1
            next_id = wordform.cleaned_data["next_id"] + 2
            last = Six.objects.filter(id_num=last_id)[0]
            now = Six.objects.filter(id_num=now_id)[0]
            next = Six.objects.filter(id_num=next_id)[0]
            return render(request, 'blog/study_six.html', {'last': last, 'now': now, 'next': next, 'user': user})
        else:
            pass

        if wordnote.is_valid():
            user = User.objects.filter(already_in=1)[0]
            save_id = wordnote.cleaned_data["save_id"]
            save = Six.objects.filter(id_num=save_id)[0]
            live = Vocabularysnote.objects.filter(username=user.username, vocabularys=save.vocabularys)
            if live:
                pass
            else:
                Vocabularysnote.objects.create(username=user.username,\
                                           vocabularys=save.vocabularys,\
                                           paraphrases=save.paraphrases)
                user.note_number = user.note_number + 1
                user.save()
            last = Six.objects.filter(id_num=save_id-1)[0]
            now = Six.objects.filter(id_num=save_id)[0]
            next = Six.objects.filter(id_num=save_id+1)[0]
            return render(request, 'blog/study_six.html', {'last': last, 'now': now, 'next': next, 'user': user})
        else:
            pass

        if wordstart.is_valid():
            user = User.objects.filter(already_in=1)[0]
            start_id = wordstart.cleaned_data["start_id"]
            if start_id >= 1:
                last = Six.objects.filter(id_num=start_id-1)[0]
                now = Six.objects.filter(id_num=start_id)[0]
                next = Six.objects.filter(id_num=start_id+1)[0]
                return render(request, 'blog/study_six.html', {'last': last, 'now': now, 'next': next, 'user': user})
            elif start_id == Six.objects.count():
                last = Six.objects.filter(id_num=start_id - 1)[0]
                now = Six.objects.filter(id_num=start_id)[0]
                return render(request, 'blog/study_six.html', {'last': last, 'now': now, 'user': user})
            else:
                now = Six.objects.filter(id_num=start_id)[0]
                next = Six.objects.filter(id_num=start_id + 1)[0]
                return render(request, 'blog/study_six.html', {'now': now, 'next': next, 'user': user})
        else:
            pass
    else:
        wordform = WordForm()
    return render(request, 'blog/study_six.html', {'wordform': wordform})


def study(request):
    if request.method == 'POST':
        wordform = WordForm(request.POST)
        wordnote = WordNote(request.POST)
        wordstart = WordStart(request.POST)
        if wordform.is_valid():
            user = User.objects.filter(already_in=1)[0]
            user.number_four = user.number_four + 1
            user.save()
            last_id = wordform.cleaned_data["last_id"]
            now_id = wordform.cleaned_data["now_id"] + 1
            next_id = wordform.cleaned_data["next_id"] + 2
            last = Four.objects.filter(id_num=last_id)[0]
            now = Four.objects.filter(id_num=now_id)[0]
            next = Four.objects.filter(id_num=next_id)[0]
            return render(request, 'blog/study.html', {'last': last, 'now': now, 'next': next, 'user':user})
        else:
            pass

        if wordnote.is_valid():
            user = User.objects.filter(already_in=1)[0]
            save_id = wordnote.cleaned_data["save_id"]
            save = Four.objects.filter(id_num=save_id)[0]
            live = Vocabularysnote.objects.filter(username=user.username, vocabularys=save.vocabularys)
            if live:
                pass
            else:
                Vocabularysnote.objects.create(username=user.username,\
                                           vocabularys=save.vocabularys,\
                                           paraphrases=save.paraphrases)
                user.note_number = user.note_number + 1
                user.save()
            last = Four.objects.filter(id_num=save_id-1)[0]
            now = Four.objects.filter(id_num=save_id)[0]
            next = Four.objects.filter(id_num=save_id+1)[0]
            return render(request, 'blog/study.html', {'last': last, 'now': now, 'next': next, 'user': user})
        else:
            pass

        if wordstart.is_valid():
            user = User.objects.filter(already_in=1)[0]
            start_id = wordstart.cleaned_data["start_id"]
            if start_id >= 1:
                last = Four.objects.filter(id_num=start_id-1)[0]
                now = Four.objects.filter(id_num=start_id)[0]
                next = Four.objects.filter(id_num=start_id+1)[0]
                return render(request, 'blog/study.html', {'last': last, 'now': now, 'next': next, 'user': user})
            elif start_id == Four.objects.count():
                last = Four.objects.filter(id_num=start_id - 1)[0]
                now = Four.objects.filter(id_num=start_id)[0]
                return render(request, 'blog/study.html', {'last': last, 'now': now, 'user': user})
            else:
                now = Four.objects.filter(id_num=start_id)[0]
                next = Four.objects.filter(id_num=start_id + 1)[0]
                return render(request, 'blog/study.html', {'now': now, 'next': next, 'user': user})
        else:
            pass
    else:
        wordform = WordForm()
        #return HttpResponse('<script>alert("没有收到post");location.href="/";</script>')
    return render(request, 'blog/study.html', {'wordform':wordform})


def index_after(request):
    user = User.objects.filter(already_in=1)[0]
    return render(request, 'blog/index_after.html', {'user': user})


def review(request):
    four_count = Four.objects.count()
    six_count = Six.objects.count()
    toefl_count = Toefl.objects.count()
    user = User.objects.filter(already_in=1)[0]
    return render(request, 'blog/features_review.html', {'four_count': four_count, 'six_count': six_count,\
                                                         'toefl_count': toefl_count, 'user': user})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def download(request):
    return render(request, 'blog/download.html', {})


def features(request):
    four_count = Four.objects.count()
    six_count = Six.objects.count()
    toefl_count = Toefl.objects.count()
    user = User.objects.filter(already_in=1)[0]
    return render(request, 'blog/features.html', {'four_count': four_count, 'six_count': six_count,\
                                                  'toefl_count': toefl_count, 'user': user})
    #return render_to_response('blog/features.html', locals())


def index(request):
    return render(request, 'blog/index.html', {})


def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            user = User.objects.filter(username=username, password=password, email=email)
            if user:
                last = User.objects.filter(already_in=1)
                if last:
                    last = User.objects.filter(already_in=1)[0]
                    last.already_in = 0
                    last.save()
                else:
                    pass
                user_a = User.objects.filter(username=username)[0]
                user_a.already_in = 1
                user_a.save()
                return render(request, 'blog/index_after.html', {'userform': userform, 'user': user})
            else:
                return HttpResponse('<script>alert("用户名或者密码错误");location.href="/";</script>')
    else:
        userform = UserForm()
    return render(request, 'blog/login.html', {'userform': userform})


def pricing(request):
    user = User.objects.filter(already_in=1)[0]
    return render(request, 'blog/pricing.html', {'user': user})


def signup(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            userinfoemail = User.objects.filter(email=email)
            userinfoname = User.objects.filter(username=username)
            if userinfoemail.exists() and userinfoname.exists():
                return HttpResponse('<script>alert("用户名或者邮箱已经存在");location.href="/signup/";</script>')
            else:
                User.objects.create(username=username, password=password, email=email,\
                                    number_four=0, number_six=0, number_toefl=0,\
                                    test_four=0, test_six=0, test_toefl=0,\
                                    review_four=0, review_six=0, review_toefl=0, already_in=0,\
                                    note_now=0, note_number=0, test_number=0)
                return HttpResponse('<script>alert("注册成功");location.href="/login/";</script>')
        else:
            return HttpResponse('<script>alert("注册失败");location.href="/signup";</script>')
    else:
        userform = UserForm()
    return render(request, 'blog/signup.html', {'userform': userform})


def blog(request):
    return render(request, 'blog/blog.html', {})


