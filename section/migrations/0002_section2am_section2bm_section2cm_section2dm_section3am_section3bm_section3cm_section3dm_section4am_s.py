# Generated by Django 2.0 on 2018-02-13 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_auto_20180130_0409'),
        ('account', '0009_studentprofile_sex'),
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section2AM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Section2BM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Section2CM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Section2DM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Section3AM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Section3BM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Section3CM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Section3DM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Section4AM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Section4BM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Section4CM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Section4DM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseList')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentProfile')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.TeacherProfile')),
            ],
        ),
    ]