# Generated by Django 3.2.3 on 2021-06-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0047_poll_polloption_pollvote"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="polloption",
            options={"ordering": ["order"]},
        ),
        migrations.AddField(
            model_name="poll",
            name="poll_type",
            field=models.CharField(
                choices=[("choice", "Choice"), ("multi", "Multi Choice")],
                default="choice",
                max_length=6,
            ),
        ),
        migrations.AddField(
            model_name="polloption",
            name="order",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="poll",
            name="state",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("open", "Open"),
                    ("closed", "Closed"),
                    ("archived", "Archived"),
                ],
                default="draft",
                max_length=8,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="pollvote",
            unique_together={("option", "sender")},
        ),
    ]
