# Generated by Django 3.0.3 on 2020-03-11 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='연락처')),
                ('major', models.CharField(blank=True, max_length=255, null=True, verbose_name='전공')),
                ('semester', models.IntegerField(default=1, verbose_name='누적학기')),
                ('interview_date', models.CharField(choices=[('WED', '25(수)'), ('THUR', '26(목)'), ('FRI', '27(금)')], default='1', max_length=20, verbose_name='희망 면접 날짜')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.TextField(blank=True, null=True, verbose_name='질문1')),
                ('q2', models.TextField(blank=True, null=True, verbose_name='질문2')),
                ('q3', models.TextField(blank=True, null=True, verbose_name='질문3')),
                ('q4', models.TextField(blank=True, null=True, verbose_name='질문4')),
                ('q5', models.FileField(blank=True, null=True, upload_to='user', verbose_name='첨부파일')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='제출 날짜')),
                ('final', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='지원자 이름')),
            ],
        ),
    ]