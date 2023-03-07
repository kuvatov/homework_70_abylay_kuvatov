# homework_58_abylay_kuvatov

superuser:

  login: admin
  password: root
  
task_2:

  from webapp.models import Issue, Type, Status
  import datetime
  
  1. Issue.objects.filter(status_id=Status.objects.get(name='Выполнено'), edited_at__range=[datetime.date.today() - datetime.timedelta(days=30), datetime.date.today()])
  2. Два запроса с разными значениями:
    а) Issue.objects.filter(status_id=Status.objects.get(name='В процессе'), type=Type.objects.get(name='Ошибка'))
    b) Issue.objects.filter(status_id=Status.objects.get(name='Новый'), type=Type.objects.get(name='Улучшение'))
  3. (Issue.objects.filter(type=Type.objects.get(name='Ошибка')) | Issue.objects.filter(summary__icontains='bug')).exclude(status_id=Status.objects.get(name='Выполнено'))
