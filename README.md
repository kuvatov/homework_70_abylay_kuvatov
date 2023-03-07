# homework_58_abylay_kuvatov

superuser:

  login: admin
  password: root
  
task_2:

  from webapp.models import Issue, Type, Status
  import datetime
  
  1. Issue.objects.filter(status_id=3, edited_at__range=[datetime.date.today() - datetime.timedelta(days=30), datetime.date.today()])
  2. 
  3. 
